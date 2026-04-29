import React from 'react';
import { useQuestionnaireStore } from '../../stores/questionnaireStore';
import { getStepConfig, getTotalSteps } from '../../constants/stepConfig';
import StepNavigation from './StepNavigation';
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

const QuestionnairePanel: React.FC = () => {
  const { currentStep, completedSteps, goNext, goPrev, markComplete } =
    useQuestionnaireStore();

  const stepConfig = getStepConfig();
  const totalSteps = getTotalSteps();

  const handleStepComplete = () => {
    markComplete(currentStep);
    goNext();
  };

  const renderStep = () => {
    const cfg = stepConfig[currentStep];
    if (!cfg) return null;
    const StepComponent = STEP_COMPONENTS[cfg.key];
    if (!StepComponent) return null;
    return <StepComponent onComplete={handleStepComplete} />;
  };

  const isFirstStep = currentStep === 0;
  const isLastStep = currentStep === totalSteps - 1;

  return (
    <div className="flex h-full flex-col border-l border-gray-200 bg-white">
      {/* ── Progress Dots ─────────────────────────────────────────────────── */}
      <div className="border-b border-gray-200 px-6 pt-5 pb-4">
        <div className="flex items-center justify-center gap-2">
          {stepConfig.map((cfg, idx) => {
            let dotColor = 'bg-gray-300';
            if (completedSteps.has(idx)) dotColor = 'bg-green-500';
            if (idx === currentStep) dotColor = 'bg-blue-500';

            return (
              <span
                key={cfg.key}
                className={`inline-block h-2.5 w-2.5 rounded-full transition-colors ${dotColor}`}
                title={cfg.label}
              />
            );
          })}
        </div>

        <p className="mt-3 text-center text-xs font-medium uppercase tracking-wide text-slate-500">
          Step {currentStep + 1} of {totalSteps}
        </p>
        <h2 className="mt-1 text-center text-base font-semibold text-slate-900">
          {stepConfig[currentStep]?.label}
        </h2>
      </div>

      {/* ── Form Area (scrollable) ────────────────────────────────────────── */}
      <div className="flex-1 overflow-y-auto px-6 py-5">{renderStep()}</div>

      {/* ── Navigation ────────────────────────────────────────────────────── */}
      <StepNavigation
        onPrev={goPrev}
        isFirstStep={isFirstStep}
        isLastStep={isLastStep}
        isSubmitting={false}
      />
    </div>
  );
};

export default QuestionnairePanel;
