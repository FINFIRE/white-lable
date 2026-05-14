import React, { useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import { getAdminUsers, type AdminUser } from '../../api/admin';
import { useQuestionnaireStore } from '../../stores/questionnaireStore';
import Avatar from '../ui/Avatar';
import LoadingSpinner from '../ui/LoadingSpinner';

const AVATAR_COLORS = ['#2563EB', '#7C3AED', '#059669', '#D97706', '#DB2777', '#0891B2'];
function avatarColor(name: string) {
  let hash = 0;
  for (let i = 0; i < name.length; i++) hash = name.charCodeAt(i) + ((hash << 5) - hash);
  return AVATAR_COLORS[Math.abs(hash) % AVATAR_COLORS.length];
}
function initials(name: string) {
  return name.split(/[\s._-]+/).filter(Boolean).map((w) => w[0]).join('').toUpperCase().slice(0, 2) || '??';
}

const AdminDashboard: React.FC = () => {
  const setView = useQuestionnaireStore((s) => s.setView);
  const setAdminEditUserId = useQuestionnaireStore((s) => s.setAdminEditUserId);
  const [search, setSearch] = useState('');

  const { data: users = [], isLoading } = useQuery({
    queryKey: ['adminUsers'],
    queryFn: getAdminUsers,
  });

  const filtered = users.filter((u) => {
    const q = search.toLowerCase();
    const name = u.contact?.display_name || u.username;
    const email = u.contact?.email || u.email;
    return name.toLowerCase().includes(q) || email.toLowerCase().includes(q) || u.username.toLowerCase().includes(q);
  });

  const handleEditUser = (user: AdminUser) => {
    setAdminEditUserId(user.id);
    setView('adminEditUser');
  };

  const handleCreateUser = () => {
    setView('adminCreateUser');
  };

  if (isLoading) {
    return (
      <div className="flex items-center justify-center py-24">
        <LoadingSpinner />
      </div>
    );
  }

  return (
    <div>
      {/* Stats */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 16, marginBottom: 24 }}>
        {[
          { label: 'Total Users', value: users.length, color: '#2563EB' },
          { label: 'Active', value: users.filter((u) => u.is_active).length, color: '#059669' },
          { label: 'Inactive', value: users.filter((u) => !u.is_active).length, color: '#D97706' },
        ].map((s) => (
          <div
            key={s.label}
            style={{
              background: '#fff',
              borderRadius: 16,
              border: '1px solid #E2E8F0',
              padding: '20px 24px',
            }}
          >
            <div style={{ fontSize: 12, color: '#64748B', fontWeight: 500, marginBottom: 4 }}>{s.label}</div>
            <div style={{ fontSize: 28, fontWeight: 800, color: s.color }}>{s.value}</div>
          </div>
        ))}
      </div>

      {/* User table */}
      <div style={{ background: '#fff', borderRadius: 16, border: '1px solid #E2E8F0', overflow: 'hidden' }}>
        {/* Header */}
        <div
          style={{
            padding: '16px 24px',
            borderBottom: '1px solid #F1F5F9',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            gap: 12,
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
            <span style={{ fontSize: 14, fontWeight: 700, color: '#0F172A' }}>All Users</span>
            <span style={{ fontSize: 13, color: '#94A3B8' }}>({filtered.length})</span>
          </div>

          <div style={{ display: 'flex', gap: 10, alignItems: 'center' }}>
            <input
              type="text"
              placeholder="Search users..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              style={{
                border: '1px solid #E2E8F0',
                borderRadius: 8,
                padding: '7px 12px',
                fontSize: 13,
                width: 220,
                outline: 'none',
              }}
            />
            <button
              onClick={handleCreateUser}
              style={{
                background: '#2563EB',
                color: '#fff',
                borderRadius: 10,
                padding: '8px 16px',
                border: 'none',
                cursor: 'pointer',
                fontSize: 13,
                fontWeight: 600,
                display: 'flex',
                alignItems: 'center',
                gap: 6,
                whiteSpace: 'nowrap',
              }}
            >
              <span style={{ fontSize: 16, lineHeight: 1 }}>+</span>
              Create User
            </button>
          </div>
        </div>

        {/* Table */}
        <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 13 }}>
          <thead>
            <tr style={{ background: '#F8FAFC' }}>
              {['User', 'Email', 'Status', 'Joined', 'Actions'].map((h) => (
                <th
                  key={h}
                  style={{
                    padding: '10px 16px',
                    color: '#64748B',
                    fontWeight: 600,
                    fontSize: 12,
                    textAlign: 'left',
                    whiteSpace: 'nowrap',
                  }}
                >
                  {h}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {filtered.map((user) => {
              const name = user.contact?.display_name || user.username;
              const email = user.contact?.email || user.email;
              const company = user.contact?.primaryBusinessAddress || '';

              return (
                <tr key={user.id} style={{ borderBottom: '1px solid #F8FAFC' }}>
                  <td style={{ padding: '10px 16px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                      <Avatar initials={initials(name)} color={avatarColor(name)} />
                      <div>
                        <div style={{ fontWeight: 600, color: '#0F172A' }}>{name}</div>
                        {company && (
                          <div style={{ fontSize: 11, color: '#94A3B8', marginTop: 1 }}>{company}</div>
                        )}
                      </div>
                    </div>
                  </td>
                  <td style={{ padding: '10px 16px', color: '#64748B' }}>{email}</td>
                  <td style={{ padding: '10px 16px' }}>
                    <span
                      style={{
                        display: 'inline-block',
                        borderRadius: 20,
                        padding: '3px 10px',
                        fontSize: 12,
                        fontWeight: 600,
                        background: user.is_active ? '#DCFCE7' : '#FEF3C7',
                        color: user.is_active ? '#166534' : '#92400E',
                      }}
                    >
                      {user.is_active ? 'Active' : 'Inactive'}
                    </span>
                  </td>
                  <td style={{ padding: '10px 16px', color: '#94A3B8' }}>
                    {new Date(user.date_joined).toLocaleDateString()}
                  </td>
                  <td style={{ padding: '10px 16px' }}>
                    <button
                      onClick={() => handleEditUser(user)}
                      style={{
                        border: '1px solid #BFDBFE',
                        background: '#EFF6FF',
                        color: '#1D4ED8',
                        borderRadius: 8,
                        padding: '5px 14px',
                        fontSize: 12,
                        fontWeight: 600,
                        cursor: 'pointer',
                      }}
                    >
                      View / Edit
                    </button>
                  </td>
                </tr>
              );
            })}
            {filtered.length === 0 && (
              <tr>
                <td colSpan={5} style={{ padding: 32, textAlign: 'center', color: '#94A3B8' }}>
                  No users found.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default AdminDashboard;
