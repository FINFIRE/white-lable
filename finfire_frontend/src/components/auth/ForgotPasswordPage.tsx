import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { Link } from 'react-router-dom';
import Button from '../ui/Button';
import * as authApi from '../../api/auth';
import BrandLogo from '../layout/BrandLogo';

const schema = z.object({
  email: z.string().email('Enter a valid email address'),
});

type FormValues = z.infer<typeof schema>;

const ForgotPasswordPage: React.FC = () => {
  const [serverError, setServerError] = useState<string | null>(null);
  const [success, setSuccess] = useState(false);

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<FormValues>({ resolver: zodResolver(schema) });

  const onSubmit = async (data: FormValues) => {
    setServerError(null);
    try {
      await authApi.requestPasswordReset(data.email);
      setSuccess(true);
    } catch {
      setServerError('Something went wrong. Please try again.');
    }
  };

  return (
    <div className="flex min-h-screen items-center justify-center bg-gradient-to-br from-primary-50 via-white to-primary-100">
      <div className="w-full max-w-md rounded-2xl bg-white p-8 shadow-lg shadow-primary-200/40">
        <div className="mb-8 flex flex-col items-center text-center">
          <BrandLogo className="h-12 w-auto" />
          <p className="mt-2 text-sm text-text-secondary">
            Reset your password
          </p>
        </div>

        {success && (
          <div className="mb-4 rounded-lg border border-green-200 bg-green-50 px-4 py-3 text-sm text-green-700">
            If an account with that email exists, a password reset link has been
            sent. Check your inbox.
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
                htmlFor="email"
                className="mb-1 block text-sm font-medium text-text-primary"
              >
                Email
              </label>
              <input
                id="email"
                type="email"
                autoComplete="email"
                {...register('email')}
                className="block w-full rounded-lg border border-border bg-surface px-3 py-2 text-sm text-text-primary placeholder-text-secondary outline-none transition focus:border-primary-400 focus:ring-2 focus:ring-primary-200"
                placeholder="you@example.com"
              />
              {errors.email && (
                <p className="mt-1 text-xs text-red-600">
                  {errors.email.message}
                </p>
              )}
            </div>

            <Button type="submit" loading={isSubmitting} className="w-full">
              Send Reset Link
            </Button>
          </form>
        )}

        <p className="mt-6 text-center text-sm text-text-secondary">
          Remember your password?{' '}
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

export default ForgotPasswordPage;
