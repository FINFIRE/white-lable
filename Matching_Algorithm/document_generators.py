"""
Document generation helpers for PDF and Word output.

Contains the CSS styling, PDF rendering via WeasyPrint, and
Word document construction via python-docx.
"""
import base64
import io
import logging
import mimetypes
import os
import re
import uuid
import threading

from django.http import HttpResponse, FileResponse
from django.template.loader import render_to_string
from django.conf import settings
from django.db import connection
from django.templatetags.static import static
from PIL import Image, UnidentifiedImageError
from weasyprint import HTML
from bs4 import BeautifulSoup
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK

from django.conf import settings
BASE_DIR = settings.BASE_DIR


logger = logging.getLogger(__name__)

# Per-image-role max pixel dimensions used when inlining into a PDF.
# Branding images are usually uploaded at unnecessarily high resolutions
# (3000x3000+); downscaling before base64-encoding cuts PDF size by an
# order of magnitude without visibly affecting the print output. The
# letter renders the logo at ~3.05in (≈915 px at 300 dpi) and the
# signature at ≤0.75in tall (~225 px at 300 dpi), so these caps still
# leave plenty of headroom.
_LOGO_MAX_DIM = 1200
_SIGNATURE_MAX_DIM = 800


def _downscale_image_bytes(raw_bytes, max_dim):
    """Resize an image so its longest side <= `max_dim`. Preserves the
    source format (PNG stays PNG, JPEG stays JPEG, etc.) and transparency.
    No-ops if the image already fits, or if PIL can't decode the input —
    in which case the raw bytes are returned unchanged.

    Returns: (bytes, mime_string)
    """
    if not raw_bytes or max_dim is None or max_dim <= 0:
        return raw_bytes, None
    try:
        img = Image.open(io.BytesIO(raw_bytes))
        img.load()
    except (UnidentifiedImageError, OSError, ValueError) as exc:
        logger.warning('Could not decode image for downscale: %s', exc)
        return raw_bytes, None

    src_format = (img.format or 'PNG').upper()
    longest = max(img.width, img.height)
    if longest <= max_dim:
        return raw_bytes, Image.MIME.get(src_format)

    ratio = max_dim / float(longest)
    new_size = (max(1, int(img.width * ratio)), max(1, int(img.height * ratio)))
    resized = img.resize(new_size, Image.LANCZOS)

    out = io.BytesIO()
    save_kwargs = {}
    if src_format == 'JPEG':
        save_kwargs['quality'] = 85
        save_kwargs['optimize'] = True
        # JPEG has no alpha — flatten if needed.
        if resized.mode in ('RGBA', 'LA', 'P'):
            background = Image.new('RGB', resized.size, (255, 255, 255))
            background.paste(resized, mask=resized.convert('RGBA').split()[-1])
            resized = background
    elif src_format == 'PNG':
        save_kwargs['optimize'] = True

    try:
        resized.save(out, format=src_format, **save_kwargs)
    except OSError as exc:
        logger.warning('Could not re-encode downscaled image as %s: %s', src_format, exc)
        return raw_bytes, Image.MIME.get(src_format)

    return out.getvalue(), Image.MIME.get(src_format)


def _image_to_data_uri(file_path, max_dim=None):
    """Read an image file off the local filesystem and return a data: URI,
    or None if the file isn't readable. We inline the bytes so WeasyPrint
    doesn't have to fetch the image over HTTP — which fails inside the
    backend container because tenant hostnames (e.g. `acme.localhost`)
    don't resolve in there.

    If `max_dim` is given, the image is downscaled so its longest side is
    no greater than that pixel count before base64-encoding. Downscale is
    silent — a corrupt or unrecognised file falls back to the raw bytes.
    """
    if not file_path or not os.path.exists(file_path):
        return None
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
    except OSError:
        return None

    if max_dim:
        data, scaled_mime = _downscale_image_bytes(data, max_dim)
    else:
        scaled_mime = None

    mime = scaled_mime
    if not mime:
        mime, _ = mimetypes.guess_type(file_path)
    mime = mime or 'image/png'

    return f'data:{mime};base64,' + base64.b64encode(data).decode('ascii')


