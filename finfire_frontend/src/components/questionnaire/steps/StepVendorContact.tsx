import React, { useState } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useMutation } from '@tanstack/react-query';
import axios from 'axios';
import { postVendorQ1 } from '../../../api/connections';
import { US_STATES, CM_TYPE_OPTIONS } from '../../../constants/options';
import SelectDropdown from '../../ui/SelectDropdown';
import type { VendorQ1Data } from '../../../types/api';

interface Props {
  onComplete: () => void;
}

const FORM_ID = 'questionnaire-step-form';

const StepVendorContact: React.FC<Props> = ({ onComplete }) => {
  const [infoMessage, setInfoMessage] = useState('');

  const mutation = useMutation({ mutationFn: postVendorQ1 });

  const { register, handleSubmit, control } = useForm<VendorQ1Data>({
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
      CM_Type: '',
    },
  });

  const onSubmit = (formData: VendorQ1Data) => {
    setInfoMessage('');
    mutation.mutate(formData, {
      onSuccess: () => onComplete(),
      onError: (err) => {
        if (axios.isAxiosError(err) && err.response?.status === 409) {
          setInfoMessage('Vendor contact already saved.');
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
        name="CM_Type"
        control={control}
        rules={{ required: 'Please select a capital market type' }}
        render={({ field, fieldState }) => (
          <div>
            <SelectDropdown
              name="CM_Type"
              label="Capital Market Type"
              options={[...CM_TYPE_OPTIONS]}
              value={field.value}
              onChange={field.onChange}
              placeholder="Select type"
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

export default StepVendorContact;
