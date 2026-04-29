"""
Document generation helpers for PDF and Word output.

Contains the CSS styling, PDF rendering via WeasyPrint, and
Word document construction via python-docx.
"""
import os
import uuid
import threading

from django.http import HttpResponse, FileResponse
from django.template.loader import render_to_string
from django.conf import settings
from django.templatetags.static import static
from weasyprint import HTML
from bs4 import BeautifulSoup
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK

from django.conf import settings
BASE_DIR = settings.BASE_DIR


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
        margin: 1in;
        @top-center {
            content: "FINFIRE REPORT";
            font-size: 11px;
            font-weight: bold;
        }
        @bottom-center {
            content: "4760 S. Pecos Road, Suite 100-28, Las Vegas, NV 89121";
            font-size: 11px;
        }
        @bottom-right {
            content: counter(page);
            font-size: 11px;
        }
    }
</style>
'''


def generate_pdf_response(request, context, company_name):
    """
    Render the letter as a PDF and return a FileResponse.

    Args:
        request: Django HttpRequest (needed for absolute URLs).
        context: Template context dict.
        company_name: Company name for the PDF header.

    Returns:
        FileResponse with the PDF attachment.
    """
    rendered_html = render_to_string('letterpdf.html', context)

    # Build header text
    if company_name.strip().lower() == "none":
        company_report = 'FINFIRE REPORT'
    else:
        company_report = company_name + ' FINFIRE REPORT'

    css_style = PDF_CSS_TEMPLATE.replace('FINFIRE REPORT', company_report.upper())
    rendered_html = rendered_html.replace('</style>', f'{css_style}</style>')

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
    rendered_html = render_to_string('letter499pdf.html', context)
    soup = BeautifulSoup(rendered_html, "html.parser")

    document = Document()

    # Set default font
    style = document.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(10)

    section = document.sections[-1]

    # Header
    header = section.header
    header_paragraph = header.paragraphs[0]
    if company_name.strip().lower() == "none":
        header_paragraph.text = "FINFIRE REPORT"
    else:
        header_paragraph.text = f"{company_name} FINFIRE REPORT"
    header_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    header_run = header_paragraph.runs[0]
    header_run.bold = False
    header_run.font.size = Pt(10)
    header_run.font.name = "Times New Roman"

    # Logo
    img_paragraph = document.add_paragraph()
    img_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    img_run = img_paragraph.add_run()
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

    # Footer
    section = document.sections[-1]
    footer = section.footer
    footer_paragraph = footer.paragraphs[0]
    footer_paragraph.text = "4760 S. Pecos Road, Suite 100-28, Las Vegas, NV 89121"
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
