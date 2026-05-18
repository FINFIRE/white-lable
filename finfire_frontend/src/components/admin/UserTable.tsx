import React, { useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import { getContact } from '../../api/questionnaire';
import { useQuestionnaireStore } from '../../stores/questionnaireStore';
import Avatar from '../ui/Avatar';
import CapitalBadge from '../ui/CapitalBadge';
import UserDetailModal from './UserDetailModal';
import DocumentModal from './DocumentModal';

const AVATAR_PALETTE = ['#2563EB', '#7C3AED', '#0891B2', '#059669', '#D97706'];

function getInitials(name: string): string {
  return name
    .split(' ')
    .map((w) => w[0] ?? '')
    .join('')
    .slice(0, 2)
    .toUpperCase();
}

interface UserRow {
  id: number;
  display_name: string;
  email: string;
  companyAffiliation: string[];
  primaryBusinessAddress: string;
  capitalType: string;
  status: string;
  date: string;
}

const MOCK_USERS: UserRow[] = [
  {
    id: 1,
    display_name: 'Sarah Johnson',
    email: 'sarah@acmecorp.io',
    companyAffiliation: ['Acme Corp'],
    primaryBusinessAddress: 'San Francisco, CA',
    capitalType: 'Equity',
    status: 'Matched',
    date: '2026-03-15',
  },
  {
    id: 2,
    display_name: 'James Williams',
    email: 'james@bluewave.co',
    companyAffiliation: ['BlueWave'],
    primaryBusinessAddress: 'Austin, TX',
    capitalType: 'Debt',
    status: 'Pending',
    date: '2026-03-12',
  },
  {
    id: 3,
    display_name: 'Maria Garcia',
    email: 'maria@greenfield.io',
    companyAffiliation: ['Greenfield'],
    primaryBusinessAddress: 'Miami, FL',
    capitalType: 'Grant',
    status: 'Matched',
    date: '2026-03-10',
  },
  {
    id: 4,
    display_name: 'Robert Chen',
    email: 'robert@novatech.com',
    companyAffiliation: ['NovaTech'],
    primaryBusinessAddress: 'Seattle, WA',
    capitalType: 'Mezzanine',
    status: 'Pending',
    date: '2026-03-08',
  },
  {
    id: 5,
    display_name: 'Emily Davis',
    email: 'emily@startuphub.co',
    companyAffiliation: ['StartupHub'],
    primaryBusinessAddress: 'Denver, CO',
    capitalType: 'Revenue-Based',
    status: 'Matched',
    date: '2026-03-05',
  },
];

const HEADERS = ['User', 'Contact', 'Capital type', 'Status', 'Date', 'Actions'];

const UserTable: React.FC = () => {
  const setView = useQuestionnaireStore((s) => s.setView);
  const [editingUser, setEditingUser] = useState<UserRow | null>(null);
  const [selectedDoc, setSelectedDoc] = useState<UserRow | null>(null);

  const { data: contactData } = useQuery({
    queryKey: ['contact'],
    queryFn: getContact,
  });

  // Merge live contact into first row if available
  const users: UserRow[] = contactData
    ? [
        {
          id: 0,
          display_name: contactData.display_name || 'Current User',
          email: contactData.email || '',
          companyAffiliation: contactData.companyAffiliation ?? [],
          primaryBusinessAddress: contactData.primaryBusinessAddress || '',
          capitalType: 'Pending',
          status: 'Pending',
          date: new Date().toISOString().slice(0, 10),
        },
        ...MOCK_USERS,
      ]
    : MOCK_USERS;

  const handleSaveUser = (_updated: any) => {
    setEditingUser(null);
  };

  return (
    <>
      <div
        style={{
          background: '#fff',
          borderRadius: 16,
          border: '1px solid #E2E8F0',
          overflow: 'hidden',
        }}
      >
        {/* Header */}
        <div
          style={{
            padding: '16px 24px',
            borderBottom: '1px solid #F1F5F9',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
            <span style={{ fontSize: 14, fontWeight: 700, color: '#0F172A' }}>
              All users
            </span>
            <span style={{ fontSize: 13, color: '#94A3B8' }}>
              ({users.length})
            </span>
          </div>
          <button
            onClick={() => setView('newUser')}
            style={{
              background: '#2563EB',
              color: '#fff',
              borderRadius: 10,
              padding: '7px 14px',
              border: 'none',
              cursor: 'pointer',
              fontSize: 13,
              fontWeight: 600,
              display: 'flex',
              alignItems: 'center',
              gap: 6,
            }}
          >
            <span style={{ fontSize: 16, lineHeight: 1 }}>+</span>
            New user
          </button>
        </div>

        {/* Table */}
        <table
          style={{
            width: '100%',
            borderCollapse: 'collapse',
            fontSize: 13,
          }}
        >
          <thead>
            <tr style={{ background: '#F8FAFC' }}>
              {HEADERS.map((h) => (
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
            {users.map((user, idx) => {
              const avatarColor = AVATAR_PALETTE[idx % AVATAR_PALETTE.length];
              const initials = getInitials(user.display_name);
              const company =
                user.companyAffiliation?.[0] || user.primaryBusinessAddress || '';
              const isMatched = user.status === 'Matched';

              return (
                <tr
                  key={user.id ?? idx}
                  style={{ borderBottom: '1px solid #F8FAFC' }}
                >
                  {/* User */}
                  <td style={{ padding: '10px 16px' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                      <Avatar initials={initials} color={avatarColor} />
                      <div>
                        <div style={{ fontWeight: 600, color: '#0F172A' }}>
                          {user.display_name}
                        </div>
                        <div
                          style={{
                            fontSize: 11,
                            color: '#94A3B8',
                            marginTop: 1,
                          }}
                        >
                          {company}
                        </div>
                      </div>
                    </div>
                  </td>

                  {/* Contact */}
                  <td style={{ padding: '10px 16px', color: '#64748B' }}>
                    {user.email}
                  </td>

                  {/* Capital type */}
                  <td style={{ padding: '10px 16px' }}>
                    <CapitalBadge capital={user.capitalType} />
                  </td>

                  {/* Status */}
                  <td style={{ padding: '10px 16px' }}>
                    <span
                      style={{
                        display: 'inline-block',
                        borderRadius: 20,
                        padding: '3px 10px',
                        fontSize: 12,
                        fontWeight: 600,
                        lineHeight: '18px',
                        background: isMatched ? '#DCFCE7' : '#FEF9C3',
                        color: isMatched ? '#166534' : '#854D0E',
                      }}
                    >
                      {user.status}
                    </span>
                  </td>

                  {/* Date */}
                  <td style={{ padding: '10px 16px', color: '#94A3B8' }}>
                    {user.date}
                  </td>

                  {/* Actions */}
                  <td style={{ padding: '10px 16px' }}>
                    <div style={{ display: 'flex', gap: 6 }}>
                      <button
                        onClick={() => setEditingUser(user)}
                        style={{
                          border: '1px solid #E2E8F0',
                          background: '#fff',
                          color: '#334155',
                          borderRadius: 8,
                          padding: '5px 12px',
                          fontSize: 12,
                          fontWeight: 600,
                          cursor: 'pointer',
                        }}
                      >
                        Edit
                      </button>
                      <button
                        onClick={() => setSelectedDoc(user)}
                        style={{
                          border: '1px solid #BFDBFE',
                          background: '#EFF6FF',
                          color: '#1D4ED8',
                          borderRadius: 8,
                          padding: '5px 12px',
                          fontSize: 12,
                          fontWeight: 600,
                          cursor: 'pointer',
                        }}
                      >
                        View doc
                      </button>
                    </div>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>

      {/* Modals */}
      {editingUser && (
        <UserDetailModal
          isOpen={true}
          onClose={() => setEditingUser(null)}
          user={editingUser}
          onSave={handleSaveUser}
        />
      )}
      {selectedDoc && (
        <DocumentModal
          isOpen={true}
          onClose={() => setSelectedDoc(null)}
          user={selectedDoc}
        />
      )}
    </>
  );
};

export default UserTable;
