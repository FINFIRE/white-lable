import React, { useEffect } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useQuery, useMutation } from '@tanstack/react-query';
import { getReferral, postReferral } from '../../../api/questionnaire';
import { REFERRAL_OPTIONS } from '../../../constants/options';
import RadioGroup from '../../ui/RadioGroup';
import LoadingSpinner from '../../ui/LoadingSpinner';
import type { ReferralData } from '../../../types/api';
import axios from 'axios';

interface Step12Props {
  onComplete: () => void;
}

const Step12Referral: React.FC<Step12Props> = ({ onComplete }) => {
  const { control, handleSubmit, reset } = useForm<ReferralData>({
    defaultValues: {
      referralSource: '',
      referrerName: '',
      referralOther: '',
    },
  });

  const { data: existing, isLoading } = useQuery({
    queryKey: ['referral'],
    queryFn: getReferral,
    retry: false,
  });

  useEffect(() => {
    if (existing) {
      reset({
        referralSource: existing.referralSource ?? '',
        referrerName: existing.referrerName ?? '',
        referralOther: existing.referralOther ?? '',
      });
    }
  }, [existing, reset]);

  const mutation = useMutation({
    mutationFn: postReferral,
    onSuccess: () => onComplete(),
    onError: (error: unknown) => {
      if (axios.isAxiosError(error) && error.response?.status === 409) {
        onComplete();
      }
    },
  });

  const onSubmit = (data: ReferralData) => {
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
      className="space-y-6"
    >
      <Controller
        name="referralSource"
        control={control}
        rules={{ required: 'Please select how you heard about us' }}
        render={({ field, fieldState }) => (
          <div>
            <RadioGroup
              name="referralSource"
              label="How did you hear about FinFire?"
              options={[...REFERRAL_OPTIONS]}
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
        name="referrerName"
        control={control}
        rules={{ required: 'Please enter a referrer name' }}
        render={({ field, fieldState }) => (
          <div className="space-y-1">
            <label
              htmlFor="referrerName"
              className="block text-sm font-medium text-slate-900"
            >
              Referrer Name
            </label>
            <input
              id="referrerName"
              type="text"
              placeholder="Who referred you?"
              className="block w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-slate-900 transition-colors focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
              {...field}
            />
            {fieldState.error && (
              <p className="mt-1 text-sm text-red-600">{fieldState.error.message}</p>
            )}
          </div>
        )}
      />

      <Controller
        name="referralOther"
        control={control}
        rules={{ required: 'Please provide additional details' }}
        render={({ field, fieldState }) => (
          <div className="space-y-1">
            <label
              htmlFor="referralOther"
              className="block text-sm font-medium text-slate-900"
            >
              Additional Details
            </label>
            <input
              id="referralOther"
              type="text"
              placeholder="Tell us more..."
              className="block w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-slate-900 transition-colors focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
              {...field}
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

export default Step12Referral;
