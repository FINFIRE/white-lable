import React from 'react';
import { ChevronDown } from 'lucide-react';

interface SelectDropdownProps {
  name: string;
  options: string[];
  value: string;
  onChange: (value: string) => void;
  label?: string;
  placeholder?: string;
}

const SelectDropdown: React.FC<SelectDropdownProps> = ({
  name,
  options,
  value,
  onChange,
  label,
  placeholder = 'Select an option',
}) => {
  return (
    <div className="space-y-1">
      {label && (
        <label
          htmlFor={name}
          className="block text-sm font-medium text-slate-900"
        >
          {label}
        </label>
      )}
      <div className="relative">
        <select
          id={name}
          name={name}
          value={value}
          onChange={(e) => onChange(e.target.value)}
          className="block w-full appearance-none rounded-lg border border-gray-300 bg-white px-4 py-2.5 pr-10 text-sm text-slate-900 transition-colors focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-200"
        >
          <option value="" disabled>
            {placeholder}
          </option>
          {options.map((option) => (
            <option key={option} value={option}>
              {option}
            </option>
          ))}
        </select>
        <ChevronDown className="pointer-events-none absolute right-3 top-1/2 h-4 w-4 -translate-y-1/2 text-gray-400" />
      </div>
    </div>
  );
};

export default SelectDropdown;
