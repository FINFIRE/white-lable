import React, { useState } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useMutation } from '@tanstack/react-query';
import axios from 'axios';
import { postIntermediaryQ1 } from '../../../api/connections';
import {
  US_STATES,
  INTERMEDIARY_TYPE_OPTIONS,
  PRE_MARKET_OPTIONS,
  NAICS_INDUSTRY_OPTIONS,
} from '../../../constants/options';
import SelectDropdown from '../../ui/SelectDropdown';
import CheckboxGroup from '../../ui/CheckboxGroup';
import type { IntermediaryQ1Data } from '../../../types/api';

interface Props {
  onComplete: () => void;
}

const FORM_ID = 'questionnaire-step-form';

const StepIntermediaryContact: React.FC<Props> = ({ onComplete }) => {
  const [infoMessage, setInfoMessage] = useState('');

  const mutation = useMutation({ mutationFn: postIntermediaryQ1 });

  const { register, handleSubmit, control } = useForm<IntermediaryQ1Data>({
    defaultValues: {
      First_Name: '',
      Last_Name: '',
      Company_Name: '',
      Primary_Phone: '',
      Secondary_Phone: '',
      Alternate_Phone: '',
      Email: '',
      Adress: '',
      City: '',
      State: '',
      Zip_Code: '',
      I_Type: '',
      Prefered_CM: [],
      Specialized_Industry: [],
      Regions_Served: [],
      Selected_Options: [],
    },
  });

  const onSubmit = (formData: IntermediaryQ1Data) => {
    setInfoMessage('');
    mutation.mutate(formData, {
      onSuccess: () => onComplete(),
      onError: (err) => {
        if (axios.isAxiosError(err) && err.response?.status === 409) {
          setInfoMessage('Intermediary contact already saved.');
          onComplete();
        }
      },
    });
  };

  const inputClass =
    'block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-sm text-slate-900 outline-none transition focus:border-blue-500 focus:ring-2 focus:ring-blue-200';

  return (
    <form id={FORM_ID} onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      {infoMessage && (
        <div className="rounded-lg bg-blue-50 border border-blue-200 px-4 py-3 text-sm text-blue-700">
          {infoMessage}
        </div>
      )}

      <div className="grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium text-slate-900 mb-1">First Name</label>
          <input {...register('First_Name', { required: true })} className={inputClass} />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-900 mb-1">Last Name</label>
          <input {...register('Last_Name', { required: true })} className={inputClass} />
        </div>
      </div>

      <div>
        <label className="block text-sm font-medium text-slate-900 mb-1">Company Name</label>
        <input {...register('Company_Name')} className={inputClass} />
      </div>

      <div className="grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium text-slate-900 mb-1">Primary Phone</label>
          <input {...register('Primary_Phone')} className={inputClass} />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-900 mb-1">Secondary Phone</label>
          <input {...register('Secondary_Phone')} className={inputClass} />
        </div>
      </div>

      <div>
        <label className="block text-sm font-medium text-slate-900 mb-1">Email</label>
        <input type="email" {...register('Email', { required: true })} className={inputClass} />
      </div>

      <div>
        <label className="block text-sm font-medium text-slate-900 mb-1">Address</label>
        <input {...register('Adress')} className={inputClass} />
      </div>

      <div className="grid grid-cols-3 gap-4">
        <div>
          <label className="block text-sm font-medium text-slate-900 mb-1">City</label>
          <input {...register('City')} className={inputClass} />
        </div>
        <Controller
          name="State"
          control={control}
          render={({ field }) => (
            <SelectDropdown
              name="State"
              label="State"
              options={[...US_STATES]}
              value={field.value}
              onChange={field.onChange}
              placeholder="Select state"
            />
          )}
        />
        <div>
          <label className="block text-sm font-medium text-slate-900 mb-1">Zip Code</label>
          <input {...register('Zip_Code')} className={inputClass} />
        </div>
      </div>

      <Controller
        name="I_Type"
        control={control}
        render={({ field }) => (
          <SelectDropdown
            name="I_Type"
            label="Intermediary Type"
            options={[...INTERMEDIARY_TYPE_OPTIONS]}
            value={field.value}
            onChange={field.onChange}
            placeholder="Select type"
          />
        )}
      />

      <Controller
        name="Prefered_CM"
        control={control}
        render={({ field }) => (
          <CheckboxGroup
            name="Prefered_CM"
            label="Preferred Capital Markets"
            options={[...PRE_MARKET_OPTIONS]}
            values={field.value}
            onChange={field.onChange}
          />
        )}
      />

      <Controller
        name="Specialized_Industry"
        control={control}
        render={({ field }) => (
          <CheckboxGroup
            name="Specialized_Industry"
            label="Specialized Industries"
            options={[...NAICS_INDUSTRY_OPTIONS]}
            values={field.value}
            onChange={field.onChange}
          />
        )}
      />

      <Controller
        name="Regions_Served"
        control={control}
        render={({ field }) => (
          <CheckboxGroup
            name="Regions_Served"
            label="Regions Served"
            options={[...US_STATES]}
            values={field.value}
            onChange={field.onChange}
          />
        )}
      />
    </form>
  );
};

export default StepIntermediaryContact;
