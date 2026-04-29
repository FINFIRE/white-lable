import React, { useEffect, useState } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useQuery, useMutation } from '@tanstack/react-query';
import axios from 'axios';
import { getAccountSetup, postAccountSetup } from '../../../api/questionnaire';
import { PRIMARY_PURPOSE_OPTIONS } from '../../../constants/options';
import CheckboxGroup from '../../ui/CheckboxGroup';
import LoadingSpinner from '../../ui/LoadingSpinner';
import type { AccountData } from '../../../types/api';

interface Props {
  onComplete: () => void;
}

const FORM_ID = 'questionnaire-step-form';

const StepAccountSetup: React.FC<Props> = ({ onComplete }) => {
  const [infoMessage, setInfoMessage] = useState('');

  const { data, isLoading } = useQuery({
    queryKey: ['accountSetup'],
    queryFn: getAccountSetup,
    retry: false,
  });

  const mutation = useMutation({ mutationFn: postAccountSetup });

  const { handleSubmit, setValue, control } = useForm<AccountData>({
    defaultValues: {
      accountType: 'Enterprise/Business',
      primaryAppUse: [],
    },
  });

  useEffect(() => {
    if (data) {
      if (data.accountType) setValue('accountType', data.accountType);
      if (Array.isArray(data.primaryAppUse)) setValue('primaryAppUse', data.primaryAppUse);
    }
  }, [data, setValue]);

  const onSubmit = (formData: AccountData) => {
    setInfoMessage('');
    // Always enforce Enterprise/Business
    formData.accountType = 'Enterprise/Business';
    mutation.mutate(formData, {
      onSuccess: () => onComplete(),
      onError: (err) => {
        if (axios.isAxiosError(err) && err.response?.status === 409) {
          setInfoMessage('Account setup already saved.');
          onComplete();
        }
      },
    });
  };

  if (isLoading) {
    return (
      <div className="flex items-center justify-center py-12">
        <LoadingSpinner />
      </div>
    );
  }

  return (
    <form id={FORM_ID} onSubmit={handleSubmit(onSubmit)} className="space-y-6">
      {infoMessage && (
        <div className="rounded-lg bg-blue-50 border border-blue-200 px-4 py-3 text-sm text-blue-700">
          {infoMessage}
        </div>
      )}

      {/* Account Type — fixed to Enterprise */}
      <div>
        <label className="block text-sm font-medium text-slate-900 mb-2">
          Account Type
        </label>
        <div
          className="flex items-center gap-3 rounded-lg border-2 border-blue-500 bg-blue-50 px-4 py-3 text-sm text-slate-900"
        >
          <span
            className="flex h-5 w-5 shrink-0 items-center justify-center rounded-full border-2 border-blue-500 bg-blue-500"
          >
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
              <circle cx="6" cy="6" r="3" fill="#fff" />
            </svg>
          </span>
          <span className="font-medium">Enterprise / Business</span>
        </div>
      </div>

      {/* Primary Purpose — multi-select */}
      <Controller
        name="primaryAppUse"
        control={control}
        rules={{ validate: (v) => v.length > 0 || 'Please select at least one purpose' }}
        render={({ field, fieldState }) => (
          <div>
            <CheckboxGroup
              name="primaryAppUse"
              label="Primary purpose for using FinFire (select all that apply)"
              options={[...PRIMARY_PURPOSE_OPTIONS]}
              values={field.value}
              onChange={field.onChange}
            />
            {fieldState.error && (
              <p className="mt-1 text-xs text-red-500">{fieldState.error.message}</p>
            )}
          </div>
        )}
      />
    </form>
  );
};

export default StepAccountSetup;
