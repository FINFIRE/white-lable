import React from 'react';
import { Check } from 'lucide-react';

interface CheckboxGroupProps {
  name: string;
  options: string[];
  values: string[];
  onChange: (values: string[]) => void;
  label?: string;
}

const CheckboxGroup: React.FC<CheckboxGroupProps> = ({
  name,
  options,
  values,
  onChange,
  label,
}) => {
  const toggle = (option: string) => {
    if (values.includes(option)) {
      onChange(values.filter((v) => v !== option));
    } else {
      onChange([...values, option]);
    }
  };

  return (
    <fieldset className="space-y-2">
      {label && (
        <legend className="text-sm font-medium text-slate-900 mb-2">
          {label}
        </legend>
      )}
      <div className="grid gap-2">
        {options.map((option) => {
          const isChecked = values.includes(option);
          return (
            <label
              key={option}
              className={`relative flex cursor-pointer items-center gap-3 rounded-lg border-2 px-4 py-3 text-sm transition-colors ${
                isChecked
                  ? 'border-blue-500 bg-blue-50 text-slate-900'
                  : 'border-gray-200 bg-white text-slate-700 hover:border-gray-300'
              }`}
            >
              <input
                type="checkbox"
                name={name}
                value={option}
                checked={isChecked}
                onChange={() => toggle(option)}
                onFocus={(e) => e.target.blur()}
                tabIndex={-1}
                className="sr-only"
              />
              <span
                className={`flex h-5 w-5 shrink-0 items-center justify-center rounded border-2 ${
                  isChecked
                    ? 'border-blue-500 bg-blue-500 text-white'
                    : 'border-gray-300 bg-white'
                }`}
              >
                {isChecked && <Check className="h-3.5 w-3.5" />}
              </span>
              <span>{option}</span>
            </label>
          );
        })}
      </div>
    </fieldset>
  );
};

export default CheckboxGroup;
