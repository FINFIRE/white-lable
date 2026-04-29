import React from 'react';
import { useQuestionnaireStore } from '../../stores/questionnaireStore';

const MatchResults: React.FC = () => {
  const matchPdfUrl = useQuestionnaireStore((s) => s.matchPdfUrl);
  const setView = useQuestionnaireStore((s) => s.setView);
  const setMatchedCapital = useQuestionnaireStore((s) => s.setMatchedCapital);
  const setMatchPdfUrl = useQuestionnaireStore((s) => s.setMatchPdfUrl);
  const goToStep = useQuestionnaireStore((s) => s.goToStep);

  const handleNewUser = () => {
    // Revoke the old blob URL to free memory
    if (matchPdfUrl) {
      URL.revokeObjectURL(matchPdfUrl);
    }
    setMatchedCapital(null);
    setMatchPdfUrl(null);
    goToStep(0);
    setView('newUser');
  };

  const handleDownload = () => {
    if (!matchPdfUrl) return;
    const link = document.createElement('a');
    link.href = matchPdfUrl;
    link.download = 'finfire-thank-you.pdf';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  const handlePrint = () => {
    if (!matchPdfUrl) return;
    const printWindow = window.open(matchPdfUrl, '_blank');
    if (printWindow) {
      printWindow.addEventListener('load', () => {
        printWindow.print();
      });
    }
  };

  return (
    <div style={{ maxWidth: 900, margin: '0 auto' }}>
      <div
        style={{
          background: '#FFFFFF',
          borderRadius: 20,
          border: '1px solid #E2E8F0',
          padding: 36,
        }}
      >
        {/* ── Header ─────────────────────────────────────────────────────────── */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 14,
            marginBottom: 24,
          }}
        >
          <div
            style={{
              width: 48,
              height: 48,
              borderRadius: '50%',
              background: '#DCFCE7',
              border: '2px solid #BBF7D0',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              flexShrink: 0,
            }}
          >
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
              <path
                d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"
                fill="#16A34A"
              />
            </svg>
          </div>
          <div>
            <div
              style={{
                fontSize: 22,
                fontWeight: 700,
                color: '#0F172A',
              }}
            >
              Submission Received!
            </div>
            <div style={{ fontSize: 14, color: '#64748B' }}>
              Thank you. Our staff will contact you after reviewing your information.
            </div>
          </div>
        </div>

        {/* ── PDF Viewer ─────────────────────────────────────────────────────── */}
        {matchPdfUrl ? (
          <div
            style={{
              border: '1px solid #E2E8F0',
              borderRadius: 12,
              overflow: 'hidden',
              marginBottom: 24,
              background: '#F8FAFC',
            }}
          >
            <iframe
              src={matchPdfUrl}
              title="Match Letter PDF"
              style={{
                width: '100%',
                height: 600,
                border: 'none',
              }}
            />
          </div>
        ) : (
          <div
            style={{
              background: '#FEF3C7',
              borderRadius: 12,
              padding: '20px 24px',
              marginBottom: 24,
              color: '#92400E',
              fontSize: 14,
              textAlign: 'center',
            }}
          >
            No PDF available. Please try matching again.
          </div>
        )}

        {/* ── Action Buttons ─────────────────────────────────────────────────── */}
        <div style={{ display: 'flex', gap: 12 }}>
          <button
            type="button"
            onClick={handleDownload}
            disabled={!matchPdfUrl}
            style={{
              flex: 1,
              padding: 12,
              borderRadius: 12,
              border: 'none',
              background: matchPdfUrl
                ? 'linear-gradient(135deg, #059669, #065F46)'
                : '#E2E8F0',
              color: matchPdfUrl ? '#FFFFFF' : '#94A3B8',
              fontWeight: 600,
              fontSize: 14,
              cursor: matchPdfUrl ? 'pointer' : 'not-allowed',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: 8,
            }}
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
              <path
                d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"
                fill="currentColor"
              />
            </svg>
            Download PDF
          </button>
          <button
            type="button"
            onClick={handlePrint}
            disabled={!matchPdfUrl}
            style={{
              flex: 1,
              padding: 12,
              borderRadius: 12,
              border: 'none',
              background: matchPdfUrl
                ? 'linear-gradient(135deg, #3B82F6, #1D4ED8)'
                : '#E2E8F0',
              color: matchPdfUrl ? '#FFFFFF' : '#94A3B8',
              fontWeight: 600,
              fontSize: 14,
              cursor: matchPdfUrl ? 'pointer' : 'not-allowed',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: 8,
            }}
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
              <path
                d="M19 8H5c-1.66 0-3 1.34-3 3v6h4v4h12v-4h4v-6c0-1.66-1.34-3-3-3zm-3 11H8v-5h8v5zm3-7c-.55 0-1-.45-1-1s.45-1 1-1 1 .45 1 1-.45 1-1 1zm-1-9H6v4h12V3z"
                fill="currentColor"
              />
            </svg>
            Print
          </button>
          <button
            type="button"
            onClick={handleNewUser}
            style={{
              flex: 1,
              padding: 12,
              borderRadius: 12,
              border: '1.5px solid #E2E8F0',
              background: '#FFFFFF',
              color: '#334155',
              fontWeight: 600,
              fontSize: 14,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              gap: 8,
            }}
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
              <path
                d="M12 5v14M5 12h14"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
              />
            </svg>
            New User
          </button>
        </div>
      </div>
    </div>
  );
};

export default MatchResults;
