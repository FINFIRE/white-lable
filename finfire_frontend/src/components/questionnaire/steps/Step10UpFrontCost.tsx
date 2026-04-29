import React, { useEffect } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useQuery, useMutation } from '@tanstack/react-query';
import { getCostTime, postCostTime } from '../../../api/questionnaire';
import { COST_RANGE_OPTIONS, TIMING_OPTIONS } from '../../../constants/options';
import RadioGroup from '../../ui/RadioGroup';
import LoadingSpinner from '../../ui/LoadingSpinner';
import type { CostTimeData } from '../../../types/api';
import axios from 'axios';

interface Step10Props {
  onComplete: () => void;
}

const Step10UpFrontCost: React.FC<Step10Props> = ({ onComplete }) => {
  const { control, handleSubmit, reset } = useForm<CostTimeData>({
    defaultValues: {
      rangeofCost: '',
      timing: '',
    },
  });

  const { data: existing, isLoading } = useQuery({
    queryKey: ['costTime'],
    queryFn: getCostTime,
    retry: false,
  });

  useEffect(() => {
    if (existing) {
      reset({
        rangeofCost: existing.rangeofCost ?? '',
        timing: existing.timing ?? '',
      });
    }
  }, [existing, reset]);

  const mutation = useMutation({
    mutationFn: postCostTime,
    onSuccess: () => onComplete(),
    onError: (error: unknown) => {
      if (axios.isAxiosError(error) && error.response?.status === 409) {
        onComplete();
      }
    },
  });

  const onSubmit = (data: CostTimeData) => {
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
        name="rangeofCost"
        control={control}
        rules={{ required: 'Please select a cost range' }}
        render={({ field, fieldState }) => (
          <div>
            <RadioGroup
              name="rangeofCost"
              label="What is your up-front cost budget range?"
              options={[...COST_RANGE_OPTIONS]}
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
        name="timing"
        control={control}
        rules={{ required: 'Please select a timing preference' }}
        render={({ field, fieldState }) => (
          <div>
            <RadioGroup
              name="timing"
              label="What is your preferred timing for the capital raise?"
              options={[...TIMING_OPTIONS]}
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

export default Step10UpFrontCost;
