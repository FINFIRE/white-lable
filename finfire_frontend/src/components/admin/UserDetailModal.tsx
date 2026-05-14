import React, { useState, useEffect } from 'react';

interface UserDetailModalProps {
  isOpen: boolean;
  onClose: () => void;
  user: any;
  onSave: (updated: any) => void;
}

const CAPITAL_OPTIONS = ['Equity', 'Debt', 'Grant', 'Mezzanine', 'Revenue-Based'];

const labelStyle: React.CSSProperties = {
  fontSize: 12,
  fontWeight: 600,
  color: '#64748B',
  textTransform: 'uppercase',
  marginBottom: 6,
  display: 'block',
};

const inputStyle: React.CSSProperties = {
  width: '100%',
  padding: '10px 12px',
  borderRadius: 10,
  border: '1.5px solid #E2E8F0',
  fontSize: 13,
  color: '#0F172A',
  outline: 'none',
  boxSizing: 'border-box',
  background: '#fff',
};

const UserDetailModal: React.FC<UserDetailModalProps> = ({
  isOpen,
  onClose,
  user,
  onSave,
}) => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [company, setCompany] = useState('');
  const [capitalType, setCapitalType] = useState('');

  useEffect(() => {
    if (user) {
      setName(user.display_name || '');
      setEmail(user.email || '');
      setCompany(user.companyAffiliation?.[0] || user.company || '');
      setCapitalType(user.capitalType || 'Equity');
    }
  }, [user]);

  if (!isOpen) return null;

  const handleSave = () => {
    onSave({
      ...user,
      display_name: name,
      email,
      companyAffiliation: [company],
      capitalType,
    });
  };

  return (
    <div
      style={{
        position: 'fixed',
        inset: 0,
        background: 'rgba(15,23,42,0.5)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        zIndex: 100,
      }}
      onClick={onClose}
    >
      <div
        style={{
          background: '#fff',
          borderRadius: 20,
          padding: 32,
          width: 420,
          boxShadow: '0 20px 60px rgba(0,0,0,0.2)',
          position: 'relative',
        }}
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div
          style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            marginBottom: 24,
          }}
        >
          <span style={{ fontSize: 17, fontWeight: 700, color: '#0F172A' }}>
            Edit user
          </span>
          <button
            onClick={onClose}
            style={{
              width: 30,
              height: 30,
              borderRadius: 8,
              background: '#F1F5F9',
              border: 'none',
              cursor: 'pointer',
              fontSize: 15,
              color: '#64748B',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
            }}
          >
            &#10005;
          </button>
        </div>

        {/* Fields */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
          <div>
            <label style={labelStyle}>Name</label>
            <input
              style={inputStyle}
              value={name}
              onChange={(e) => setName(e.target.value)}
            />
          </div>

          <div>
            <label style={labelStyle}>Email</label>
            <input
              style={inputStyle}
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>

          <div>
            <label style={labelStyle}>Company</label>
            <input
              style={inputStyle}
              value={company}
              onChange={(e) => setCompany(e.target.value)}
            />
          </div>

          <div>
            <label style={labelStyle}>Capital type</label>
            <select
              style={{
                ...inputStyle,
                appearance: 'auto',
              }}
              value={capitalType}
              onChange={(e) => setCapitalType(e.target.value)}
            >
              {CAPITAL_OPTIONS.map((opt) => (
                <option key={opt} value={opt}>
                  {opt}
                </option>
              ))}
            </select>
          </div>
        </div>

        {/* Buttons */}
        <div style={{ display: 'flex', gap: 10, marginTop: 28 }}>
          <button
            onClick={handleSave}
            style={{
              flex: 1,
              padding: '10px 0',
              borderRadius: 10,
              border: 'none',
              background: 'linear-gradient(135deg, #2563EB, #1D4ED8)',
              color: '#fff',
              fontSize: 13,
              fontWeight: 700,
              cursor: 'pointer',
            }}
          >
            Save changes
          </button>
          <button
            onClick={onClose}
            style={{
              flex: 1,
              padding: '10px 0',
              borderRadius: 10,
              border: '1.5px solid #E2E8F0',
              background: '#fff',
              color: '#334155',
              fontSize: 13,
              fontWeight: 700,
              cursor: 'pointer',
            }}
          >
            Cancel
          </button>
        </div>
      </div>
    </div>
  );
};

export default UserDetailModal;