def _file_path_for_image_field(file_field):
    """Resolve a Django ImageField/FileField to a local filesystem path,
    or None if no file is attached or it isn't on local storage.
    """
    if not file_field:
        return None
    try:
        return file_field.path
    except (NotImplementedError, ValueError):
        # File is on remote storage (e.g. S3) — no local path available.
        return None


# ──────────────────────────────────────────────────────────────────────
# Tenant branding for generated documents
# ──────────────────────────────────────────────────────────────────────

# Defaults used when no tenant is resolved (or a tenant hasn't set a value).
# Kept here so the letter still renders sensibly outside a tenant context.
_DEFAULT_BRAND_NAME = 'FINFIRE'
_DEFAULT_FOOTER_ADDRESS = '4760 S. Pecos Road, Suite 100-28, Las Vegas, NV 89121'
_DEFAULT_SIGNATORY_NAME = 'Nick Cope'
_DEFAULT_SIGNATORY_TITLE = 'Chief Revenue Officer'
_DEFAULT_SUPPORT_EMAIL = 'Sam@FINFIRE.com'
_DEFAULT_LOGO_RELPATH = 'img/b.png'  # under STATIC_ROOT

# Conservative defaults if a tenant hasn't set their own colors. Dark slate
# + medium blue read as professional on white and have enough contrast for
# both body accents and white-on-color badges.
_DEFAULT_PRIMARY_COLOR = '#0F172A'
_DEFAULT_ACCENT_COLOR = '#3B82F6'


def _default_logo_data_uri():
    """data: URI for the bundled fallback FINFIRE logo, or None if missing."""
    return _image_to_data_uri(
        os.path.join(settings.BASE_DIR, 'static', _DEFAULT_LOGO_RELPATH),
        max_dim=_LOGO_MAX_DIM,
    )


def get_letter_branding(request):
    """Resolve white-label branding for the active tenant. Returns a dict
    with the fields the letter templates expect, falling back to legacy
    FINFIRE defaults when a tenant hasn't set a value (so an unbranded
    install still produces a usable letter).

    Images (`logo_url`, `signature_url`) are returned as inline `data:`
    URIs read directly from the local filesystem so WeasyPrint never needs
    to make an HTTP request — fetching over HTTP fails inside the backend
    container because tenant hostnames don't resolve there.

    Callers should merge this into the template/render context before
    calling generate_pdf_response / generate_word_response.
    """
    tenant = getattr(connection, 'tenant', None)
    is_real_tenant = (
        tenant is not None
        and getattr(tenant, 'schema_name', 'public') != 'public'
    )

    if is_real_tenant:
        brand_name = (tenant.display_name or tenant.name or _DEFAULT_BRAND_NAME).strip()
        # Inline tenant logo if uploaded, else fall back to the bundled FINFIRE logo.
        logo_url = (
            _image_to_data_uri(_file_path_for_image_field(tenant.logo), max_dim=_LOGO_MAX_DIM)
            or _default_logo_data_uri()
        )
        signature_url = _image_to_data_uri(
            _file_path_for_image_field(tenant.signature_image),
            max_dim=_SIGNATURE_MAX_DIM,
        )
        signatory_name = (tenant.signatory_name or _DEFAULT_SIGNATORY_NAME).strip()
        signatory_title = (tenant.signatory_title or _DEFAULT_SIGNATORY_TITLE).strip()
        support_email = (tenant.support_email or _DEFAULT_SUPPORT_EMAIL).strip()
        contact_phone = (tenant.contact_phone or '').strip()
        address = (tenant.address or _DEFAULT_FOOTER_ADDRESS).strip()
        primary_color = (tenant.primary_color or _DEFAULT_PRIMARY_COLOR).strip()
        accent_color = (tenant.accent_color or _DEFAULT_ACCENT_COLOR).strip()
    else:
        brand_name = _DEFAULT_BRAND_NAME
        logo_url = _default_logo_data_uri()
        signature_url = None
        signatory_name = _DEFAULT_SIGNATORY_NAME
        signatory_title = _DEFAULT_SIGNATORY_TITLE
        support_email = _DEFAULT_SUPPORT_EMAIL
        contact_phone = ''
        address = _DEFAULT_FOOTER_ADDRESS
        primary_color = _DEFAULT_PRIMARY_COLOR
        accent_color = _DEFAULT_ACCENT_COLOR

    # Header text shown on every page (`@page @top-center` in PDF, header
    # paragraph in Word). Single line, single‑line and uppercase.
    page_header = f'{brand_name} REPORT'.upper()

    # Footer composes address + (optional) phone on a single line. We
    # normalise CRLF/CR/LF (admin textareas on Windows browsers submit
    # multi-line text with '\r\n' line endings) — leaving a stray '\r' in
    # the CSS @bottom-center string literal would break the @page rule.
    flat_address = re.sub(r'\s*[\r\n]+\s*', ', ', address).strip(', ').strip()
    page_footer = flat_address
    if contact_phone:
        page_footer = f'{page_footer} • {contact_phone}' if page_footer else contact_phone

    return {
        'brand_name': brand_name,
        'page_header': page_header,
        'page_footer': page_footer,
        'address_lines': [ln for ln in address.splitlines() if ln.strip()],
        'logo_url': logo_url,
        'signature_url': signature_url,
        'signatory_name': signatory_name,
        'signatory_title': signatory_title,
        'support_email': support_email,
        'contact_phone': contact_phone,
        'primary_color': primary_color,
        'accent_color': accent_color,
    }


