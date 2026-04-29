import { useState } from 'react';
import { useMutation } from '@tanstack/react-query';
import { postAccount } from '../../api/connections';
import { useQuestionnaireStore, type AccountType } from '../../stores/questionnaireStore';
import {
  ACCOUNT_TYPE_OPTIONS,
  PRIMARY_PURPOSE_OPTIONS,
} from '../../constants/options';
import Button from '../ui/Button';

const AccountTypeStep: React.FC = () => {
  const setAccountType = useQuestionnaireStore((s) => s.setAccountType);
  const [selectedType, setSelectedType] = useState<string>('');
  const [selectedPurposes, setSelectedPurposes] = useState<string[]>([]);
  const [error, setError] = useState<string | null>(null);

  const mutation = useMutation({
    mutationFn: postAccount,
    onSuccess: () => {
      setAccountType(selectedType as AccountType);
    },
    onError: (err: unknown) => {
      // 409 means account already exists — treat as success
      if (
        err &&
        typeof err === 'object' &&
        'response' in err &&
        (err as { response?: { status?: number } }).response?.status === 409
      ) {
        setAccountType(selectedType as AccountType);
        return;
      }
      setError('Failed to save account setup. Please try again.');
    },
  });

  const handlePurposeToggle = (purpose: string) => {
    setSelectedPurposes((prev) =>
      prev.includes(purpose)
        ? prev.filter((p) => p !== purpose)
        : [...prev, purpose]
    );
  };

  const handleSubmit = () => {
    if (!selectedType) {
      setError('Please select an account type.');
      return;
    }
    setError(null);
    mutation.mutate({ accountType: selectedType, primaryAppUse: selectedPurposes });
  };

  return (
    <div className="mx-auto max-w-3xl py-12 px-4">
      <div className="mb-8 text-center">
        <h2 className="text-2xl font-bold text-text-primary">
          Account Setup
        </h2>
        <p className="mt-1 text-sm text-text-secondary">
          Select your account type to get started
        </p>
      </div>

      {error && (
        <div className="mb-4 rounded-lg border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
          {error}
        </div>
      )}

      {/* Account Type Cards */}
      <div className="mb-8 grid grid-cols-1 gap-4 sm:grid-cols-3">
        {ACCOUNT_TYPE_OPTIONS.map((type) => (
          <button
            key={type}
            type="button"
            onClick={() => setSelectedType(type)}
            className={`rounded-xl border-2 p-6 text-left transition ${
              selectedType === type
                ? 'border-primary-500 bg-primary-50 shadow-md'
                : 'border-border bg-white hover:border-primary-300'
            }`}
          >
            <h3 className="font-semibold text-text-primary">{type}</h3>
            <p className="mt-1 text-xs text-text-secondary">
              {type === 'Enterprise/Business'
                ? 'Seeking capital for your business'
                : type === 'Intermediary'
                  ? 'Consultant or intermediary providing advice'
                  : 'Capital market representative'}
            </p>
          </button>
        ))}
      </div>

      {/* Primary Purpose */}
      <div className="mb-8">
        <h3 className="mb-3 text-sm font-medium text-text-primary">
          Primary Purpose (select all that apply)
        </h3>
        <div className="space-y-2">
          {PRIMARY_PURPOSE_OPTIONS.map((purpose) => (
            <label
              key={purpose}
              className="flex items-start gap-3 rounded-lg border border-border p-3 hover:bg-surface cursor-pointer"
            >
              <input
                type="checkbox"
                checked={selectedPurposes.includes(purpose)}
                onChange={() => handlePurposeToggle(purpose)}
                className="mt-0.5 h-4 w-4 rounded border-border text-primary-500 focus:ring-primary-200"
              />
              <span className="text-sm text-text-primary">{purpose}</span>
            </label>
          ))}
        </div>
      </div>

      <Button
        onClick={handleSubmit}
        loading={mutation.isPending}
        className="w-full"
      >
        Continue
      </Button>
    </div>
  );
};

export default AccountTypeStep;
