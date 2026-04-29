import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { Link, useParams } from 'react-router-dom';
import Button from '../ui/Button';
import * as authApi from '../../api/auth';

const schema = z
  .object({
    new_password: z.string().min(8, 'Password must be at least 8 characters'),
    re_new_password: z.string().min(1, 'Please confirm your password'),
  })
  .refine((d) => d.new_password === d.re_new_password, {
    message: 'Passwords do not match',
    path: ['re_new_password'],
  });

type FormValues = z.infer<typeof schema>;

const ResetPasswordConfirmPage: React.FC = () => {
  const { uid, token } = useParams<{ uid: string; token: string }>();
  const [serverError, setServerError] = useState<string | null>(null);
  const [success, setSuccess] = useState(false);

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({ resolver: zodResolver(schema) });

  const onSubmit = async (data: FormValues) => {
    if (!uid || !token) {
      setServerError('Invalid reset link.');
      return;
    }
    setServerError(null);
    try {
      await authApi.confirmPasswordReset({
        uid,
        token,
        new_password: data.new_password,
        re_new_password: data.re_new_password,
      });
      setSuccess(true);
    } catch (err: unknown) {
      if (
        err &&
        typeof err === 'object' &&
        'response' in err &&
        (err as { response?: { data?: Record<string, string[]> } }).response
          ?.data
      ) {
        const responseData = (
          err as { response: { data: Record<string, string[]> } }
        ).response.data;
        const messages = Object.values(responseData).flat().join(' ');
        setServerError(messages || 'Password reset failed. Please try again.');
      } else {
        setServerError('Password reset failed. Please try again.');
      }
    }
  };

  return (
    <div className="flex min-h-screen items-center justify-center bg-gradient-to-br from-primary-50 via-white to-primary-100">
      <div className="w-full max-w-md rounded-2xl bg-white p-8 shadow-lg shadow-primary-200/40">
        <div className="mb-8 flex flex-col items-center text-center">
          <img src="/logo.png" alt="FINFIRE" className="h-12 w-auto" />
          <p className="mt-2 text-sm text-text-secondary">
            Set your new password
          </p>
        </div>

        {success && (
          <div className="mb-4 rounded-lg border border-green-200 bg-green-50 px-4 py-3 text-sm text-green-700">
            Password reset successful! You can now log in with your new
            password.
          </div>
        )}

        {serverError && (
          <div className="mb-4 rounded-lg border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
            {serverError}
          </div>
        )}

        {!success && (
          <form onSubmit={handleSubmit(onSubmit)} className="space-y-5">
            <div>
              <label
                htmlFor="new_password"
                className="mb-1 block text-sm font-medium text-text-primary"
              >
                New Password
              </label>
              <input
                id="new_password"
                type="password"
                autoComplete="new-password"
                {...register('new_password')}
                className="block w-full rounded-lg border border-border bg-surface px-3 py-2 text-sm text-text-primary placeholder-text-secondary outline-none transition focus:border-primary-400 focus:ring-2 focus:ring-primary-200"
                placeholder="Min. 8 characters"
              />
              {errors.new_password && (
                <p className="mt-1 text-xs text-red-600">
                  {errors.new_password.message}
                </p>
              )}
            </div>

            <div>
              <label
                htmlFor="re_new_password"
                className="mb-1 block text-sm font-medium text-text-primary"
              >
                Confirm New Password
              </label>
              <input
                id="re_new_password"
                type="password"
                autoComplete="new-password"
                {...register('re_new_password')}
                className="block w-full rounded-lg border border-border bg-surface px-3 py-2 text-sm text-text-primary placeholder-text-secondary outline-none transition focus:border-primary-400 focus:ring-2 focus:ring-primary-200"
                placeholder="Re-enter your new password"
              />
              {errors.re_new_password && (
                <p className="mt-1 text-xs text-red-600">
                  {errors.re_new_password.message}
                </p>
              )}
            </div>

            <Button type="submit" loading={isSubmitting} className="w-full">
              Reset Password
            </Button>
          </form>
        )}

        <p className="mt-6 text-center text-sm text-text-secondary">
          <Link
            to="/login"
            className="font-medium text-primary-500 hover:text-primary-700 hover:underline"
          >
            Back to Login
          </Link>
        </p>
      </div>
    </div>
  );
};

export default ResetPasswordConfirmPage;
