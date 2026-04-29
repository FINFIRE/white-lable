import React from 'react';

interface AvatarProps {
  initials: string;
  color: string;
  size?: number;
}

const Avatar: React.FC<AvatarProps> = ({ initials, color, size = 38 }) => {
  return (
    <div
      style={{
        width: size,
        height: size,
        borderRadius: '50%',
        background: color + '22',
        border: `1.5px solid ${color}44`,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        fontSize: size * 0.34,
        fontWeight: 700,
        color: color,
        lineHeight: 1,
        flexShrink: 0,
      }}
    >
      {initials}
    </div>
  );
};

export default Avatar;
