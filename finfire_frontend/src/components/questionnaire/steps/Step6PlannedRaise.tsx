import React, { useEffect, useState } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useQuery, useMutation } from '@tanstack/react-query';
import axios from 'axios';
import { getPlannedRaise, postPlannedRaise } from '../../../api/questionnaire';
import { PLANNED_RAISE_OPTIONS } from '../../../constants/options';
import RadioGroup from '../../ui/RadioGroup';
import LoadingSpinner from '../../ui/LoadingSpinner';
import type { PlannedRaiseData } from '../../../types/api';

interface Step6PlannedRaiseProps {
  onComplete: () => void;
}

const FORM_ID = 'questionnaire-step-form';

const Step6PlannedRaise: React.FC<Step6PlannedRaiseProps> = ({ onComplete }) => {
  const [infoMessage, setInfoMessage] = useState('');

  const { data, isLoading } = useQuery({
    queryKey: ['plannedRaise'],
    queryFn: getPlannedRaise,
    retry: false,
  });

  const mutation = useMutation({ mutationFn: postPlannedRaise });

  const { handleSubmit, setValue, control } = useForm<PlannedRaiseData>({
    defaultValues: { plannedRaise: '' },
  });

  useEffect(() => {
    if (data) {
      const d = Array.isArray(data) ? data[0] : data;
      if (d?.plannedRaise) setValue('plannedRaise', d.plannedRaise);
    }
  }, [data, setValue]);

  const onSubmit = (formData: PlannedRaiseData) => {
    setInfoMessage('');
    mutation.mutate(formData, {
      onSuccess: () => onComplete(),
      onError: (err) => {
        if (axios.isAxiosError(err) && err.response?.status === 409) {
          setInfoMessage('Planned raise data already saved.');
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
        name="plannedRaise"
        control={control}
        rules={{ required: 'Please select a planned raise amount' }}
        render={({ field, fieldState }) => (
          <div>
            <RadioGroup
              name="plannedRaise"
              label="How much do you plan to raise?"
              options={[...PLANNED_RAISE_OPTIONS]}
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

export default Step6PlannedRaise;
