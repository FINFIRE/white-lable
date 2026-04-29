import React from 'react';

interface RangeSliderProps {
  name: string;
  label: string;
  tooltip?: string;
  value: number;
  onChange: (value: number) => void;
  min?: number;
  max?: number;
}

const RangeSlider: React.FC<RangeSliderProps> = ({
  name,
  label,
  tooltip,
  value,
  onChange,
  min = 0,
  max = 10,
}) => {
  const percentage = ((value - min) / (max - min)) * 100;

  return (
    <div className="space-y-2">
      <div className="flex items-center justify-between">
        <label
          htmlFor={name}
          className="text-sm font-medium text-slate-900"
          title={tooltip}
        >
          {label}
        </label>
        <span
          className="inline-flex h-7 w-9 items-center justify-center rounded-md text-sm font-bold"
          style={{
            background:
              value === 0
                ? '#F1F5F9'
                : value <= 3
                  ? '#FEF3C7'
                  : value <= 6
                    ? '#DBEAFE'
                    : '#DCFCE7',
            color:
              value === 0
                ? '#94A3B8'
                : value <= 3
                  ? '#92400E'
                  : value <= 6
                    ? '#1E40AF'
                    : '#166534',
          }}
        >
          {value}
        </span>
      </div>
      <input
        id={name}
        type="range"
        min={min}
        max={max}
        step={1}
        value={value}
        onChange={(e) => onChange(Number(e.target.value))}
        className="w-full h-2 rounded-lg appearance-none cursor-pointer"
        style={{
          background: `linear-gradient(to right, #3B82F6 0%, #3B82F6 ${percentage}%, #E2E8F0 ${percentage}%, #E2E8F0 100%)`,
        }}
      />
      <div className="flex justify-between text-[10px] text-slate-400">
        <span>{min}</span>
        <span>{max}</span>
      </div>
    </div>
  );
};

export default RangeSlider;
