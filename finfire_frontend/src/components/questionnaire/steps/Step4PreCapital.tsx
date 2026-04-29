import React, { useEffect, useState } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useQuery, useMutation } from '@tanstack/react-query';
import axios from 'axios';
import { getPreCapital, postPreCapital } from '../../../api/questionnaire';
import { PRE_CAPITAL_OPTIONS } from '../../../constants/options';
import RadioGroup from '../../ui/RadioGroup';
import LoadingSpinner from '../../ui/LoadingSpinner';
import type { PreCapitalData } from '../../../types/api';

interface Step4PreCapitalProps {
  onComplete: () => void;
}

const FORM_ID = 'questionnaire-step-form';

const Step4PreCapital: React.FC<Step4PreCapitalProps> = ({ onComplete }) => {
  const [infoMessage, setInfoMessage] = useState('');

  const { data, isLoading } = useQuery({
    queryKey: ['preCapital'],
    queryFn: getPreCapital,
    retry: false,
  });

  const mutation = useMutation({ mutationFn: postPreCapital });

  const { handleSubmit, setValue, control } = useForm<PreCapitalData>({
    defaultValues: { preCapitalRaise: '' },
  });

  useEffect(() => {
    if (data) {
      const d = Array.isArray(data) ? data[0] : data;
      if (d?.preCapitalRaise) setValue('preCapitalRaise', d.preCapitalRaise);
    }
  }, [data, setValue]);

  const onSubmit = (formData: PreCapitalData) => {
    setInfoMessage('');
    mutation.mutate(formData, {
      onSuccess: () => onComplete(),
      onError: (err) => {
        if (axios.isAxiosError(err) && err.response?.status === 409) {
          setInfoMessage('Pre-capital data already saved.');
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
    <form id={FORM_ID} onSubmit={handleSubmit(onSubmit)} className="space-y-5">
      {infoMessage && (
        <div className="rounded-lg bg-blue-50 border border-blue-200 px-4 py-3 text-sm text-blue-700">
          {infoMessage}
        </div>
      )}

      <Controller
        name="preCapitalRaise"
        control={control}
        rules={{ required: 'Please select a pre-capital range' }}
        render={({ field, fieldState }) => (
          <div>
            <RadioGroup
              name="preCapitalRaise"
              label="How much capital have you previously raised?"
              options={[...PRE_CAPITAL_OPTIONS]}
              value={field.value}
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

export default Step4PreCapital;