def _resolve_letter_logo_for_docx(branding):
    """Return a file path the python-docx add_picture() can read.
    Prefers the tenant's uploaded logo (from MEDIA_ROOT), falling back to
    the bundled FINFIRE default under STATIC_ROOT.
    """
    tenant = getattr(connection, 'tenant', None)
    if tenant is not None and getattr(tenant, 'logo', None):
        try:
            return tenant.logo.path
        except Exception:
            pass
    return os.path.join(settings.BASE_DIR, 'static', 'img', 'b.png')


# ──────────────────────────────────────────────────────────────────────
# PDF Generation
# ──────────────────────────────────────────────────────────────────────

PDF_CSS_TEMPLATE = '''
<style>
    body {
        font-family: Arial, sans-serif;
        text-align: center;
        margin: 0;
        padding: 0;
    }
    .container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }
    .logo {
        display: inline-block;
        margin: 0;
        padding: 0;
        line-height: 0;
    }
    .logo img {
        display: inline;
        vertical-align: middle;
    }
    .spacing {
        margin-top: 20px;
    }
    .content {
        text-align: left;
        margin-top: 20px;
        line-height: 1.5;
        font-family: "Times New Roman", Times, serif;
        font-size: 11px;
    }
    .capital-source, .pricing {
        display: flex;
        justify-content: space-between;
    }
    .pricing-summary {
        margin-top: 20px;
        text-align: right;
    }
    .signature {
        margin-top: 40px;
        text-align: left;
    }
    .button {
        margin-top: 20px;
        text-align: right;
    }
    .page {
        margin: 0 auto;
        padding: 20px;
        max-width: 80%;
        border: 1px solid #ccc;
        border-radius: 10px;
        background-color: #f9f9f9;
    }
    .page-break {
        page-break-after: always;
    }
    @page {
        size: letter;
        /* Margins kept moderate so the cover letter (with logo head,
           recipient block, body, 3 steps, summary, email line, signature)
           comfortably fits on a single page. */
        margin: 0.75in 0.85in;
        @top-center {
            content: "__PAGE_HEADER__";
            font-size: 10px;
            font-weight: bold;
        }
        @bottom-center {
            content: "__PAGE_FOOTER__";
            font-size: 10px;
        }
        @bottom-right {
            content: counter(page);
            font-size: 10px;
        }
    }
</style>
'''


def _escape_css_string(value):
    """Escape a string so it can sit safely inside a CSS `content: "…"` value.

    Strips raw control characters (CR/LF/TAB) — they're illegal inside an
    unescaped CSS string and would otherwise trigger a parser error that
    invalidates the whole @page rule (which is how an admin-entered
    multi-line address full of '\\r\\n' line endings ends up wiping the
    page footer AND header).
    """
    if not value:
        return ''
    # Collapse any CRLF / CR / LF / TAB sequences into a single space, then
    # backslash-escape characters that have meaning inside a CSS string.
    cleaned = re.sub(r'[\r\n\t]+', ' ', value)
    cleaned = re.sub(r' +', ' ', cleaned).strip()
    return cleaned.replace('\\', '\\\\').replace('"', '\\"')


