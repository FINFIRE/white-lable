import React from 'react';

interface StatCardProps {
  label: string;
  value: string | number;
  icon: string;
  accent: string;
}

const StatCard: React.FC<StatCardProps> = ({ label, value, icon, accent }) => {
  return (
    <div
      style={{
        background: '#FFFFFF',
        borderRadius: 16,
        border: '1px solid #E2E8F0',
        padding: '20px 22px',
        display: 'flex',
        alignItems: 'center',
        gap: 16,
      }}
    >
      {/* Icon box */}
      <div
        style={{
          width: 46,
          height: 46,
          borderRadius: 12,
          background: accent + '18',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          flexShrink: 0,
        }}
      >
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none">
          <path d={icon} fill={accent} />
        </svg>
      </div>

      {/* Text */}
      <div style={{ display: 'flex', flexDirection: 'column' }}>
        <span
          style={{
            fontSize: 13,
            color: '#94A3B8',
            fontWeight: 500,
            lineHeight: '16px',
          }}
        >
          {label}
        </span>
        <span
          style={{
            fontSize: 26,
            fontWeight: 700,
            color: '#0F172A',
            lineHeight: '32px',
          }}
        >
          {value}
        </span>
      </div>
    </div>
  );
};

export default StatCard;
