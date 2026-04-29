import React, { useEffect, useState } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useQuery, useMutation } from '@tanstack/react-query';
import axios from 'axios';
import { getPeopleCulture, postPeopleCulture } from '../../../api/connections';
import { DOCUMENT_STATUS_OPTIONS } from '../../../constants/options';
import SelectDropdown from '../../ui/SelectDropdown';
import LoadingSpinner from '../../ui/LoadingSpinner';
import type { PeopleCultureData } from '../../../types/api';

interface Props {
  onComplete: () => void;
}

const FORM_ID = 'questionnaire-step-form';

const FIELDS: { key: keyof PeopleCultureData; label: string }[] = [
  { key: 'leadership', label: 'Leadership' },
  { key: 'managementExperience', label: 'Management Experience' },
  { key: 'consultantsAdvisors', label: 'Consultants & Advisors' },
  { key: 'staff', label: 'Staff' },
  { key: 'culture', label: 'Culture' },
];

const statusOptions = DOCUMENT_STATUS_OPTIONS.map((o) => o.label);

const StepPeopleCulture: React.FC<Props> = ({ onComplete }) => {
  const [infoMessage, setInfoMessage] = useState('');

  const { data, isLoading } = useQuery({
    queryKey: ['peopleCulture'],
    queryFn: getPeopleCulture,
    retry: false,
  });

  const mutation = useMutation({ mutationFn: postPeopleCulture });

  const defaults: PeopleCultureData = {
    leadership: '',
    managementExperience: '',
    consultantsAdvisors: '',
    staff: '',
    culture: '',
  };

  const { handleSubmit, setValue, control } = useForm<PeopleCultureData>({
    defaultValues: defaults,
  });

  useEffect(() => {
    if (data) {
      const d = Array.isArray(data) ? data[0] : data;
      if (d) {
        for (const f of FIELDS) {
          if (d[f.key]) setValue(f.key, String(d[f.key]));
        }
      }
    }
  }, [data, setValue]);

  const onSubmit = (formData: PeopleCultureData) => {
    setInfoMessage('');
    mutation.mutate(formData, {
      onSuccess: () => onComplete(),
      onError: (err) => {
        if (axios.isAxiosError(err) && err.response?.status === 409) {
          setInfoMessage('People & Culture data already saved.');
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

      {FIELDS.map((f) => (
        <Controller
          key={f.key}
          name={f.key}
          control={control}
          render={({ field }) => (
            <SelectDropdown
              name={f.key}
              label={f.label}
              options={statusOptions}
              value={field.value}
              onChange={field.onChange}
              placeholder="Select status"
            />
          )}
        />
      ))}
    </form>
  );
};

export default StepPeopleCulture;