def generate_pdf_response(request, context, company_name):
    """
    Render the letter as a PDF and return a FileResponse.

    Args:
        request: Django HttpRequest (needed for absolute URLs).
        context: Template context dict.
        company_name: Company name for the PDF header (the registered
            user's business name; combined with tenant brand for the
            header banner).

    Returns:
        FileResponse with the PDF attachment.
    """
    branding = get_letter_branding(request)
    # The template reads `branding.*` for logo/signature/signatory; merge
    # without overwriting any key the caller already supplied.
    context = {**context, 'branding': context.get('branding') or branding}

    rendered_html = render_to_string('letterpdf.html', context)

    # PDF page header banner: "<COMPANY> <BRAND> REPORT" (or just the
    # brand if no company is set on the user).
    brand_header = branding['page_header']  # already uppercase
    if company_name and company_name.strip().lower() != "none":
        page_header = f'{company_name.strip().upper()} {brand_header}'
    else:
        page_header = brand_header

    css_style = (
        PDF_CSS_TEMPLATE
        .replace('__PAGE_HEADER__', _escape_css_string(page_header))
        .replace('__PAGE_FOOTER__', _escape_css_string(branding['page_footer']))
    )
    # Inject as a second, separate <style> block in <head> rather than
    # nesting it inside the template's existing <style>. The previous
    # nest-by-replace produced a literal `<style>` text token mid-stylesheet,
    # which fails CSS parsing and causes WeasyPrint to drop the @page rules
    # (so the header and footer never rendered).
    if '</head>' in rendered_html:
        rendered_html = rendered_html.replace('</head>', f'{css_style}\n</head>', 1)
    else:
        # Fallback for templates without <head>: prepend before <body>
        rendered_html = rendered_html.replace('<body', f'{css_style}\n<body', 1)

    html = HTML(string=rendered_html, base_url=request.build_absolute_uri('/'))
    pdf_bytes = html.write_pdf()

    # Save to temp file
    unique_filename = f"FINFIRE_Letter_{uuid.uuid4().hex}.pdf"
    media_dir = os.path.join(settings.MEDIA_ROOT, 'temp_pdfs')
    os.makedirs(media_dir, exist_ok=True)
    pdf_path = os.path.join(media_dir, unique_filename)

    with open(pdf_path, 'wb') as f:
        f.write(pdf_bytes)

    # Serve file and schedule cleanup
    response = FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="FINFIRE_Letter.pdf"'

    def delete_file():
        try:
            if os.path.exists(pdf_path):
                os.remove(pdf_path)
        except Exception as e:
            print(f"Error deleting file {pdf_path}: {e}")

    timer = threading.Timer(30.0, delete_file)
    timer.start()

    return response


# ──────────────────────────────────────────────────────────────────────
# Word Document Generation
# ──────────────────────────────────────────────────────────────────────

