import React from 'react';
import { Loader2 } from 'lucide-react';

type ButtonVariant = 'primary' | 'secondary' | 'danger';

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: ButtonVariant;
  loading?: boolean;
  children: React.ReactNode;
}

const variantClasses: Record<ButtonVariant, string> = {
  primary:
    'bg-blue-500 text-white hover:bg-blue-600 focus:ring-blue-300 disabled:bg-blue-300',
  secondary:
    'bg-white border border-gray-300 text-slate-900 hover:bg-gray-50 focus:ring-blue-200 disabled:text-gray-400',
  danger:
    'bg-red-500 text-white hover:bg-red-600 focus:ring-red-300 disabled:bg-red-300',
};

const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  loading = false,
  disabled,
  className = '',
  children,
  type = 'button',
  ...rest
}) => {
  const isDisabled = disabled || loading;

  return (
    <button
      type={type}
      disabled={isDisabled}
      className={`inline-flex items-center justify-center gap-2 rounded-lg px-4 py-2 text-sm font-medium transition-colors focus:outline-none focus:ring-2 disabled:cursor-not-allowed ${variantClasses[variant]} ${className}`}
      {...rest}
    >
      {loading && <Loader2 className="h-4 w-4 animate-spin" />}
      {children}
    </button>
  );
};

export default Button;
