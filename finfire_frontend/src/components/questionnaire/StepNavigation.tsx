import React from 'react';
import Button from '../ui/Button';

interface StepNavigationProps {
  onPrev: () => void;
  isFirstStep: boolean;
  isLastStep: boolean;
  isSubmitting: boolean;
}

const StepNavigation: React.FC<StepNavigationProps> = ({
  onPrev,
  isFirstStep,
  isLastStep,
  isSubmitting,
}) => {
  return (
    <div className="flex items-center justify-between gap-3 border-t border-gray-200 bg-white px-6 py-4">
      {!isFirstStep ? (
        <Button
          type="button"
          variant="secondary"
          onClick={onPrev}
          disabled={isSubmitting}
        >
          Previous
        </Button>
      ) : (
        <div />
      )}

      <Button
        type="submit"
        form="questionnaire-step-form"
        variant="primary"
        loading={isSubmitting}
      >
        {isLastStep ? 'Complete' : 'Next'}
      </Button>
    </div>
  );
};

export default StepNavigation;