def generate_word_response(request, context, company_name):
    """
    Render the letter as a Word document (.docx) and return an HttpResponse.

    Args:
        request: Django HttpRequest.
        context: Template context dict.
        company_name: Company name for the document header.

    Returns:
        HttpResponse with the .docx attachment.
    """
    branding = get_letter_branding(request)
    context = {**context, 'branding': context.get('branding') or branding}

    rendered_html = render_to_string('letter499pdf.html', context)
    soup = BeautifulSoup(rendered_html, "html.parser")

    document = Document()

    # Set default font
    style = document.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(10)

    section = document.sections[-1]

    # Header — tenant-aware brand banner with the registered user's company
    header = section.header
    header_paragraph = header.paragraphs[0]
    brand_header = branding['page_header']
    if company_name and company_name.strip().lower() != "none":
        header_paragraph.text = f"{company_name.strip().upper()} {brand_header}"
    else:
        header_paragraph.text = brand_header
    header_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    header_run = header_paragraph.runs[0]
    header_run.bold = False
    header_run.font.size = Pt(10)
    header_run.font.name = "Times New Roman"

    # Logo — tenant logo if uploaded, otherwise bundled FINFIRE fallback
    img_paragraph = document.add_paragraph()
    img_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    img_run = img_paragraph.add_run()
    try:
        img_run.add_picture(
            _resolve_letter_logo_for_docx(branding),
            width=Inches(2.44), height=Inches(0.656),
        )
    except Exception:
        # If the tenant uploaded a file that python-docx can't read, fall
        # back silently to the bundled default rather than 500-ing.
        img_run.add_picture(
            os.path.join(settings.BASE_DIR, 'static', 'img', 'b.png'),
            width=Inches(2.44), height=Inches(0.656),
        )

    # Process HTML containers
    containers = soup.find_all('div', class_='container')
    for idx, container in enumerate(containers):
        content_divs = container.find_all('div', class_='content')
        for content_div in content_divs:
            for element in content_div.find_all(['p', 'center', 'div']):
                # Skip nested elements to avoid duplication
                skip = False
                parent = element.parent
                while parent is not None and parent != content_div:
                    if parent.name in ('p', 'center'):
                        skip = True
                        break
                    parent = parent.parent
                if skip:
                    continue

                if element.name == "center":
                    _add_centered_element(document, element)
                elif element.name == "p":
                    _add_paragraph_element(document, element)
                elif element.name == "div" and 'class' in element.attrs:
                    pass  # Signature section placeholder

        # Page break between containers
        if idx < len(containers) - 1:
            last_paragraph = document.paragraphs[-1]
            if last_paragraph.runs:
                last_paragraph.runs[-1].add_break(WD_BREAK.PAGE)
            else:
                last_paragraph.add_run().add_break(WD_BREAK.PAGE)

    # Footer — tenant address + contact number on one line
    section = document.sections[-1]
    footer = section.footer
    footer_paragraph = footer.paragraphs[0]
    footer_paragraph.text = branding['page_footer']
    footer_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer_paragraph.style.font.size = Pt(8)
    footer_paragraph.style.font.name = 'Times New Roman'

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
    response["Content-Disposition"] = 'attachment; filename="FINFIRE_Letter.docx"'
    document.save(response)
    return response


def _add_centered_element(document, element):
    """Add a centered element to the Word document."""
    paragraph = document.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    if element.find('b') and element.find('u'):
        run = paragraph.add_run(element.text.strip())
        run.bold = True
        run.underline = True
    else:
        run = paragraph.add_run(element.text.strip())

    run.font.name = 'Times New Roman'
    run.font.size = Pt(10)


def _add_paragraph_element(document, element):
    """Add a paragraph element to the Word document."""
    center_child = element.find('center')
    if center_child:
        paragraph = document.add_paragraph()
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        has_bold = center_child.find('b') is not None
        has_underline = center_child.find('u') is not None
        ancestor = center_child.parent
        while ancestor is not None and ancestor != element:
            if ancestor.name == 'b':
                has_bold = True
            if ancestor.name == 'u':
                has_underline = True
            ancestor = ancestor.parent
        run = paragraph.add_run(center_child.text.strip())
        run.bold = has_bold
        run.underline = has_underline
        run.font.name = 'Times New Roman'
        run.font.size = Pt(10)
    else:
        paragraph = document.add_paragraph()
        paragraph.style = document.styles['Normal']

        for part in element.contents:
            if isinstance(part, str):
                run = paragraph.add_run(part.strip())
                run.font.name = 'Times New Roman'
                run.font.size = Pt(10)
            elif part.name == "br":
                paragraph.add_run().add_break(WD_BREAK.LINE)
            elif part.name == "b":
                run = paragraph.add_run(part.text.strip())
                run.bold = True
                if part.find('u'):
                    run.underline = True
                run.font.name = 'Times New Roman'
                run.font.size = Pt(10)
            elif part.name == "u":
                run = paragraph.add_run(part.text.strip())
                run.underline = True
                if part.find('b'):
                    run.bold = True
                run.font.name = 'Times New Roman'
                run.font.size = Pt(10)
            elif part.name == "a":
                run = paragraph.add_run(part.text.strip())
                run.font.name = 'Times New Roman'
                run.font.size = Pt(10)
                run.font.color.rgb = RGBColor(0, 0, 255)
