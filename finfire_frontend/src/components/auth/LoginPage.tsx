import { useState } from 'react';
import { useForm } from 'react-hook-form';
import { Link, useNavigate } from 'react-router-dom';
import Button from '../ui/Button';
import { useAuthStore } from '../../stores/authStore';
import BrandLogo from '../layout/BrandLogo';

interface LoginFormValues {
  username: string;
  password: string;
}

const LoginPage: React.FC = () => {
  const navigate = useNavigate();
  const login = useAuthStore((s) => s.login);
  const [error, setError] = useState<string | null>(null);

  const {
    register,
    handleSubmit,
    formState: { isSubmitting },
  } = useForm<LoginFormValues>();

  const onSubmit = async (data: LoginFormValues) => {
    setError(null);
    try {
      await login(data.username, data.password);
      navigate('/', { replace: true });
    } catch (err: unknown) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError('Invalid username or password. Please try again.');
      }
    }
  };

  return (
    <div className="flex min-h-screen items-center justify-center bg-gradient-to-br from-primary-50 via-white to-primary-100">
      <div className="w-full max-w-md rounded-2xl bg-white p-8 shadow-lg shadow-primary-200/40">
        {/* Branding */}
        <div className="mb-8 flex flex-col items-center text-center">
          <BrandLogo className="h-12 w-auto" />
          <p className="mt-2 text-sm text-text-secondary">
            Sign in to your account
          </p>
        </div>

        {/* Error */}
        {error && (
          <div className="mb-4 rounded-lg border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
            {error}
          </div>
        )}

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
              required
              {...register('username', { required: true })}
              className="block w-full rounded-lg border border-border bg-surface px-3 py-2 text-sm text-text-primary placeholder-text-secondary outline-none transition focus:border-primary-400 focus:ring-2 focus:ring-primary-200"
              placeholder="Enter your username"
            />
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
              autoComplete="current-password"
              required
              {...register('password', { required: true })}
              className="block w-full rounded-lg border border-border bg-surface px-3 py-2 text-sm text-text-primary placeholder-text-secondary outline-none transition focus:border-primary-400 focus:ring-2 focus:ring-primary-200"
              placeholder="Enter your password"
            />
          </div>

          {/* Forgot password */}
          <div className="text-right">
            <Link
              to="/forgot-password"
              className="text-sm font-medium text-primary-500 hover:text-primary-700 hover:underline"
            >
              Forgot password?
            </Link>
          </div>

          {/* Submit */}
          <Button
            type="submit"
            loading={isSubmitting}
            className="w-full"
          >
            Login
          </Button>
        </form>

        {/* Register link */}
        <p className="mt-6 text-center text-sm text-text-secondary">
          Don&apos;t have an account?{' '}
          <Link
            to="/register"
            className="font-medium text-primary-500 hover:text-primary-700 hover:underline"
          >
            Register
          </Link>
        </p>
      </div>
    </div>
  );
};

export default LoginPage;
