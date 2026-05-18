import jsPDF from 'jspdf';

/** Branding the thank-you PDF should pick up from the active tenant. */
export interface ThankYouPdfBranding {
  /** Display name for the tenant (falls back to "FINFIRE"). */
  brandName?: string;
  /** Hex like "#1d4ed8". Lighter/darker shades derived via mix(). */
  primaryColor?: string;
}

const LEGACY_BRAND_NAME = 'FINFIRE';
const LEGACY_PRIMARY: RGB = [29, 78, 216]; // tailwind blue-700

type RGB = [number, number, number];

function hexToRgb(hex?: string): RGB | null {
  if (!hex) return null;
  const m = hex.trim().replace('#', '').match(/^([0-9a-f]{6})$/i);
  if (!m) return null;
  const n = parseInt(m[1], 16);
  return [(n >> 16) & 0xff, (n >> 8) & 0xff, n & 0xff];
}

/** Mix `rgb` with white by `t` (0 = unchanged, 1 = pure white). */
function lighten(rgb: RGB, t: number): RGB {
  return [
    Math.round(rgb[0] + (255 - rgb[0]) * t),
    Math.round(rgb[1] + (255 - rgb[1]) * t),
    Math.round(rgb[2] + (255 - rgb[2]) * t),
  ];
}

/** Mix `rgb` with black by `t` (0 = unchanged, 1 = pure black). */
function darken(rgb: RGB, t: number): RGB {
  return [
    Math.round(rgb[0] * (1 - t)),
    Math.round(rgb[1] * (1 - t)),
    Math.round(rgb[2] * (1 - t)),
  ];
}

/**
 * Generate a thank-you PDF for the user after they complete the
 * questionnaire. Tenant `brandName` + `primaryColor` are used everywhere
 * the legacy "FINFIRE" string and blue header lived. Returns a Blob
 * that can be displayed in an iframe or downloaded.
 */
export function generateThankYouPDF(
  userName?: string,
  branding?: ThankYouPdfBranding,
): Blob {
  const brandName = (branding?.brandName || LEGACY_BRAND_NAME).trim();
  const primary = hexToRgb(branding?.primaryColor) ?? LEGACY_PRIMARY;
  // Derived shades for the highlight box and accents.
  const primaryFill = lighten(primary, 0.92); // very light (≈primary-50)
  const primaryBorder = lighten(primary, 0.75); // soft (≈primary-200)
  const primaryDarker = darken(primary, 0.2); // step-text (≈primary-700)

  const doc = new jsPDF({
    orientation: 'portrait',
    unit: 'mm',
    format: 'a4',
  });

  const pageWidth = doc.internal.pageSize.getWidth();
  const pageHeight = doc.internal.pageSize.getHeight();
  const margin = 20;
  const contentWidth = pageWidth - margin * 2;

  // ── Top header band (tenant brand color) ───────────────────────────────
  doc.setFillColor(primary[0], primary[1], primary[2]);
  doc.rect(0, 0, pageWidth, 30, 'F');

  doc.setTextColor(255, 255, 255);
  doc.setFont('helvetica', 'bold');
  doc.setFontSize(22);
  doc.text(brandName.toUpperCase(), margin, 19);

  doc.setFont('helvetica', 'normal');
  doc.setFontSize(10);
  doc.text('Capital Matching Platform', margin, 25);

  // ── Date (top right) ───────────────────────────────────────────────────
  const today = new Date().toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });
  doc.setFontSize(9);
  doc.text(today, pageWidth - margin, 19, { align: 'right' });

  // ── Greeting ───────────────────────────────────────────────────────────
  doc.setTextColor(15, 23, 42); // slate-900
  doc.setFont('helvetica', 'bold');
  doc.setFontSize(20);
  doc.text('Thank You!', margin, 55);

  doc.setFont('helvetica', 'normal');
  doc.setFontSize(13);
  doc.setTextColor(71, 85, 105); // slate-600
  const greeting = userName ? `Dear ${userName},` : 'Dear Valued User,';
  doc.text(greeting, margin, 67);

  // ── Body paragraphs ────────────────────────────────────────────────────
  doc.setTextColor(51, 65, 85); // slate-700
  doc.setFontSize(11);

  const body1 = `Thank you for taking the time to complete the ${brandName} capital matching questionnaire. We truly appreciate the detailed information you have shared with us about your business, financial profile, and capital requirements.`;

  const body2 =
    'Our team is now reviewing your responses to identify the most suitable capital sources and intermediaries for your specific situation. This careful review ensures that we recommend the right capital type, the right partners, and the right strategy tailored to your goals.';

  const body3 =
    'A member of our staff will be in touch with you shortly to discuss your match results, answer any questions you may have, and walk you through the next steps. Please keep an eye on your inbox for our follow-up communication.';

  const body4 =
    'In the meantime, if you have any urgent questions or wish to update your information, feel free to reach out to us at any time. We are committed to helping you find the right capital, faster.';

  let y = 80;
  const lineHeight = 6;

  const addParagraph = (text: string) => {
    const lines = doc.splitTextToSize(text, contentWidth);
    doc.text(lines, margin, y);
    y += lines.length * lineHeight + 4;
  };

  addParagraph(body1);
  addParagraph(body2);
  addParagraph(body3);
  addParagraph(body4);

  // ── Highlighted "What happens next" box (tenant primary tones) ─────────
  y += 4;
  doc.setFillColor(primaryFill[0], primaryFill[1], primaryFill[2]);
  doc.setDrawColor(primaryBorder[0], primaryBorder[1], primaryBorder[2]);
  const boxHeight = 38;
  doc.roundedRect(margin, y, contentWidth, boxHeight, 3, 3, 'FD');

  doc.setTextColor(primary[0], primary[1], primary[2]);
  doc.setFont('helvetica', 'bold');
  doc.setFontSize(11);
  doc.text('What happens next?', margin + 6, y + 9);

  doc.setFont('helvetica', 'normal');
  doc.setFontSize(10);
  doc.setTextColor(primaryDarker[0], primaryDarker[1], primaryDarker[2]);
  const steps = [
    '1. Our team reviews your questionnaire responses (within 1-2 business days).',
    '2. We identify and validate the best-fit capital types and intermediaries.',
    '3. A staff member contacts you to share your personalized match report.',
  ];
  let stepY = y + 16;
  steps.forEach((step) => {
    const lines = doc.splitTextToSize(step, contentWidth - 12);
    doc.text(lines, margin + 6, stepY);
    stepY += lines.length * 5;
  });

  y += boxHeight + 12;

  // ── Closing ────────────────────────────────────────────────────────────
  doc.setTextColor(51, 65, 85);
  doc.setFont('helvetica', 'normal');
  doc.setFontSize(11);
  doc.text('Warm regards,', margin, y);
  y += 7;

  doc.setFont('helvetica', 'bold');
  doc.text(`The ${brandName} Team`, margin, y);

  // ── Footer ─────────────────────────────────────────────────────────────
  doc.setDrawColor(226, 232, 240);
  doc.line(margin, pageHeight - 18, pageWidth - margin, pageHeight - 18);

  doc.setFont('helvetica', 'normal');
  doc.setFontSize(8);
  doc.setTextColor(148, 163, 184);
  doc.text(
    `${brandName} Capital Matching Platform • Confidential`,
    pageWidth / 2,
    pageHeight - 12,
    { align: 'center' },
  );
  doc.text(
    'This document was generated automatically upon completion of your survey.',
    pageWidth / 2,
    pageHeight - 7,
    { align: 'center' },
  );

  return doc.output('blob');
}
