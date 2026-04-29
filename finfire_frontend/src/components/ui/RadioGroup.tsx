import React from 'react';

interface RadioGroupProps {
  name: string;
  options: string[];
  value: string;
  onChange: (value: string) => void;
  label?: string;
}

const RadioGroup: React.FC<RadioGroupProps> = ({
  name,
  options,
  value,
  onChange,
  label,
}) => {
  return (
    <fieldset className="space-y-2">
      {label && (
        <legend className="text-sm font-medium text-slate-900 mb-2">
          {label}
        </legend>
      )}
      <div className="grid gap-2">
        {options.map((option) => {
          const isSelected = value === option;
          return (
            <label
              key={option}
              className={`relative flex cursor-pointer items-center gap-3 rounded-lg border-2 px-4 py-3 text-sm transition-colors ${
                isSelected
                  ? 'border-blue-500 bg-blue-50 text-slate-900'
                  : 'border-gray-200 bg-white text-slate-700 hover:border-gray-300'
              }`}
            >
              <input
                type="radio"
                name={name}
                value={option}
                checked={isSelected}
                onChange={() => onChange(option)}
                onFocus={(e) => e.target.blur()}
                tabIndex={-1}
                className="sr-only"
              />
              <span
                className={`flex h-5 w-5 shrink-0 items-center justify-center rounded-full border-2 ${
                  isSelected ? 'border-blue-500' : 'border-gray-300'
                }`}
              >
                {isSelected && (
                  <span className="h-2.5 w-2.5 rounded-full bg-blue-500" />
                )}
              </span>
              <span>{option}</span>
            </label>
          );
        })}
      </div>
    </fieldset>
  );
};

export default RadioGroup;
