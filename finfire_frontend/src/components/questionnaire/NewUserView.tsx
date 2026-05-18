import React, { useState } from 'react';
import { useQuestionnaireStore } from '../../stores/questionnaireStore';
import { getStepConfig } from '../../constants/stepConfig';
import { postPayload } from '../../api/connections';
import { useAuthStore } from '../../stores/authStore';
import { useBrandingStore } from '../../stores/brandingStore';
import { generateThankYouPDF } from '../../utils/thankYouPdf';

import Step1Contact from './steps/Step1Contact';
import StepAccountSetup from './steps/StepAccountSetup';
import Step2Stage from './steps/Step2Stage';
import Step3Entity from './steps/Step3Entity';
import Step4PreCapital from './steps/Step4PreCapital';
import Step5PreMarket from './steps/Step5PreMarket';
import Step6PlannedRaise from './steps/Step6PlannedRaise';
import Step7Rounds from './steps/Step7Rounds';
import Step8UseOfFunds from './steps/Step8UseOfFunds';
import Step9RiskAssessment from './steps/Step9RiskAssessment';
import Step10UpFrontCost from './steps/Step10UpFrontCost';
import Step11PreRating from './steps/Step11PreRating';
import StepPreRating from './steps/StepPreRating';
import Step12Referral from './steps/Step12Referral';
import StepLending from './steps/StepLending';

/** Maps step config keys to React components */
const STEP_COMPONENTS: Record<string, React.FC<{ onComplete: () => void }>> = {
  contact: Step1Contact,
  accountSetup: StepAccountSetup,
  stage: Step2Stage,
  entity: Step3Entity,
  preCapital: Step4PreCapital,
  preMarket: Step5PreMarket,
  plannedRaise: Step6PlannedRaise,
  rounds: Step7Rounds,
  useOfFunds: Step8UseOfFunds,
  risk: Step9RiskAssessment,
  costTime: Step10UpFrontCost,
  documentsPrepared: Step11PreRating,
  preRating: StepPreRating,
  lending: StepLending,
  referral: Step12Referral,
};

/** Default icon for steps without a specific icon */
const DEFAULT_ICON =
  'M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z';

const STEP_ICONS: Record<string, string> = {
  contact:
    'M12 12c2.7 0 4.8-2.1 4.8-4.8S14.7 2.4 12 2.4 7.2 4.5 7.2 7.2 9.3 12 12 12zm0 2.4c-3.2 0-9.6 1.6-9.6 4.8v2.4h19.2v-2.4c0-3.2-6.4-4.8-9.6-4.8z',
  accountSetup:
    'M19.14 12.94c.04-.31.06-.63.06-.94 0-.31-.02-.63-.06-.94l2.03-1.58a.49.49 0 00.12-.61l-1.92-3.32a.488.488 0 00-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54a.484.484 0 00-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.04.31-.06.63-.06.94s.02.63.06.94l-2.03 1.58a.49.49 0 00-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6A3.6 3.6 0 1115.6 12 3.611 3.611 0 0112 15.6z',
  stage:
    'M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z',
  entity:
    'M12 7V3H2v18h20V7H12zM6 19H4v-2h2v2zm0-4H4v-2h2v2zm0-4H4V9h2v2zm0-4H4V5h2v2zm4 12H8v-2h2v2zm0-4H8v-2h2v2zm0-4H8V9h2v2zm0-4H8V5h2v2zm10 12h-8v-2h2v-2h-2v-2h2v-2h-2V9h8v10zm-2-8h-2v2h2v-2zm0 4h-2v2h2v-2z',
  preCapital:
    'M11.8 10.9c-2.27-.59-3-1.2-3-2.15 0-1.09 1.01-1.85 2.7-1.85 1.78 0 2.44.85 2.5 2.1h2.21c-.07-1.72-1.12-3.3-3.21-3.81V3h-3v2.16c-1.94.42-3.5 1.68-3.5 3.61 0 2.31 1.91 3.46 4.7 4.13 2.5.6 3 1.48 3 2.41 0 .69-.49 1.79-2.7 1.79-2.06 0-2.87-.92-2.98-2.1h-2.2c.12 2.19 1.76 3.42 3.68 3.83V21h3v-2.15c1.95-.37 3.5-1.5 3.5-3.55 0-2.84-2.43-3.81-4.7-4.4z',
  preMarket:
    'M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5',
  plannedRaise:
    'M21 18v1c0 1.1-.9 2-2 2H5c-1.11 0-2-.9-2-2V5c0-1.1.89-2 2-2h14c1.1 0 2 .9 2 2v1h-9c-1.11 0-2 .9-2 2v8c0 1.1.89 2 2 2h9zm-9-2h10V8H12v8zm4-2.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z',
  rounds:
    'M12 4V1L8 5l4 4V6c3.31 0 6 2.69 6 6 0 1.01-.25 1.97-.7 2.8l1.46 1.46C19.54 15.03 20 13.57 20 12c0-4.42-3.58-8-8-8zm0 14c-3.31 0-6-2.69-6-6 0-1.01.25-1.97.7-2.8L5.24 7.74C4.46 8.97 4 10.43 4 12c0 4.42 3.58 8 8 8v3l4-4-4-4v3z',
  useOfFunds:
    'M9 11H7v2h2v-2zm4 0h-2v2h2v-2zm4 0h-2v2h2v-2zm2-7h-1V2h-2v2H8V2H6v2H5c-1.11 0-1.99.9-1.99 2L3 20c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 16H5V9h14v11z',
  risk: 'M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm0 10.99h7c-.53 4.12-3.28 7.79-7 8.94V12H5V6.3l7-3.11v8.8z',
  costTime:
    'M19.5 3.5L18 2l-1.5 1.5L15 2l-1.5 1.5L12 2l-1.5 1.5L9 2 7.5 3.5 6 2 4.5 3.5 3 2v20l1.5-1.5L6 22l1.5-1.5L9 22l1.5-1.5L12 22l1.5-1.5L15 22l1.5-1.5L18 22l1.5-1.5L21 22V2l-1.5 1.5zM19 19.09H5V4.91h14v14.18zM6 15h12v2H6zm0-4h12v2H6zm0-4h12v2H6z',
  documentsPrepared:
    'M14 2H6c-1.1 0-2 .9-2 2v16c0 1.1.9 2 2 2h12c1.1 0 2-.9 2-2V8l-6-6zm4 18H6V4h7v5h5v11z',
  preRating:
    'M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z',
  referral:
    'M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zm0 14H6l-2 2V4h16v12z',
  lending:
    'M21 18v1c0 1.1-.9 2-2 2H5c-1.11 0-2-.9-2-2V5c0-1.1.89-2 2-2h14c1.1 0 2 .9 2 2v1h-9c-1.11 0-2 .9-2 2v8c0 1.1.89 2 2 2h9zm-9-2h10V8H12v8zm4-2.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z',
};

