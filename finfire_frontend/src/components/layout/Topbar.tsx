import React from 'react';
import { useQuestionnaireStore } from '../../stores/questionnaireStore';
import { useAuthStore } from '../../stores/authStore';
import { getTotalSteps } from '../../constants/stepConfig';

const VIEW_META: Record<string, { title: string; subtitle: string }> = {
  dashboard: { title: 'Dashboard', subtitle: 'Overview & recent activity' },
  newUser: { title: 'New user match', subtitle: 'Match a user to a capital type' },
  users: { title: 'All users', subtitle: 'Manage all user records' },
  matched: { title: 'Match result', subtitle: 'Document generated' },
  adminEditUser: { title: 'Edit User', subtitle: 'View and modify user form data' },
  adminCreateUser: { title: 'Create User', subtitle: 'Add a new user to the system' },
};

const Topbar: React.FC = () => {
  const view = useQuestionnaireStore((s) => s.view);
  const currentStep = useQuestionnaireStore((s) => s.currentStep);
  const setView = useQuestionnaireStore((s) => s.setView);
  const isAdmin = useAuthStore((s) => s.isAdmin);

  const accountType = useQuestionnaireStore((s) => s.accountType);
  const totalSteps = getTotalSteps(accountType);
  const progress = ((currentStep + 1) / totalSteps) * 100;

  // Admin dashboard title override
  const meta = isAdmin && view === 'dashboard'
    ? { title: 'Admin Dashboard', subtitle: 'Manage users and their data' }
    : VIEW_META[view] ?? VIEW_META.dashboard;

  return (
    <div
      style={{
        background: '#FFFFFF',
        borderBottom: '1px solid #E2E8F0',
        padding: '0 28px',
        height: 58,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        flexShrink: 0,
      }}
    >
      <div>
        <div style={{ fontSize: 17, fontWeight: 700, color: '#0F172A', lineHeight: '22px' }}>
          {meta.title}
        </div>
        <div style={{ fontSize: 11, color: '#94A3B8', marginTop: 1, lineHeight: '14px' }}>
          {meta.subtitle}
        </div>
      </div>

      {view === 'newUser' ? (
        <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          <div
            style={{
              width: 180,
              height: 5,
              borderRadius: 4,
              background: '#E2E8F0',
              overflow: 'hidden',
            }}
          >
            <div
              style={{
                width: `${progress}%`,
                height: '100%',
                borderRadius: 4,
                background:
                  'linear-gradient(90deg, var(--brand-primary), var(--brand-accent))',
                transition: 'width 0.3s ease',
              }}
            />
          </div>
          <span style={{ fontSize: 12, fontWeight: 600, color: '#64748B', whiteSpace: 'nowrap' }}>
            {currentStep + 1}/{totalSteps}
          </span>
        </div>
      ) : isAdmin && view === 'dashboard' ? (
        <button
          onClick={() => setView('adminCreateUser')}
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 6,
            background: 'var(--brand-primary)',
            color: '#FFFFFF',
            border: 'none',
            borderRadius: 10,
            padding: '8px 16px',
            fontSize: 13,
            fontWeight: 600,
            cursor: 'pointer',
            fontFamily: 'inherit',
            transition: 'filter 0.15s',
          }}
          onMouseEnter={(e) => (e.currentTarget.style.filter = 'brightness(0.9)')}
          onMouseLeave={(e) => (e.currentTarget.style.filter = '')}
        >
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none">
            <path d="M12 5v14M5 12h14" stroke="#FFFFFF" strokeWidth="2.2" strokeLinecap="round" />
          </svg>
          Create User
        </button>
      ) : !isAdmin && view !== 'matched' ? (
        <button
          onClick={() => setView('newUser')}
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 6,
            background: 'var(--brand-primary)',
            color: '#FFFFFF',
            border: 'none',
            borderRadius: 10,
            padding: '8px 16px',
            fontSize: 13,
            fontWeight: 600,
            cursor: 'pointer',
            fontFamily: 'inherit',
            transition: 'filter 0.15s',
          }}
          onMouseEnter={(e) => (e.currentTarget.style.filter = 'brightness(0.9)')}
          onMouseLeave={(e) => (e.currentTarget.style.filter = '')}
        >
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none">
            <path d="M12 5v14M5 12h14" stroke="#FFFFFF" strokeWidth="2.2" strokeLinecap="round" />
          </svg>
          New Match
        </button>
      ) : null}
    </div>
  );
};

export default Topbar;
