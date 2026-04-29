import React, { useEffect } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useQuery, useMutation } from '@tanstack/react-query';
import { getDocsPrepared, postDocsPrepared } from '../../../api/questionnaire';
import LoadingSpinner from '../../ui/LoadingSpinner';
import type { DocumentsPreparedData } from '../../../types/api';
import axios from 'axios';
import { Check } from 'lucide-react';

interface Props {
  onComplete: () => void;
}

const DOCUMENT_FIELDS: { key: keyof DocumentsPreparedData; label: string }[] = [
  { key: 'summaryofOffering', label: 'Summary of Offering' },
  { key: 'financialForecast', label: 'Financial Forecast' },
  { key: 'leanBusinessModelCanvas', label: 'Lean Business Model Canvas' },
  { key: 'presentationDeck', label: 'Presentation Deck' },
  { key: 'leadershipOverview', label: 'Leadership Overview' },
  { key: 'exitStrategy', label: 'Exit Strategy' },
  { key: 'offeringDocuments', label: 'Offering Documents' },
  { key: 'aiGeneratedDeepDive', label: 'AI-Generated Deep Dive' },
  { key: 'virtualDataroom', label: 'Virtual Dataroom' },
];

const Step11PreRating: React.FC<Props> = ({ onComplete }) => {
  const defaultValues: DocumentsPreparedData = {
    summaryofOffering: false,
    financialForecast: false,
    leanBusinessModelCanvas: false,
    presentationDeck: false,
    leadershipOverview: false,
    exitStrategy: false,
    offeringDocuments: false,
    aiGeneratedDeepDive: false,
    virtualDataroom: false,
  };

  const { control, handleSubmit, reset } = useForm<DocumentsPreparedData>({
    defaultValues,
  });

  const { data: existing, isLoading } = useQuery({
    queryKey: ['docsPrepared'],
    queryFn: getDocsPrepared,
    retry: false,
  });

  useEffect(() => {
    if (existing) {
      const filled: DocumentsPreparedData = { ...defaultValues };
      for (const f of DOCUMENT_FIELDS) {
        filled[f.key] = !!existing[f.key];
      }
      reset(filled);
    }
  }, [existing, reset]);

  const mutation = useMutation({
    mutationFn: postDocsPrepared,
    onSuccess: () => onComplete(),
    onError: (error: unknown) => {
      if (axios.isAxiosError(error) && error.response?.status === 409) {
        onComplete();
      }
    },
  });

  const onSubmit = (data: DocumentsPreparedData) => {
    mutation.mutate(data);
  };

  if (isLoading) {
    return (
      <div className="flex items-center justify-center py-12">
        <LoadingSpinner />
      </div>
    );
  }

  return (
    <form
      id="questionnaire-step-form"
      onSubmit={handleSubmit(onSubmit)}
      className="space-y-6"
    >
      <fieldset className="space-y-2">
        <legend className="text-sm font-medium text-slate-900 mb-2">
          Which of the following documents have you prepared?
        </legend>
        <div className="grid gap-2">
          {DOCUMENT_FIELDS.map((doc) => (
            <Controller
              key={doc.key}
              name={doc.key}
              control={control}
              render={({ field }) => {
                const isChecked = !!field.value;
                return (
                  <label
                    className={`relative flex cursor-pointer items-center gap-3 rounded-lg border-2 px-4 py-3 text-sm transition-colors ${
                      isChecked
                        ? 'border-blue-500 bg-blue-50 text-slate-900'
                        : 'border-gray-200 bg-white text-slate-700 hover:border-gray-300'
                    }`}
                  >
                    <input
                      type="checkbox"
                      checked={isChecked}
                      onChange={() => field.onChange(!isChecked)}
                      onFocus={(e) => e.target.blur()}
                      tabIndex={-1}
                      className="sr-only"
                    />
                    <span
                      className={`flex h-5 w-5 shrink-0 items-center justify-center rounded border-2 ${
                        isChecked
                          ? 'border-blue-500 bg-blue-500 text-white'
                          : 'border-gray-300 bg-white'
                      }`}
                    >
                      {isChecked && <Check className="h-3.5 w-3.5" />}
                    </span>
                    <span>{doc.label}</span>
                  </label>
                );
              }}
            />
          ))}
        </div>
      </fieldset>

      {mutation.isError && !axios.isAxiosError(mutation.error) && (
        <p className="text-sm text-red-600">
          Something went wrong. Please try again.
        </p>
      )}
    </form>
  );
};

export default Step11PreRating;
