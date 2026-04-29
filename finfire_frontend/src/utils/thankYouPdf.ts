import jsPDF from 'jspdf';

/**
 * Generate a thank-you PDF for the user after they complete the questionnaire.
 * Returns a Blob that can be displayed in an iframe or downloaded.
 */
export function generateThankYouPDF(userName?: string): Blob {
  const doc = new jsPDF({
    orientation: 'portrait',
    unit: 'mm',
    format: 'a4',
  });

  const pageWidth = doc.internal.pageSize.getWidth();
  const pageHeight = doc.internal.pageSize.getHeight();
  const margin = 20;
  const contentWidth = pageWidth - margin * 2;

  // ── Top header band (FINFIRE branding) ─────────────────────────────────
  doc.setFillColor(29, 78, 216); // primary blue
  doc.rect(0, 0, pageWidth, 30, 'F');

  doc.setTextColor(255, 255, 255);
  doc.setFont('helvetica', 'bold');
  doc.setFontSize(22);
  doc.text('FINFIRE', margin, 19);

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

  const body1 =
    'Thank you for taking the time to complete the FINFIRE capital matching questionnaire. We truly appreciate the detailed information you have shared with us about your business, financial profile, and capital requirements.';

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

  // ── Highlighted "What happens next" box ────────────────────────────────
  y += 4;
  doc.setFillColor(239, 246, 255); // primary-50
  doc.setDrawColor(191, 219, 254); // primary-200
  const boxHeight = 38;
  doc.roundedRect(margin, y, contentWidth, boxHeight, 3, 3, 'FD');

  doc.setTextColor(29, 78, 216);
  doc.setFont('helvetica', 'bold');
  doc.setFontSize(11);
  doc.text('What happens next?', margin + 6, y + 9);

  doc.setFont('helvetica', 'normal');
  doc.setFontSize(10);
  doc.setTextColor(30, 64, 175);
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
  doc.text('The FINFIRE Team', margin, y);

  // ── Footer ─────────────────────────────────────────────────────────────
  doc.setDrawColor(226, 232, 240);
  doc.line(margin, pageHeight - 18, pageWidth - margin, pageHeight - 18);

  doc.setFont('helvetica', 'normal');
  doc.setFontSize(8);
  doc.setTextColor(148, 163, 184);
  doc.text(
    'FINFIRE Capital Matching Platform • Confidential',
    pageWidth / 2,
    pageHeight - 12,
    { align: 'center' }
  );
  doc.text(
    'This document was generated automatically upon completion of your survey.',
    pageWidth / 2,
    pageHeight - 7,
    { align: 'center' }
  );

  return doc.output('blob');
}
