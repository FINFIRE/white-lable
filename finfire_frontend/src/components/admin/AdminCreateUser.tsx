import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { useMutation, useQueryClient } from '@tanstack/react-query';
import { createAdminUser } from '../../api/admin';
import { useQuestionnaireStore } from '../../stores/questionnaireStore';
import Button from '../ui/Button';

const schema = z
  .object({
    username: z.string().min(1, 'Username is required'),
    email: z.string().email('Enter a valid email address'),
    password: z.string().min(8, 'Password must be at least 8 characters'),
    confirmPassword: z.string().min(1, 'Please confirm the password'),
  })
  .refine((d) => d.password === d.confirmPassword, {
    message: 'Passwords do not match',
    path: ['confirmPassword'],
  });

type FormValues = z.infer<typeof schema>;

const inputClass =
  'block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-sm text-slate-900 outline-none transition focus:border-blue-500 focus:ring-2 focus:ring-blue-200';

const AdminCreateUser: React.FC = () => {
  const setView = useQuestionnaireStore((s) => s.setView);
  const setAdminEditUserId = useQuestionnaireStore((s) => s.setAdminEditUserId);
  const queryClient = useQueryClient();
  const [serverError, setServerError] = useState<string | null>(null);

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({ resolver: zodResolver(schema) });

  const mutation = useMutation({
    mutationFn: createAdminUser,
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ['adminUsers'] });
      // Navigate to edit the new user's forms
      setAdminEditUserId(data.id);
      setView('adminEditUser');
    },
    onError: (err: unknown) => {
      if (
        err &&
        typeof err === 'object' &&
        'response' in err &&
        (err as { response?: { data?: { error?: string } } }).response?.data?.error
      ) {
        setServerError(
          (err as { response: { data: { error: string } } }).response.data.error
        );
      } else {
        setServerError('Failed to create user. Please try again.');
      }
    },
  });

  const onSubmit = (data: FormValues) => {
    setServerError(null);
    mutation.mutate({
      username: data.username,
      email: data.email,
      password: data.password,
    });
  };

  return (
    <div style={{ maxWidth: 480, margin: '0 auto' }}>
      <div
        style={{
          background: '#fff',
          borderRadius: 20,
          border: '1px solid #E2E8F0',
          padding: 36,
        }}
      >
        {/* Header */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 12, marginBottom: 24 }}>
          <button
            onClick={() => setView('dashboard')}
            style={{
              background: 'none',
              border: '1px solid #E2E8F0',
              borderRadius: 8,
              padding: '6px 12px',
              cursor: 'pointer',
              fontSize: 13,
              color: '#334155',
            }}
          >
            &larr; Back
          </button>
          <div>
            <div style={{ fontSize: 18, fontWeight: 700, color: '#0F172A' }}>
              Create New User
            </div>
            <div style={{ fontSize: 12, color: '#94A3B8' }}>
              User will be active immediately (no email verification needed)
            </div>
          </div>
        </div>

        {serverError && (
          <div className="mb-4 rounded-lg border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
            {serverError}
          </div>
        )}

        <form onSubmit={handleSubmit(onSubmit)} className="space-y-5">
          <div>
            <label className="mb-1 block text-sm font-medium text-text-primary">
              Username
            </label>
            <input
              type="text"
              autoComplete="username"
              {...register('username')}
              className={inputClass}
              placeholder="Enter username"
            />
            {errors.username && (
              <p className="mt-1 text-xs text-red-600">{errors.username.message}</p>
            )}
          </div>

          <div>
            <label className="mb-1 block text-sm font-medium text-text-primary">
              Email
            </label>
            <input
              type="email"
              autoComplete="email"
              {...register('email')}
              className={inputClass}
              placeholder="user@example.com"
            />
            {errors.email && (
              <p className="mt-1 text-xs text-red-600">{errors.email.message}</p>
            )}
          </div>

          <div>
            <label className="mb-1 block text-sm font-medium text-text-primary">
              Password
            </label>
            <input
              type="password"
              autoComplete="new-password"
              {...register('password')}
              className={inputClass}
              placeholder="Min. 8 characters"
            />
            {errors.password && (
              <p className="mt-1 text-xs text-red-600">{errors.password.message}</p>
            )}
          </div>

          <div>
            <label className="mb-1 block text-sm font-medium text-text-primary">
              Confirm Password
            </label>
            <input
              type="password"
              autoComplete="new-password"
              {...register('confirmPassword')}
              className={inputClass}
              placeholder="Re-enter password"
            />
            {errors.confirmPassword && (
              <p className="mt-1 text-xs text-red-600">{errors.confirmPassword.message}</p>
            )}
          </div>

          <Button type="submit" loading={isSubmitting || mutation.isPending} className="w-full">
            Create User & Fill Forms
          </Button>
        </form>
      </div>
    </div>
  );
};

export default AdminCreateUser;
