import React, { useEffect } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useQuery, useMutation } from '@tanstack/react-query';
import { getRisk, postRisk } from '../../../api/questionnaire';
import {
  RISK_TOLERANCE_OPTIONS,
  COST_TOLERANCE_OPTIONS,
} from '../../../constants/options';
import RadioGroup from '../../ui/RadioGroup';
import LoadingSpinner from '../../ui/LoadingSpinner';
import type { RiskData } from '../../../types/api';
import axios from 'axios';

interface Step9Props {
  onComplete: () => void;
}

const Step9RiskAssessment: React.FC<Step9Props> = ({ onComplete }) => {
  const { control, handleSubmit, reset } = useForm<RiskData>({
    defaultValues: {
      riskToleranceInvestor: '',
      riskToleranceFounder: '',
    },
  });

  const { data: existing, isLoading } = useQuery({
    queryKey: ['risk'],
    queryFn: getRisk,
    retry: false,
  });

  useEffect(() => {
    if (existing) {
      reset({
        riskToleranceInvestor: existing.riskToleranceInvestor ?? '',
        riskToleranceFounder: existing.riskToleranceFounder ?? '',
      });
    }
  }, [existing, reset]);

  const mutation = useMutation({
    mutationFn: postRisk,
    onSuccess: () => onComplete(),
    onError: (error: unknown) => {
      if (axios.isAxiosError(error) && error.response?.status === 409) {
        onComplete();
      }
    },
  });

  const onSubmit = (data: RiskData) => {
    mutation.mutate(data);
  };

  if (isLoading) {
    return (
      <div className="flex items-center justify-center py-12">
        <LoadingSpinner size="lg" />
      </div>
    );
  }

  return (
    <form
      id="questionnaire-step-form"
      onSubmit={handleSubmit(onSubmit)}
      className="space-y-8"
    >
      <Controller
        name="riskToleranceInvestor"
        control={control}
        rules={{ required: 'Please select investor risk tolerance' }}
        render={({ field, fieldState }) => (
          <div>
            <RadioGroup
              name="riskToleranceInvestor"
              label="What is the investor's risk tolerance?"
              options={[...RISK_TOLERANCE_OPTIONS]}
              value={field.value}
              onChange={field.onChange}
            />
            {fieldState.error && (
              <p className="mt-1 text-sm text-red-600">{fieldState.error.message}</p>
            )}
          </div>
        )}
      />

      <Controller
        name="riskToleranceFounder"
        control={control}
        rules={{ required: 'Please select cost of capital tolerance' }}
        render={({ field, fieldState }) => (
          <div>
            <RadioGroup
              name="riskToleranceFounder"
              label="What is the founder's tolerance for cost of capital?"
              options={[...COST_TOLERANCE_OPTIONS]}
              value={field.value}
              onChange={field.onChange}
            />
            {fieldState.error && (
              <p className="mt-1 text-sm text-red-600">{fieldState.error.message}</p>
            )}
          </div>
        )}
      />

      {mutation.isError && !axios.isAxiosError(mutation.error) && (
        <p className="text-sm text-red-600">
          Something went wrong. Please try again.
        </p>
      )}
    </form>
  );
};

export default Step9RiskAssessment;
