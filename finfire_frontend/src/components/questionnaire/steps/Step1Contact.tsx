import React, { useEffect, useState } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useQuery, useMutation } from '@tanstack/react-query';
import axios from 'axios';
import { getContact, postContact } from '../../../api/questionnaire';
import {
  AFFILIATION_OPTIONS,
  SPECIAL_PROGRAMS_OPTIONS,
} from '../../../constants/options';
import CheckboxGroup from '../../ui/CheckboxGroup';
import LoadingSpinner from '../../ui/LoadingSpinner';
import type { ContactData } from '../../../types/api';

interface Step1ContactProps {
  onComplete: () => void;
}

const FORM_ID = 'questionnaire-step-form';

const Step1Contact: React.FC<Step1ContactProps> = ({ onComplete }) => {
  const [infoMessage, setInfoMessage] = useState('');

  const { data, isLoading } = useQuery({
    queryKey: ['contact'],
    queryFn: getContact,
    retry: false,
  });

  const mutation = useMutation({ mutationFn: postContact });

  const {
    register,
    handleSubmit,
    setValue,
    control,
    formState: { errors },
  } = useForm<ContactData>({
    defaultValues: {
      display_name: '',
      email: '',
      companyWebsite: '',
      primaryBusinessAddress: '',
      businessPhone: '',
      mobilePhone: '',
      companyAffiliation: [],
      specialPrograms: [],
    },
  });

  useEffect(() => {
    if (data) {
      const d = Array.isArray(data) ? data[0] : data;
      if (d) {
        setValue('display_name', d.display_name ?? '');
        setValue('email', d.email ?? '');
        setValue('companyWebsite', d.companyWebsite ?? '');
        setValue('primaryBusinessAddress', d.primaryBusinessAddress ?? '');
        setValue('businessPhone', d.businessPhone ?? '');
        setValue('mobilePhone', d.mobilePhone ?? '');
        setValue('companyAffiliation', d.companyAffiliation ?? []);
        setValue('specialPrograms', d.specialPrograms ?? []);
      }
    }
  }, [data, setValue]);

  const onSubmit = (formData: ContactData) => {
    setInfoMessage('');
    mutation.mutate(formData, {
      onSuccess: () => onComplete(),
      onError: (err) => {
        if (axios.isAxiosError(err) && err.response?.status === 409) {
          setInfoMessage('Contact information already saved.');
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
    <form
      id={FORM_ID}
      onSubmit={handleSubmit(onSubmit)}
      className="space-y-5"
    >
      {infoMessage && (
        <div className="rounded-lg bg-blue-50 border border-blue-200 px-4 py-3 text-sm text-blue-700">
          {infoMessage}
        </div>
      )}

      {/* Display Name */}
      <div className="space-y-1">
        <label htmlFor="display_name" className="block text-sm font-medium text-slate-900">
          Display Name *
        </label>
        <input
          id="display_name"
          type="text"
          {...register('display_name', { required: 'Display name is required' })}
          className="block w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-slate-900 transition-colors focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
          placeholder="Your full name"
        />
        {errors.display_name && (
          <p className="text-xs text-red-500">{errors.display_name.message}</p>
        )}
      </div>

      {/* Email */}
      <div className="space-y-1">
        <label htmlFor="email" className="block text-sm font-medium text-slate-900">
          Email *
        </label>
        <input
          id="email"
          type="email"
          {...register('email', { required: 'Email is required' })}
          className="block w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-slate-900 transition-colors focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
          placeholder="you@example.com"
        />
        {errors.email && (
          <p className="text-xs text-red-500">{errors.email.message}</p>
        )}
      </div>

      {/* Company Website */}
      <div className="space-y-1">
        <label htmlFor="companyWebsite" className="block text-sm font-medium text-slate-900">
          Company Website
        </label>
        <input
          id="companyWebsite"
          type="text"
          {...register('companyWebsite')}
          className="block w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-slate-900 transition-colors focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
          placeholder="https://yourcompany.com"
        />
      </div>

      {/* Primary Business Address */}
      <div className="space-y-1">
        <label htmlFor="primaryBusinessAddress" className="block text-sm font-medium text-slate-900">
          Primary Business Address
        </label>
        <input
          id="primaryBusinessAddress"
          type="text"
          {...register('primaryBusinessAddress')}
          className="block w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-slate-900 transition-colors focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
          placeholder="123 Main St, City, State ZIP"
        />
      </div>

      {/* Business Phone — digits and basic formatting only */}
      <div className="space-y-1">
        <label htmlFor="businessPhone" className="block text-sm font-medium text-slate-900">
          Business Phone
        </label>
        <input
          id="businessPhone"
          type="tel"
          inputMode="tel"
          autoComplete="tel-national"
          {...register('businessPhone', {
            pattern: {
              value: /^[0-9+\-()\s.]*$/,
              message: 'Phone must contain digits only (with optional +, -, (), spaces)',
            },
          })}
          className="block w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-slate-900 transition-colors focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
          placeholder="(555) 123-4567"
        />
        {errors.businessPhone && (
          <p className="text-xs text-red-500">{errors.businessPhone.message}</p>
        )}
      </div>

      {/* Mobile Phone — digits and basic formatting only */}
      <div className="space-y-1">
        <label htmlFor="mobilePhone" className="block text-sm font-medium text-slate-900">
          Mobile Phone
        </label>
        <input
          id="mobilePhone"
          type="tel"
          inputMode="tel"
          autoComplete="tel"
          {...register('mobilePhone', {
            pattern: {
              value: /^[0-9+\-()\s.]*$/,
              message: 'Phone must contain digits only (with optional +, -, (), spaces)',
            },
          })}
          className="block w-full rounded-lg border border-gray-300 bg-white px-4 py-2.5 text-sm text-slate-900 transition-colors focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
          placeholder="(555) 987-6543"
        />
        {errors.mobilePhone && (
          <p className="text-xs text-red-500">{errors.mobilePhone.message}</p>
        )}
      </div>

      {/* Company Affiliation */}
      <Controller
        name="companyAffiliation"
        control={control}
        render={({ field }) => (
          <CheckboxGroup
            name="companyAffiliation"
            label="Company Affiliation"
            options={[...AFFILIATION_OPTIONS]}
            values={field.value ?? []}
            onChange={field.onChange}
          />
        )}
      />

      {/* Special Programs */}
      <Controller
        name="specialPrograms"
        control={control}
        render={({ field }) => (
          <CheckboxGroup
            name="specialPrograms"
            label="Special Programs"
            options={[...SPECIAL_PROGRAMS_OPTIONS]}
            values={field.value ?? []}
            onChange={field.onChange}
          />
        )}
      />
    </form>
  );
};

export default Step1Contact;
