import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { Link } from 'react-router-dom';
import Button from '../ui/Button';
import * as authApi from '../../api/auth';

const registerSchema = z
  .object({
    username: z.string().min(1, 'Username is required'),
    email: z.string().email('Enter a valid email address'),
    password: z.string().min(8, 'Password must be at least 8 characters'),
    confirmPassword: z.string().min(1, 'Please confirm your password'),
  })
  .refine((data) => data.password === data.confirmPassword, {
    message: 'Passwords do not match',
    path: ['confirmPassword'],
  });

type RegisterFormValues = z.infer<typeof registerSchema>;

const RegisterPage: React.FC = () => {
  const [serverError, setServerError] = useState<string | null>(null);
  const [success, setSuccess] = useState(false);

  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<RegisterFormValues>({
    resolver: zodResolver(registerSchema),
  });

  const onSubmit = async (data: RegisterFormValues) => {
    setServerError(null);
    try {
      await authApi.register(data.username, data.email, data.password);
      setSuccess(true);
    } catch (err: unknown) {
      if (
        err &&
        typeof err === 'object' &&
        'response' in err &&
        (err as { response?: { data?: Record<string, string[]> } }).response?.data
      ) {
        const responseData = (err as { response: { data: Record<string, string[]> } })
          .response.data;
        const messages = Object.values(responseData).flat().join(' ');
        setServerError(messages || 'Registration failed. Please try again.');
      } else {
        setServerError('Registration failed. Please try again.');
      }
    }
  };

  return (
    <div className="flex min-h-screen items-center justify-center bg-gradient-to-br from-primary-50 via-white to-primary-100">
      <div className="w-full max-w-md rounded-2xl bg-white p-8 shadow-lg shadow-primary-200/40">
        {/* Branding */}
        <div className="mb-8 flex flex-col items-center text-center">
          <img src="/logo.png" alt="FINFIRE" className="h-12 w-auto" />
          <p className="mt-2 text-sm text-text-secondary">
            Create your account
          </p>
        </div>

        {/* Success message */}
        {success && (
          <div className="mb-4 rounded-lg border border-green-200 bg-green-50 px-4 py-3 text-sm text-green-700">
            Check your email to activate your account.
          </div>
        )}

        {/* Server error */}
        {serverError && (
          <div className="mb-4 rounded-lg border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
            {serverError}
          </div>
        )}

        {!success && (
          <form onSubmit={handleSubmit(onSubmit)} className="space-y-5">
            {/* Username */}
            <div>
              <label
                htmlFor="username"
                className="mb-1 block text-sm font-medium text-text-primary"
              >
                Username
              </label>
              <input
                id="username"
                type="text"
                autoComplete="username"
                {...register('username')}
                className="block w-full rounded-lg border border-border bg-surface px-3 py-2 text-sm text-text-primary placeholder-text-secondary outline-none transition focus:border-primary-400 focus:ring-2 focus:ring-primary-200"
                placeholder="Choose a username"
              />
              {errors.username && (
                <p className="mt-1 text-xs text-red-600">
                  {errors.username.message}
                </p>
              )}
            </div>

            {/* Email */}
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

            {/* Password */}
            <div>
              <label
                htmlFor="password"
                className="mb-1 block text-sm font-medium text-text-primary"
              >
                Password
              </label>
              <input
                id="password"
                type="password"
                autoComplete="new-password"
                {...register('password')}
                className="block w-full rounded-lg border border-border bg-surface px-3 py-2 text-sm text-text-primary placeholder-text-secondary outline-none transition focus:border-primary-400 focus:ring-2 focus:ring-primary-200"
                placeholder="Min. 8 characters"
              />
              {errors.password && (
                <p className="mt-1 text-xs text-red-600">
                  {errors.password.message}
                </p>
              )}
            </div>

            {/* Confirm Password */}
            <div>
              <label
                htmlFor="confirmPassword"
                className="mb-1 block text-sm font-medium text-text-primary"
              >
                Confirm Password
              </label>
              <input
                id="confirmPassword"
                type="password"
                autoComplete="new-password"
                {...register('confirmPassword')}
                className="block w-full rounded-lg border border-border bg-surface px-3 py-2 text-sm text-text-primary placeholder-text-secondary outline-none transition focus:border-primary-400 focus:ring-2 focus:ring-primary-200"
                placeholder="Re-enter your password"
              />
              {errors.confirmPassword && (
                <p className="mt-1 text-xs text-red-600">
                  {errors.confirmPassword.message}
                </p>
              )}
            </div>

            {/* Submit */}
            <Button
              type="submit"
              loading={isSubmitting}
              className="w-full"
            >
              Register
            </Button>
          </form>
        )}

        {/* Login link */}
        <p className="mt-6 text-center text-sm text-text-secondary">
          Already have an account?{' '}
          <Link
            to="/login"
            className="font-medium text-primary-500 hover:text-primary-700 hover:underline"
          >
            Login
          </Link>
        </p>
      </div>
    </div>
  );
};

export default RegisterPage;
