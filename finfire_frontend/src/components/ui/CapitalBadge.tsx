import React from 'react';

const CAPITAL_COLORS: Record<string, string> = {
  Equity: '#2563EB',
  Debt: '#7C3AED',
  Grant: '#059669',
  Mezzanine: '#D97706',
  'Revenue-Based': '#DB2777',
};

const CAPITAL_BG: Record<string, string> = {
  Equity: '#EFF6FF',
  Debt: '#F5F3FF',
  Grant: '#ECFDF5',
  Mezzanine: '#FFFBEB',
  'Revenue-Based': '#FDF2F8',
};

interface CapitalBadgeProps {
  capital: string;
}

const CapitalBadge: React.FC<CapitalBadgeProps> = ({ capital }) => {
  const color = CAPITAL_COLORS[capital] ?? '#64748B';
  const bg = CAPITAL_BG[capital] ?? '#F1F5F9';

  return (
    <span
      style={{
        display: 'inline-block',
        borderRadius: 20,
        padding: '3px 10px',
        fontSize: 12,
        fontWeight: 600,
        color: color,
        background: bg,
        border: `1px solid ${color}44`,
        lineHeight: '18px',
        whiteSpace: 'nowrap',
      }}
    >
      {capital}
    </span>
  );
};

export default CapitalBadge;
