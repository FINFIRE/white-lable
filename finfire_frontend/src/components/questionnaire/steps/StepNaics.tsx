import React, { useEffect, useState } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useQuery, useMutation } from '@tanstack/react-query';
import axios from 'axios';
import { getNaics, postNaics } from '../../../api/connections';
import { NAICS_INDUSTRY_OPTIONS } from '../../../constants/options';
import SelectDropdown from '../../ui/SelectDropdown';
import LoadingSpinner from '../../ui/LoadingSpinner';
import type { NaicsData } from '../../../types/api';

interface Props {
  onComplete: () => void;
}

const FORM_ID = 'questionnaire-step-form';

const StepNaics: React.FC<Props> = ({ onComplete }) => {
  const [infoMessage, setInfoMessage] = useState('');

  const { data, isLoading } = useQuery({
    queryKey: ['naics'],
    queryFn: getNaics,
    retry: false,
  });

  const mutation = useMutation({ mutationFn: postNaics });

  const { handleSubmit, setValue, control } = useForm<NaicsData>({
    defaultValues: { naicsCode: '' },
  });

  useEffect(() => {
    if (data) {
      const d = Array.isArray(data) ? data[0] : data;
      if (d?.naicsCode) setValue('naicsCode', d.naicsCode);
    }
  }, [data, setValue]);

  const onSubmit = (formData: NaicsData) => {
    setInfoMessage('');
    mutation.mutate(formData, {
      onSuccess: () => onComplete(),
      onError: (err) => {
        if (axios.isAxiosError(err) && err.response?.status === 409) {
          setInfoMessage('NAICS data already saved.');
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
        name="naicsCode"
        control={control}
        rules={{ required: 'Please select an industry' }}
        render={({ field, fieldState }) => (
          <div>
            <SelectDropdown
              name="naicsCode"
              label="What industry is your business in?"
              options={[...NAICS_INDUSTRY_OPTIONS]}
              value={field.value}
              onChange={field.onChange}
              placeholder="Select industry"
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

export default StepNaics;
