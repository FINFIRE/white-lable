import React, { useEffect, useState } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useQuery, useMutation } from '@tanstack/react-query';
import axios from 'axios';
import { getDocumentsPrepared, postDocumentsPrepared } from '../../../api/connections';
import { DOCUMENT_STATUS_OPTIONS } from '../../../constants/options';
import SelectDropdown from '../../ui/SelectDropdown';
import LoadingSpinner from '../../ui/LoadingSpinner';
import type { DocumentsDetailData } from '../../../types/api';

interface Props {
  onComplete: () => void;
}

const FORM_ID = 'questionnaire-step-form';

const FIELDS: { key: keyof DocumentsDetailData; label: string }[] = [
  { key: 'onePageTearSheet', label: 'One Page Tear Sheet' },
  { key: 'elevatorPitch', label: 'Elevator Pitch' },
  { key: 'businessPlan', label: 'Business Plan' },
  { key: 'corporateIdentityDueDiligence', label: 'Corporate Identity Due Diligence' },
  { key: 'technologyDueDiligence', label: 'Technology Due Diligence' },
  { key: 'executiveSummary', label: 'Executive Summary' },
  { key: 'virtualPortal', label: 'Virtual Portal' },
];

const statusOptions = DOCUMENT_STATUS_OPTIONS.map((o) => o.label);

const StepDocumentDetails: React.FC<Props> = ({ onComplete }) => {
  const [infoMessage, setInfoMessage] = useState('');

  const { data, isLoading } = useQuery({
    queryKey: ['documentsPrepared'],
    queryFn: getDocumentsPrepared,
    retry: false,
  });

  const mutation = useMutation({ mutationFn: postDocumentsPrepared });

  const defaults: DocumentsDetailData = {
    onePageTearSheet: '',
    elevatorPitch: '',
    businessPlan: '',
    corporateIdentityDueDiligence: '',
    technologyDueDiligence: '',
    executiveSummary: '',
    virtualPortal: '',
  };

  const { handleSubmit, setValue, control } = useForm<DocumentsDetailData>({
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

  const onSubmit = (formData: DocumentsDetailData) => {
    setInfoMessage('');
    mutation.mutate(formData, {
      onSuccess: () => onComplete(),
      onError: (err) => {
        if (axios.isAxiosError(err) && err.response?.status === 409) {
          setInfoMessage('Document details already saved.');
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

export default StepDocumentDetails;
