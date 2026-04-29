import React from 'react';
import { useQuery } from '@tanstack/react-query';
import { getContact } from '../../api/questionnaire';
import { useQuestionnaireStore } from '../../stores/questionnaireStore';
import { useAuthStore } from '../../stores/authStore';
import StatCard from '../ui/StatCard';
import Avatar from '../ui/Avatar';
import CapitalBadge from '../ui/CapitalBadge';

/* ── SVG icon paths ────────────────────────────────────────────────────────── */
const ICONS = {
  people:
    'M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05C16.19 13.89 17 15.02 17 16.5V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z',
  check:
    'M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z',
  warning:
    'M1 21h22L12 2 1 21zm12-3h-2v-2h2v2zm0-4h-2v-4h2v4z',
};

/* ── Colour helper for avatar ──────────────────────────────────────────────── */
const AVATAR_COLORS = ['#2563EB', '#7C3AED', '#059669', '#D97706', '#DB2777', '#0891B2'];
function avatarColor(name: string) {
  let hash = 0;
  for (let i = 0; i < name.length; i++) hash = name.charCodeAt(i) + ((hash << 5) - hash);
  return AVATAR_COLORS[Math.abs(hash) % AVATAR_COLORS.length];
}
function getInitials(name: string) {
  return name
    .split(' ')
    .filter(Boolean)
    .map((w) => w[0])
    .join('')
    .toUpperCase()
    .slice(0, 2);
}

/* ── Capital distribution placeholder ──────────────────────────────────────── */
const CAPITAL_DIST = [
  { label: 'Equity', count: 14, color: '#2563EB' },
  { label: 'Debt', count: 9, color: '#7C3AED' },
  { label: 'Grant', count: 6, color: '#059669' },
  { label: 'Mezzanine', count: 4, color: '#D97706' },
  { label: 'Revenue-Based', count: 3, color: '#DB2777' },
];

