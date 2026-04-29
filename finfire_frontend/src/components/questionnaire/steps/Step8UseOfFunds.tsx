import React, { useEffect } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useQuery, useMutation } from '@tanstack/react-query';
import { getUseOfFunds, postUseOfFunds } from '../../../api/questionnaire';
import { USE_OF_FUNDS_OPTIONS } from '../../../constants/options';
import CheckboxGroup from '../../ui/CheckboxGroup';
import LoadingSpinner from '../../ui/LoadingSpinner';
import type { UseOfFundsData } from '../../../types/api';
import axios from 'axios';

interface Step8Props {
  onComplete: () => void;
}

const Step8UseOfFunds: React.FC<Step8Props> = ({ onComplete }) => {
  const { control, handleSubmit, reset } = useForm<UseOfFundsData>({
    defaultValues: {
      fundsUse: [],
    },
  });

  const { data: existing, isLoading } = useQuery({
    queryKey: ['useOfFunds'],
    queryFn: getUseOfFunds,
    retry: false,
  });

  useEffect(() => {
    if (existing) {
      reset({
        fundsUse: existing.fundsUse ?? [],
      });
    }
  }, [existing, reset]);

  const mutation = useMutation({
    mutationFn: postUseOfFunds,
    onSuccess: () => onComplete(),
    onError: (error: unknown) => {
      if (axios.isAxiosError(error) && error.response?.status === 409) {
        onComplete();
      }
    },
  });

  const onSubmit = (data: UseOfFundsData) => {
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
        name="fundsUse"
        control={control}
        rules={{ validate: (v) => v.length > 0 || 'Select at least one use of funds' }}
        render={({ field, fieldState }) => (
          <div>
            <CheckboxGroup
              name="fundsUse"
              label="What will the funds be used for?"
              options={[...USE_OF_FUNDS_OPTIONS]}
              values={field.value}
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

export default Step8UseOfFunds;
