import React from 'react';
import { useQuestionnaireStore } from '../../stores/questionnaireStore';
import { useAuthStore } from '../../stores/authStore';

interface NavItem {
  id: string;
  label: string;
  icon: string;
}

const ADMIN_NAV: NavItem[] = [
  {
    id: 'dashboard',
    label: 'All Users',
    icon: 'M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5s-3 1.34-3 3 1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05C16.19 13.89 17 15.02 17 16.5V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z',
  },
  {
    id: 'adminCreateUser',
    label: 'Create User',
    icon: 'M12 12c2.7 0 5-2.3 5-5s-2.3-5-5-5-5 2.3-5 5 2.3 5 5 5zm0 2c-3.3 0-10 1.7-10 5v1c0 .6.4 1 1 1h18c.6 0 1-.4 1-1v-1c0-3.3-6.7-5-10-5zm9-7h-2V5a1 1 0 10-2 0v2h-2a1 1 0 100 2h2v2a1 1 0 102 0V9h2a1 1 0 100-2z',
  },
];

const USER_NAV: NavItem[] = [
  {
    id: 'dashboard',
    label: 'Dashboard',
    icon: 'M4 5a1 1 0 011-1h4a1 1 0 011 1v4a1 1 0 01-1 1H5a1 1 0 01-1-1V5zm10 0a1 1 0 011-1h4a1 1 0 011 1v4a1 1 0 01-1 1h-4a1 1 0 01-1-1V5zM4 15a1 1 0 011-1h4a1 1 0 011 1v4a1 1 0 01-1 1H5a1 1 0 01-1-1v-4zm10 0a1 1 0 011-1h4a1 1 0 011 1v4a1 1 0 01-1 1h-4a1 1 0 01-1-1v-4z',
  },
  {
    id: 'newUser',
    label: 'New Match',
    icon: 'M12 12c2.7 0 5-2.3 5-5s-2.3-5-5-5-5 2.3-5 5 2.3 5 5 5zm0 2c-3.3 0-10 1.7-10 5v1c0 .6.4 1 1 1h18c.6 0 1-.4 1-1v-1c0-3.3-6.7-5-10-5zm9-7h-2V5a1 1 0 10-2 0v2h-2a1 1 0 100 2h2v2a1 1 0 102 0V9h2a1 1 0 100-2z',
  },
];

const Sidebar: React.FC = () => {
  const view = useQuestionnaireStore((s) => s.view);
  const setView = useQuestionnaireStore((s) => s.setView);
  const goToStep = useQuestionnaireStore((s) => s.goToStep);
  const setAnimating = useQuestionnaireStore((s) => s.setAnimating);
  const user = useAuthStore((s) => s.user);
  const isAdmin = useAuthStore((s) => s.isAdmin);
  const logout = useAuthStore((s) => s.logout);

  const navItems = isAdmin ? ADMIN_NAV : USER_NAV;

  const handleNav = (id: string) => {
    setView(id as any);
    goToStep(0);
    setAnimating(false);
  };

  const initials = user?.username
    ? user.username
        .split(/[\s._-]+/)
        .map((w) => w[0]?.toUpperCase() ?? '')
        .slice(0, 2)
        .join('')
    : '??';

  return (
    <aside
      style={{
        width: 240,
        minWidth: 240,
        background: '#0F172A',
        display: 'flex',
        flexDirection: 'column',
        height: '100%',
        userSelect: 'none',
      }}
    >
      {/* Logo */}
      <div style={{ padding: '22px 18px 18px', display: 'flex', alignItems: 'center', gap: 10 }}>
        <img
          src="/logo.png"
          alt="FINFIRE"
          style={{ height: 34, width: 'auto', flexShrink: 0 }}
        />
        <div>
          <div style={{ fontSize: 11, color: '#64748B', lineHeight: '14px' }}>
            {isAdmin ? 'Admin Panel' : 'Tenant Portal'}
          </div>
        </div>
      </div>

      {/* Nav */}
      <nav style={{ flex: 1, padding: '6px 10px', display: 'flex', flexDirection: 'column', gap: 2 }}>
        {navItems.map((item) => {
          const active =
            view === item.id ||
            (item.id === 'dashboard' && view === 'adminEditUser') ||
            (item.id === 'newUser' && view === 'matched');
          return (
            <button
              key={item.id}
              onClick={() => handleNav(item.id)}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 10,
                padding: '10px 12px',
                borderRadius: 10,
                border: 'none',
                cursor: 'pointer',
                background: active ? '#1E293B' : 'transparent',
                color: active ? '#F8FAFC' : '#94A3B8',
                fontWeight: active ? 600 : 400,
                fontSize: 14,
                fontFamily: 'inherit',
                width: '100%',
                textAlign: 'left',
                position: 'relative',
                transition: 'background 0.15s, color 0.15s',
              }}
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill={active ? '#3B82F6' : '#64748B'}>
                <path d={item.icon} />
              </svg>
              <span>{item.label}</span>
              {active && (
                <span
                  style={{
                    position: 'absolute',
                    right: 10,
                    width: 6,
                    height: 6,
                    borderRadius: '50%',
                    background: '#3B82F6',
                  }}
                />
              )}
            </button>
          );
        })}
      </nav>

      {/* User + Logout */}
      <div style={{ borderTop: '1px solid #1E293B', padding: '14px 16px', display: 'flex', flexDirection: 'column', gap: 10 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          <div
            style={{
              width: 32,
              height: 32,
              borderRadius: '50%',
              background: isAdmin ? '#7C3AED' : '#1E40AF',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontSize: 12,
              fontWeight: 700,
              color: '#FFFFFF',
              flexShrink: 0,
            }}
          >
            {initials}
          </div>
          <div style={{ overflow: 'hidden', flex: 1 }}>
            <div style={{ fontSize: 12, fontWeight: 600, color: '#E2E8F0', lineHeight: '16px' }}>
              {user?.username ?? 'User'}
              {isAdmin && (
                <span style={{ marginLeft: 6, fontSize: 10, color: '#A78BFA', fontWeight: 500 }}>
                  ADMIN
                </span>
              )}
            </div>
            <div
              style={{
                fontSize: 11,
                color: '#475569',
                lineHeight: '14px',
                overflow: 'hidden',
                textOverflow: 'ellipsis',
                whiteSpace: 'nowrap',
              }}
            >
              {user?.email ?? ''}
            </div>
          </div>
        </div>

        <button
          onClick={() => logout()}
          style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: 8,
            width: '100%',
            padding: '8px 12px',
            borderRadius: 8,
            border: '1px solid #334155',
            background: 'transparent',
            color: '#94A3B8',
            fontSize: 13,
            fontWeight: 500,
            fontFamily: 'inherit',
            cursor: 'pointer',
            transition: 'background 0.15s, color 0.15s',
          }}
          onMouseEnter={(e) => {
            e.currentTarget.style.background = '#1E293B';
            e.currentTarget.style.color = '#F8FAFC';
          }}
          onMouseLeave={(e) => {
            e.currentTarget.style.background = 'transparent';
            e.currentTarget.style.color = '#94A3B8';
          }}
        >
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
            <path
              d="M9 21H5a2 2 0 01-2-2V5a2 2 0 012-2h4M16 17l5-5-5-5M21 12H9"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
          </svg>
          Logout
        </button>
      </div>
    </aside>
  );
};

export default Sidebar;
