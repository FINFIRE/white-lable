import React, { useEffect, useState } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useQuery, useMutation } from '@tanstack/react-query';
import axios from 'axios';
import { getFinancials, postFinancials } from '../../../api/connections';
import { DOCUMENT_STATUS_OPTIONS } from '../../../constants/options';
import SelectDropdown from '../../ui/SelectDropdown';
import LoadingSpinner from '../../ui/LoadingSpinner';
import type { FinancialsData } from '../../../types/api';

interface Props {
  onComplete: () => void;
}

const FORM_ID = 'questionnaire-step-form';

const FIELDS: { key: keyof FinancialsData; label: string }[] = [
  { key: 'assumptionsWorksheets', label: 'Assumptions Worksheets' },
  { key: 'capitalSourceStructure', label: 'Capital Source Structure' },
  { key: 'capitalizationTable', label: 'Capitalization Table' },
  { key: 'financialModelingFixedCosts', label: 'Financial Modeling - Fixed Costs' },
  { key: 'financialModelingRevenuesCosts', label: 'Financial Modeling - Revenues & Costs' },
  { key: 'financialModelingSummaryPage', label: 'Financial Modeling - Summary Page' },
  { key: 'sourcesUses', label: 'Sources & Uses' },
  { key: 'valuationSpreadsheets', label: 'Valuation Spreadsheets' },
  { key: 'valuationLetterFinal', label: 'Valuation Letter (Final)' },
];

const statusOptions = DOCUMENT_STATUS_OPTIONS.map((o) => o.label);

const StepFinancials: React.FC<Props> = ({ onComplete }) => {
  const [infoMessage, setInfoMessage] = useState('');

  const { data, isLoading } = useQuery({
    queryKey: ['financials'],
    queryFn: getFinancials,
    retry: false,
  });

  const mutation = useMutation({ mutationFn: postFinancials });

  const defaults: FinancialsData = {
    assumptionsWorksheets: '',
    capitalSourceStructure: '',
    capitalizationTable: '',
    financialModelingFixedCosts: '',
    financialModelingRevenuesCosts: '',
    financialModelingSummaryPage: '',
    sourcesUses: '',
    valuationSpreadsheets: '',
    valuationLetterFinal: '',
  };

  const { handleSubmit, setValue, control } = useForm<FinancialsData>({
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

  const onSubmit = (formData: FinancialsData) => {
    setInfoMessage('');
    mutation.mutate(formData, {
      onSuccess: () => onComplete(),
      onError: (err) => {
        if (axios.isAxiosError(err) && err.response?.status === 409) {
          setInfoMessage('Financials data already saved.');
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

export default StepFinancials;
