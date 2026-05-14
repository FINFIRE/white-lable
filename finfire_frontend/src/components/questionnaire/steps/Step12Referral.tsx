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

/**
 * "Have a referrer" toggle — UI-only, not persisted to the backend.
 * When set to "None", we hide the two free-text fields and submit the
 * sentinel string "None" for both `referrerName` and `referralOther`.
 */
const HAS_REFERRER_YES = 'I have a referrer';
const HAS_REFERRER_NONE = 'None';
const NONE_SENTINEL = 'None';

type FormValues = ReferralData & { hasReferrer: string };

const Step12Referral: React.FC<Step12Props> = ({ onComplete }) => {
  const { control, handleSubmit, reset, watch, setValue } =
    useForm<FormValues>({
      defaultValues: {
        referralSource: '',
        referrerName: '',
        referralOther: '',
        hasReferrer: HAS_REFERRER_YES,
      },
    });

  const hasReferrer = watch('hasReferrer');
  const showDetails = hasReferrer === HAS_REFERRER_YES;

  const { data: existing, isLoading } = useQuery({
    queryKey: ['referral'],
    queryFn: getReferral,
    retry: false,
  });

  useEffect(() => {
    if (existing) {
      const name = existing.referrerName ?? '';
      const other = existing.referralOther ?? '';
      const restoredHasReferrer =
        name === NONE_SENTINEL && other === NONE_SENTINEL
          ? HAS_REFERRER_NONE
          : HAS_REFERRER_YES;
      reset({
        referralSource: existing.referralSource ?? '',
        // Don't show "None" in the input when we know it's the sentinel.
        referrerName: restoredHasReferrer === HAS_REFERRER_NONE ? '' : name,
        referralOther: restoredHasReferrer === HAS_REFERRER_NONE ? '' : other,
        hasReferrer: restoredHasReferrer,
      });
    }
  }, [existing, reset]);

  // Clear the free-text fields when the user flips to "None" so any
  // previously typed value isn't sent on submit.
  useEffect(() => {
    if (hasReferrer === HAS_REFERRER_NONE) {
      setValue('referrerName', '');
      setValue('referralOther', '');
    }
  }, [hasReferrer, setValue]);

  const mutation = useMutation({
    mutationFn: postReferral,
    onSuccess: () => onComplete(),
    onError: (error: unknown) => {
      if (axios.isAxiosError(error) && error.response?.status === 409) {
        onComplete();
      }
    },
  });

  const onSubmit = (data: FormValues) => {
    const payload: ReferralData = {
      referralSource: data.referralSource,
      referrerName:
        data.hasReferrer === HAS_REFERRER_NONE ? NONE_SENTINEL : data.referrerName,
      referralOther:
        data.hasReferrer === HAS_REFERRER_NONE ? NONE_SENTINEL : data.referralOther,
    };
    mutation.mutate(payload);
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

      {/* "None" toggle — skips the referrer name + additional details fields */}
      <Controller
        name="hasReferrer"
        control={control}
        render={({ field }) => (
          <RadioGroup
            name="hasReferrer"
            label="Referrer details"
            options={[HAS_REFERRER_YES, HAS_REFERRER_NONE]}
            value={field.value}
            onChange={field.onChange}
          />
        )}
      />

      {showDetails && (
        <Controller
          name="referrerName"
          control={control}
          rules={{
            validate: (value, formValues) =>
              formValues.hasReferrer === HAS_REFERRER_NONE ||
              (value && value.trim().length > 0) ||
              'Please enter a referrer name',
          }}
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
      )}

      {showDetails && (
        <Controller
          name="referralOther"
          control={control}
          rules={{
            validate: (value, formValues) =>
              formValues.hasReferrer === HAS_REFERRER_NONE ||
              (value && value.trim().length > 0) ||
              'Please provide additional details',
          }}
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
      )}

      {mutation.isError && !axios.isAxiosError(mutation.error) && (
        <p className="text-sm text-red-600">
          Something went wrong. Please try again.
        </p>
      )}
    </form>
  );
};

export default Step12Referral;
