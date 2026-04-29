import React, { useEffect, useState } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useQuery, useMutation } from '@tanstack/react-query';
import axios from 'axios';
import { getAllDocuments, postAllDocuments } from '../../../api/connections';
import LoadingSpinner from '../../ui/LoadingSpinner';
import type { DocumentsPreparedData } from '../../../types/api';

interface Props {
  onComplete: () => void;
}

const FORM_ID = 'questionnaire-step-form';

const FIELDS: { key: keyof DocumentsPreparedData; label: string }[] = [
  { key: 'summaryofOffering', label: 'Summary of Offering' },
  { key: 'financialForecast', label: 'Financial Forecast' },
  { key: 'leanBusinessModelCanvas', label: 'Lean Business Model Canvas' },
  { key: 'presentationDeck', label: 'Presentation Deck' },
  { key: 'leadershipOverview', label: 'Leadership Overview' },
  { key: 'exitStrategy', label: 'Exit Strategy' },
  { key: 'offeringDocuments', label: 'Offering Documents' },
  { key: 'aiGeneratedDeepDive', label: 'AI Generated Deep Dive' },
  { key: 'virtualDataroom', label: 'Virtual Data Room' },
];

const StepAllDocuments: React.FC<Props> = ({ onComplete }) => {
  const [infoMessage, setInfoMessage] = useState('');

  const { data, isLoading } = useQuery({
    queryKey: ['allDocuments'],
    queryFn: getAllDocuments,
    retry: false,
  });

  const mutation = useMutation({ mutationFn: postAllDocuments });

  const { handleSubmit, setValue, control } = useForm<DocumentsPreparedData>({
    defaultValues: {
      summaryofOffering: false,
      financialForecast: false,
      leanBusinessModelCanvas: false,
      presentationDeck: false,
      leadershipOverview: false,
      exitStrategy: false,
      offeringDocuments: false,
      aiGeneratedDeepDive: false,
      virtualDataroom: false,
    },
  });

  useEffect(() => {
    if (data) {
      const d = Array.isArray(data) ? data[0] : data;
      if (d) {
        for (const f of FIELDS) {
          if (d[f.key] !== undefined) setValue(f.key, !!d[f.key]);
        }
      }
    }
  }, [data, setValue]);

  const onSubmit = (formData: DocumentsPreparedData) => {
    setInfoMessage('');
    mutation.mutate(formData, {
      onSuccess: () => onComplete(),
      onError: (err) => {
        if (axios.isAxiosError(err) && err.response?.status === 409) {
          setInfoMessage('Documents data already saved.');
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
    <form id={FORM_ID} onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      {infoMessage && (
        <div className="rounded-lg bg-blue-50 border border-blue-200 px-4 py-3 text-sm text-blue-700">
          {infoMessage}
        </div>
      )}

      <p className="text-sm font-medium text-slate-900 mb-2">
        Which documents have you prepared?
      </p>

      {FIELDS.map((f) => (
        <Controller
          key={f.key}
          name={f.key}
          control={control}
          render={({ field }) => (
            <label className="flex items-center gap-3 rounded-lg border border-gray-200 px-4 py-3 cursor-pointer hover:border-gray-300">
              <input
                type="checkbox"
                checked={!!field.value}
                onChange={(e) => field.onChange(e.target.checked)}
                className="h-4 w-4 rounded border-gray-300 text-blue-500 focus:ring-blue-200"
              />
              <span className="text-sm text-slate-700">{f.label}</span>
            </label>
          )}
        />
      ))}
    </form>
  );
};

export default StepAllDocuments;
