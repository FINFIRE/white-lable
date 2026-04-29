import React, { useEffect } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useQuery, useMutation } from '@tanstack/react-query';
import { getRounds, postRounds } from '../../../api/questionnaire';
import { ROUNDS_OPTIONS, ROUNDS_COUNT_OPTIONS } from '../../../constants/options';
import CheckboxGroup from '../../ui/CheckboxGroup';
import RadioGroup from '../../ui/RadioGroup';
import LoadingSpinner from '../../ui/LoadingSpinner';
import type { RoundsData } from '../../../types/api';
import axios from 'axios';

interface Step7Props {
  onComplete: () => void;
}

const Step7Rounds: React.FC<Step7Props> = ({ onComplete }) => {
  const { control, handleSubmit, reset } = useForm<RoundsData>({
    defaultValues: {
      currentRounds: [],
      howManyRounds: '',
    },
  });

  const { data: existing, isLoading } = useQuery({
    queryKey: ['rounds'],
    queryFn: getRounds,
    retry: false,
  });

  useEffect(() => {
    if (existing) {
      reset({
        currentRounds: existing.currentRounds ?? [],
        howManyRounds: existing.howManyRounds ?? '',
      });
    }
  }, [existing, reset]);

  const mutation = useMutation({
    mutationFn: postRounds,
    onSuccess: () => onComplete(),
    onError: (error: unknown) => {
      if (axios.isAxiosError(error) && error.response?.status === 409) {
        onComplete();
      }
    },
  });

  const onSubmit = (data: RoundsData) => {
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
        name="currentRounds"
        control={control}
        rules={{ validate: (v) => v.length > 0 || 'Select at least one round' }}
        render={({ field, fieldState }) => (
          <div>
            <CheckboxGroup
              name="currentRounds"
              label="Which rounds of capital are you currently in or pursuing?"
              options={[...ROUNDS_OPTIONS]}
              values={field.value}
              onChange={field.onChange}
            />
            {fieldState.error && (
              <p className="mt-1 text-sm text-red-600">{fieldState.error.message}</p>
            )}
          </div>
        )}
      />

      <Controller
        name="howManyRounds"
        control={control}
        rules={{ required: 'Please select the number of rounds' }}
        render={({ field, fieldState }) => (
          <div>
            <RadioGroup
              name="howManyRounds"
              label="How many rounds of capital do you plan to raise?"
              options={[...ROUNDS_COUNT_OPTIONS]}
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

export default Step7Rounds;
