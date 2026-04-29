import React, { useEffect, useState } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useQuery, useMutation } from '@tanstack/react-query';
import axios from 'axios';
import { getLending, postLending } from '../../../api/connections';
import {
  COLLATERAL_OPTIONS,
  CREDIT_SCORE_OPTIONS,
  CRIMINAL_HISTORY_OPTIONS,
} from '../../../constants/options';
import RadioGroup from '../../ui/RadioGroup';
import LoadingSpinner from '../../ui/LoadingSpinner';
import type { LendingData } from '../../../types/api';

interface Props {
  onComplete: () => void;
}

const FORM_ID = 'questionnaire-step-form';

const StepLending: React.FC<Props> = ({ onComplete }) => {
  const [infoMessage, setInfoMessage] = useState('');

  const { data, isLoading } = useQuery({
    queryKey: ['lending'],
    queryFn: getLending,
    retry: false,
  });

  const mutation = useMutation({ mutationFn: postLending });

  const { handleSubmit, setValue, control } = useForm<LendingData>({
    defaultValues: {
      collateralStatus: '',
      creditScore: '',
      criminalHistory: '',
    },
  });

  useEffect(() => {
    if (data) {
      const d = Array.isArray(data) ? data[0] : data;
      if (d?.collateralStatus) setValue('collateralStatus', d.collateralStatus);
      if (d?.creditScore) setValue('creditScore', d.creditScore);
      if (d?.criminalHistory) setValue('criminalHistory', d.criminalHistory);
    }
  }, [data, setValue]);

  const onSubmit = (formData: LendingData) => {
    setInfoMessage('');
    mutation.mutate(formData, {
      onSuccess: () => onComplete(),
      onError: (err) => {
        if (axios.isAxiosError(err) && err.response?.status === 409) {
          setInfoMessage('Lending information already saved.');
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

      <Controller
        name="collateralStatus"
        control={control}
        rules={{ required: 'Please select a collateral option' }}
        render={({ field, fieldState }) => (
          <div>
            <RadioGroup
              name="collateralStatus"
              label="Do you have collateral available?"
              options={[...COLLATERAL_OPTIONS]}
              value={field.value}
              onChange={field.onChange}
            />
            {fieldState.error && (
              <p className="mt-1 text-xs text-red-500">
                {fieldState.error.message}
              </p>
            )}
          </div>
        )}
      />

      <Controller
        name="creditScore"
        control={control}
        rules={{ required: 'Please select your credit score range' }}
        render={({ field, fieldState }) => (
          <div>
            <RadioGroup
              name="creditScore"
              label="What is your credit score?"
              options={[...CREDIT_SCORE_OPTIONS]}
              value={field.value}
              onChange={field.onChange}
            />
            {fieldState.error && (
              <p className="mt-1 text-xs text-red-500">
                {fieldState.error.message}
              </p>
            )}
          </div>
        )}
      />

      <Controller
        name="criminalHistory"
        control={control}
        rules={{ required: 'Please select an option' }}
        render={({ field, fieldState }) => (
          <div>
            <RadioGroup
              name="criminalHistory"
              label="Criminal history (if any)"
              options={[...CRIMINAL_HISTORY_OPTIONS]}
              value={field.value}
              onChange={field.onChange}
            />
            {fieldState.error && (
              <p className="mt-1 text-xs text-red-500">
                {fieldState.error.message}
              </p>
            )}
          </div>
        )}
      />
    </form>
  );
};

export default StepLending;