const FORM_ID = 'questionnaire-step-form';

const NewUserView: React.FC = () => {
  const currentStep = useQuestionnaireStore((s) => s.currentStep);
  const completedSteps = useQuestionnaireStore((s) => s.completedSteps);
  const animating = useQuestionnaireStore((s) => s.animating);
  const goToStep = useQuestionnaireStore((s) => s.goToStep);
  const markComplete = useQuestionnaireStore((s) => s.markComplete);
  const setView = useQuestionnaireStore((s) => s.setView);
  const setMatchedCapital = useQuestionnaireStore((s) => s.setMatchedCapital);
  const setMatchPdfUrl = useQuestionnaireStore((s) => s.setMatchPdfUrl);
  const user = useAuthStore((s) => s.user);
  const branding = useBrandingStore((s) => s.branding);

  const [matching, setMatching] = useState(false);
  const [matchError, setMatchError] = useState<string | null>(null);

  const stepConfig = getStepConfig();
  const totalSteps = stepConfig.length;
  const isLastStep = currentStep === totalSteps - 1;

  /* ── Match handler ───────────────────────────────────────────────────────── */
  const handleMatch = async () => {
    setMatching(true);
    setMatchError(null);
    try {
      // Generate a thank-you PDF locally instead of calling the backend match API.
      // The user will be contacted by staff after their submission is reviewed.
      const pdfBlob = generateThankYouPDF(user?.username, {
        brandName: branding?.display_name || branding?.name,
        primaryColor: branding?.primary_color,
      });
      const pdfUrl = URL.createObjectURL(pdfBlob);
      setMatchPdfUrl(pdfUrl);
      setMatchedCapital('Submitted');

      // Trigger payload webhook so staff are notified the user finished the survey
      try {
        await postPayload({ payLoadString: { matched: true, timestamp: new Date().toISOString() } });
      } catch {
        // Payload is best-effort, don't block the flow
      }

      setView('matched');
    } catch {
      setMatchError('Something went wrong. Please try again.');
    } finally {
      setMatching(false);
    }
  };

  /* ── onComplete for step forms ───────────────────────────────────────────── */
  const handleStepComplete = () => {
    markComplete(currentStep);
    if (isLastStep) {
      handleMatch();
    } else {
      goToStep(currentStep + 1);
    }
  };

  /* ── Render current step form ────────────────────────────────────────────── */
  const renderStep = () => {
    const cfg = stepConfig[currentStep];
    if (!cfg) return null;
    const StepComponent = STEP_COMPONENTS[cfg.key];
    if (!StepComponent) return <div>Unknown step: {cfg.key}</div>;
    return <StepComponent onComplete={handleStepComplete} />;
  };

  /* ── Checkmark SVG for completed steps ───────────────────────────────────── */
  const CheckSVG = (
    <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
      <path
        d="M2 6l3 3 5-5"
        stroke="#fff"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );

  return (
    <div style={{ display: 'flex', gap: 24 }}>
      {/* ── Left: Step list ─────────────────────────────────────────────────── */}
      <div
        style={{
          width: 200,
          flexShrink: 0,
          background: '#FFFFFF',
          borderRadius: 16,
          border: '1px solid #E2E8F0',
          padding: '16px 14px',
          alignSelf: 'flex-start',
          maxHeight: 'calc(100vh - 120px)',
          overflowY: 'auto',
        }}
      >
        {stepConfig.map((cfg, i) => {
          const isCompleted = completedSteps.has(i);
          const isCurrent = i === currentStep;
          const canClick = isCompleted && !isCurrent;

          return (
            <div
              key={cfg.key}
              onClick={canClick ? () => goToStep(i) : undefined}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 10,
                padding: '7px 8px',
                borderRadius: 8,
                marginBottom: 2,
                background: isCurrent ? '#EFF6FF' : 'transparent',
                cursor: canClick ? 'pointer' : 'default',
              }}
            >
              <div
                style={{
                  width: 22,
                  height: 22,
                  borderRadius: '50%',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  flexShrink: 0,
                  fontSize: 11,
                  fontWeight: 700,
                  ...(isCompleted
                    ? { background: '#2563EB', color: '#fff' }
                    : isCurrent
                      ? {
                          background: '#BFDBFE',
                          border: '2px solid #2563EB',
                          color: '#2563EB',
                        }
                      : { background: '#F1F5F9', color: '#94A3B8' }),
                }}
              >
                {isCompleted ? CheckSVG : i + 1}
              </div>

              <span
                style={{
                  fontSize: 11.5,
                  fontWeight: isCurrent ? 600 : 400,
                  color: isCurrent
                    ? '#1D4ED8'
                    : isCompleted
                      ? '#334155'
                      : '#94A3B8',
                  lineHeight: '14px',
                }}
              >
                {cfg.shortLabel}
              </span>
            </div>
          );
        })}
      </div>

      {/* ── Right: Question card ────────────────────────────────────────────── */}
      <div
        style={{
          flex: 1,
          maxWidth: 520,
          background: '#FFFFFF',
          borderRadius: 20,
          border: '1px solid #E2E8F0',
          padding: '36px 36px 32px',
          opacity: animating ? 0 : 1,
          transform: animating ? 'translateY(8px)' : 'translateY(0)',
          transition: 'opacity 0.15s ease, transform 0.15s ease',
        }}
      >
        {/* Header */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 14,
            marginBottom: 4,
          }}
        >
          <div
            style={{
              width: 40,
              height: 40,
              borderRadius: 12,
              background: '#EFF6FF',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              flexShrink: 0,
            }}
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
              <path
                d={
                  STEP_ICONS[stepConfig[currentStep]?.key] ?? DEFAULT_ICON
                }
                fill="#2563EB"
              />
            </svg>
          </div>
          <div>
            <div
              style={{
                fontSize: 11,
                fontWeight: 700,
                color: '#1D4ED8',
                textTransform: 'uppercase' as const,
                letterSpacing: 0.5,
                marginBottom: 2,
              }}
            >
              Step {currentStep + 1} of {totalSteps}
            </div>
            <div style={{ fontSize: 20, fontWeight: 700, color: '#0F172A' }}>
              {stepConfig[currentStep]?.label}
            </div>
          </div>
        </div>

        <div style={{ height: 1, background: '#F1F5F9', margin: '20px 0' }} />

        {renderStep()}

        {matchError && (
          <div style={{ color: '#DC2626', fontSize: 13, marginTop: 12 }}>
            {matchError}
          </div>
        )}

        <div style={{ display: 'flex', gap: 12, marginTop: 24 }}>
          {currentStep > 0 && (
            <button
              type="button"
              onClick={() => goToStep(currentStep - 1)}
              style={{
                flex: 1,
                padding: 11,
                borderRadius: 12,
                border: '1.5px solid #E2E8F0',
                background: '#FFFFFF',
                color: '#334155',
                fontWeight: 600,
                fontSize: 14,
                cursor: 'pointer',
              }}
            >
              Back
            </button>
          )}

          {!isLastStep && (
            <button
              type="submit"
              form={FORM_ID}
              disabled={matching}
              style={{
                flex: 1,
                padding: 11,
                borderRadius: 12,
                border: 'none',
                background: 'linear-gradient(135deg, #3B82F6, #1D4ED8)',
                color: '#FFFFFF',
                fontWeight: 600,
                fontSize: 14,
                cursor: matching ? 'not-allowed' : 'pointer',
                opacity: matching ? 0.7 : 1,
              }}
            >
              Continue
            </button>
          )}

          {isLastStep && (
            <button
              type="submit"
              form={FORM_ID}
              disabled={matching}
              style={{
                flex: 1,
                padding: 11,
                borderRadius: 12,
                border: 'none',
                background: 'linear-gradient(135deg, #059669, #065F46)',
                color: '#FFFFFF',
                fontWeight: 600,
                fontSize: 14,
                cursor: matching ? 'not-allowed' : 'pointer',
                opacity: matching ? 0.7 : 1,
              }}
            >
              {matching ? 'Matching...' : 'Match capital'}
            </button>
          )}
        </div>
      </div>
    </div>
  );
};

export default NewUserView;