const DashboardHome: React.FC = () => {
  const setView = useQuestionnaireStore((s) => s.setView);
  const isAdmin = useAuthStore((s) => s.isAdmin);
  const user = useAuthStore((s) => s.user);

  const { data: users = [] } = useQuery<any[]>({
    queryKey: ['contact'],
    queryFn: async () => {
      const res = await getContact();
      return Array.isArray(res) ? res : [res];
    },
    retry: false,
    enabled: isAdmin,
  });

  // Non-admin welcome view
  if (!isAdmin) {
    return (
      <div>
        <div
          style={{
            background: '#FFFFFF',
            borderRadius: 16,
            border: '1px solid #E2E8F0',
            padding: '40px 32px',
            textAlign: 'center',
          }}
        >
          <h2 style={{ fontSize: 22, fontWeight: 700, color: '#0F172A', marginBottom: 8 }}>
            Welcome{user?.username ? `, ${user.username}` : ''}
          </h2>
          <p style={{ fontSize: 14, color: '#64748B', marginBottom: 24 }}>
            Start a new capital match or view your match results.
          </p>
          <button
            onClick={() => setView('newUser')}
            style={{
              background: 'linear-gradient(135deg, #3B82F6, #1D4ED8)',
              color: '#FFFFFF',
              border: 'none',
              borderRadius: 12,
              padding: '12px 28px',
              fontSize: 14,
              fontWeight: 600,
              cursor: 'pointer',
            }}
          >
            Start New Match
          </button>
        </div>
      </div>
    );
  }

  // Admin dashboard with full user data
  const totalUsers = users.length;
  const matchedCount = users.filter((u: any) => u.status === 'Matched').length;
  const pendingCount = users.filter((u: any) => u.status === 'Pending').length || Math.max(totalUsers - matchedCount, 0);
  const recentUsers = users.slice(0, 5);
  const maxBar = Math.max(...CAPITAL_DIST.map((d) => d.count), 1);

  return (
    <div>
      {/* ── Stat Cards ─────────────────────────────────────────────────────── */}
      <div
        style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(3, 1fr)',
          gap: 16,
          marginBottom: 24,
        }}
      >
        <StatCard label="Total users" value={totalUsers} icon={ICONS.people} accent="#2563EB" />
        <StatCard label="Matched" value={matchedCount} icon={ICONS.check} accent="#059669" />
        <StatCard label="Pending" value={pendingCount} icon={ICONS.warning} accent="#D97706" />
      </div>

      {/* ── Capital Type Distribution ──────────────────────────────────────── */}
      <div
        style={{
          background: '#FFFFFF',
          borderRadius: 16,
          border: '1px solid #E2E8F0',
          padding: '20px 24px',
          marginBottom: 24,
        }}
      >
        <div style={{ fontSize: 14, fontWeight: 600, color: '#0F172A', marginBottom: 16 }}>
          Capital type distribution
        </div>
        <div
          style={{
            display: 'flex',
            alignItems: 'flex-end',
            gap: 12,
            height: 80,
          }}
        >
          {CAPITAL_DIST.map((d) => (
            <div
              key={d.label}
              style={{
                flex: 1,
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                gap: 4,
              }}
            >
              <span style={{ fontSize: 11, fontWeight: 600, color: '#0F172A' }}>{d.count}</span>
              <div
                style={{
                  width: '100%',
                  maxWidth: 36,
                  height: Math.max((d.count / maxBar) * 56, 4),
                  borderRadius: 4,
                  background: d.color,
                }}
              />
              <span
                style={{
                  fontSize: 10,
                  color: '#64748B',
                  textAlign: 'center',
                  lineHeight: '12px',
                  whiteSpace: 'nowrap',
                }}
              >
                {d.label}
              </span>
            </div>
          ))}
        </div>
      </div>

      {/* ── Recent Users ───────────────────────────────────────────────────── */}
      <div
        style={{
          background: '#FFFFFF',
          borderRadius: 16,
          border: '1px solid #E2E8F0',
          padding: '20px 24px',
        }}
      >
        {/* Header */}
        <div
          style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            marginBottom: 16,
          }}
        >
          <span style={{ fontSize: 14, fontWeight: 600, color: '#0F172A' }}>Recent users</span>
          <button
            onClick={() => setView('users' as any)}
            style={{
              background: 'none',
              border: 'none',
              color: '#2563EB',
              fontSize: 12,
              fontWeight: 600,
              cursor: 'pointer',
              padding: 0,
            }}
          >
            View all &rarr;
          </button>
        </div>

        {/* User rows */}
        {recentUsers.length === 0 && (
          <div style={{ fontSize: 13, color: '#94A3B8', textAlign: 'center', padding: 24 }}>
            No users yet. Add a new user to get started.
          </div>
        )}
        {recentUsers.map((userRow: any, idx: number) => {
          const name = userRow.display_name || userRow.email || 'Unknown';
          const company = userRow.companyWebsite || userRow.primaryBusinessAddress || '';
          const status = userRow.status || 'Pending';
          const capitalType = userRow.capitalType || '';
          const date = userRow.created_at
            ? new Date(userRow.created_at).toLocaleDateString()
            : '';

          return (
            <div
              key={idx}
              style={{
                display: 'flex',
                alignItems: 'center',
                gap: 12,
                padding: '10px 0',
                borderTop: idx > 0 ? '1px solid #F1F5F9' : 'none',
              }}
            >
              <Avatar initials={getInitials(name)} color={avatarColor(name)} size={36} />
              <div style={{ flex: 1, minWidth: 0 }}>
                <div
                  style={{
                    fontSize: 13,
                    fontWeight: 600,
                    color: '#0F172A',
                    overflow: 'hidden',
                    textOverflow: 'ellipsis',
                    whiteSpace: 'nowrap',
                  }}
                >
                  {name}
                </div>
                <div
                  style={{
                    fontSize: 11,
                    color: '#94A3B8',
                    overflow: 'hidden',
                    textOverflow: 'ellipsis',
                    whiteSpace: 'nowrap',
                  }}
                >
                  {company}
                </div>
              </div>
              {date && (
                <span style={{ fontSize: 11, color: '#94A3B8', flexShrink: 0 }}>{date}</span>
              )}
              {capitalType && <CapitalBadge capital={capitalType} />}
              <span
                style={{
                  fontSize: 11,
                  fontWeight: 600,
                  padding: '2px 8px',
                  borderRadius: 10,
                  flexShrink: 0,
                  background: status === 'Matched' ? '#DCFCE7' : '#FEF3C7',
                  color: status === 'Matched' ? '#166534' : '#92400E',
                }}
              >
                {status}
              </span>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default DashboardHome;
