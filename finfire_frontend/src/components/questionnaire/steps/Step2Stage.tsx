import React, { useEffect, useState } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useQuery, useMutation } from '@tanstack/react-query';
import axios from 'axios';
import { getStage, postStage } from '../../../api/questionnaire';
import { STAGE_OPTIONS } from '../../../constants/options';
import RadioGroup from '../../ui/RadioGroup';
import LoadingSpinner from '../../ui/LoadingSpinner';
import type { StageData } from '../../../types/api';

interface Step2StageProps {
  onComplete: () => void;
}

const FORM_ID = 'questionnaire-step-form';

const Step2Stage: React.FC<Step2StageProps> = ({ onComplete }) => {
  const [infoMessage, setInfoMessage] = useState('');

  const { data, isLoading } = useQuery({
    queryKey: ['stage'],
    queryFn: getStage,
    retry: false,
  });

  const mutation = useMutation({ mutationFn: postStage });

  const { handleSubmit, setValue, control } = useForm<StageData>({
    defaultValues: { stageofCompany: '' },
  });

  useEffect(() => {
    if (data) {
      const d = Array.isArray(data) ? data[0] : data;
      if (d?.stageofCompany) setValue('stageofCompany', d.stageofCompany);
    }
  }, [data, setValue]);

  const onSubmit = (formData: StageData) => {
    setInfoMessage('');
    mutation.mutate(formData, {
      onSuccess: () => onComplete(),
      onError: (err) => {
        if (axios.isAxiosError(err) && err.response?.status === 409) {
          setInfoMessage('Stage data already saved.');
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
        name="stageofCompany"
        control={control}
        rules={{ required: 'Please select a stage' }}
        render={({ field, fieldState }) => (
          <div>
            <RadioGroup
              name="stageofCompany"
              label="What stage is your company in?"
              options={[...STAGE_OPTIONS]}
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

export default Step2Stage;
