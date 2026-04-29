import React, { useEffect, useState } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useQuery, useMutation } from '@tanstack/react-query';
import axios from 'axios';
import { getEntity, postEntity } from '../../../api/questionnaire';
import { ENTITY_OPTIONS, US_STATES } from '../../../constants/options';
import RadioGroup from '../../ui/RadioGroup';
import SelectDropdown from '../../ui/SelectDropdown';
import LoadingSpinner from '../../ui/LoadingSpinner';
import type { EntityData } from '../../../types/api';

interface Step3EntityProps {
  onComplete: () => void;
}

const FORM_ID = 'questionnaire-step-form';

const Step3Entity: React.FC<Step3EntityProps> = ({ onComplete }) => {
  const [infoMessage, setInfoMessage] = useState('');

  const { data, isLoading } = useQuery({
    queryKey: ['entity'],
    queryFn: getEntity,
    retry: false,
  });

  const mutation = useMutation({ mutationFn: postEntity });

  const {
    register,
    handleSubmit,
    setValue,
    control,
    formState: { errors },
  } = useForm<EntityData>({
    defaultValues: {
      entityType: '',
      entityName: '',
      entityStateofRegistration: '',
    },
  });

  useEffect(() => {
    if (data) {
      const d = Array.isArray(data) ? data[0] : data;
      if (d) {
        if (d.entityType) setValue('entityType', d.entityType);
        if (d.entityName) setValue('entityName', d.entityName);
        if (d.entityStateofRegistration)
          setValue('entityStateofRegistration', d.entityStateofRegistration);
      }
    }
  }, [data, setValue]);

  const onSubmit = (formData: EntityData) => {
    setInfoMessage('');
    mutation.mutate(formData, {
      onSuccess: () => onComplete(),
      onError: (err) => {
        if (axios.isAxiosError(err) && err.response?.status === 409) {
          setInfoMessage('Entity data already saved.');
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

      {/* Entity Type */}
      <Controller
        name="entityType"
        control={control}
        rules={{ required: 'Please select an entity type' }}
        render={({ field, fieldState }) => (
          <div>
            <RadioGroup
              name="entityType"
              label="Entity Type"
              options={[...ENTITY_OPTIONS]}
              value={field.value}
              onChange={field.onChange}
            />
            {fieldState.error && (
              <p className="mt-1 text-xs text-red-500">{fieldState.error.message}</p>
            )}
          </div>
        )}
      />

      {/* Entity Name (Business Name) */}
      <div className="space-y-1">
        <label htmlFor="entityName" className="block text-sm font-medium text-slate-900">
          Business Name
        </label>
        <input
          id="entityName"
          type="text"
          {...register('entityName')}
          className="block w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-slate-900 transition-colors focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
          placeholder="Your business name"
        />
        {errors.entityName && (
          <p className="text-xs text-red-500">{errors.entityName.message}</p>
        )}
      </div>

      {/* State of Registration */}
      <Controller
        name="entityStateofRegistration"
        control={control}
        render={({ field }) => (
          <SelectDropdown
            name="entityStateofRegistration"
            label="State of Registration"
            options={[...US_STATES]}
            value={field.value}
            onChange={field.onChange}
            placeholder="Select a state"
          />
        )}
      />
    </form>
  );
};

export default Step3Entity;
