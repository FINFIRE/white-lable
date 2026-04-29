import React, { useState } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useMutation } from '@tanstack/react-query';
import axios from 'axios';
import { postIntermediaryQ2 } from '../../../api/connections';
import { INTERMEDIARY_PRICING_TYPE_OPTIONS } from '../../../constants/options';
import SelectDropdown from '../../ui/SelectDropdown';
import type { IntermediaryQ2Data } from '../../../types/api';

interface Props {
  onComplete: () => void;
}

const FORM_ID = 'questionnaire-step-form';

const StepIntermediaryPricing: React.FC<Props> = ({ onComplete }) => {
  const [infoMessage, setInfoMessage] = useState('');

  const mutation = useMutation({ mutationFn: postIntermediaryQ2 });

  const { register, handleSubmit, control } = useForm<IntermediaryQ2Data>({
    defaultValues: {
      Type: '',
      Explanation: '',
      Rate: '',
    },
  });

  const onSubmit = (formData: IntermediaryQ2Data) => {
    setInfoMessage('');
    mutation.mutate(formData, {
      onSuccess: () => onComplete(),
      onError: (err) => {
        if (axios.isAxiosError(err) && err.response?.status === 409) {
          setInfoMessage('Pricing data already saved.');
          onComplete();
        }
      },
    });
  };

  return (
    <form id={FORM_ID} onSubmit={handleSubmit(onSubmit)} className="space-y-5">
      {infoMessage && (
        <div className="rounded-lg bg-blue-50 border border-blue-200 px-4 py-3 text-sm text-blue-700">
          {infoMessage}
        </div>
      )}

      <Controller
        name="Type"
        control={control}
        rules={{ required: 'Please select a pricing type' }}
        render={({ field, fieldState }) => (
          <div>
            <SelectDropdown
              name="Type"
              label="Pricing Type"
              options={[...INTERMEDIARY_PRICING_TYPE_OPTIONS]}
              value={field.value}
              onChange={field.onChange}
              placeholder="Select pricing type"
            />
            {fieldState.error && (
              <p className="mt-1 text-xs text-red-500">{fieldState.error.message}</p>
            )}
          </div>
        )}
      />

      <div>
        <label className="block text-sm font-medium text-slate-900 mb-1">
          Explanation
        </label>
        <textarea
          {...register('Explanation')}
          rows={4}
          className="block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-sm text-slate-900 outline-none transition focus:border-blue-500 focus:ring-2 focus:ring-blue-200"
          placeholder="Describe your pricing structure..."
        />
      </div>

      <div>
        <label className="block text-sm font-medium text-slate-900 mb-1">
          Rate
        </label>
        <input
          {...register('Rate', { required: 'Rate is required' })}
          className="block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-sm text-slate-900 outline-none transition focus:border-blue-500 focus:ring-2 focus:ring-blue-200"
          placeholder="e.g. $150/hr, 5%, etc."
        />
      </div>
    </form>
  );
};

export default StepIntermediaryPricing;
