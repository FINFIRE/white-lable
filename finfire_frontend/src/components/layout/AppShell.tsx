import React from 'react';
import Sidebar from './Sidebar';
import Topbar from './Topbar';
import { useQuestionnaireStore } from '../../stores/questionnaireStore';
import { useAuthStore } from '../../stores/authStore';
import DashboardHome from '../dashboard/DashboardHome';
import NewUserView from '../questionnaire/NewUserView';
import MatchResults from '../dashboard/MatchResults';
import AdminDashboard from '../admin/AdminDashboard';
import AdminUserEdit from '../admin/AdminUserEdit';
import AdminCreateUser from '../admin/AdminCreateUser';

const AppShell: React.FC = () => {
  const view = useQuestionnaireStore((s) => s.view);
  const isAdmin = useAuthStore((s) => s.isAdmin);

  const renderContent = () => {
    if (isAdmin) {
      switch (view) {
        case 'dashboard':
          return <AdminDashboard />;
        case 'adminEditUser':
          return <AdminUserEdit />;
        case 'adminCreateUser':
          return <AdminCreateUser />;
        case 'newUser':
          return <NewUserView />;
        case 'matched':
          return <MatchResults />;
        default:
          return <AdminDashboard />;
      }
    }

    // Regular user views
    switch (view) {
      case 'dashboard':
        return <DashboardHome />;
      case 'newUser':
        return <NewUserView />;
      case 'matched':
        return <MatchResults />;
      default:
        return <DashboardHome />;
    }
  };

  return (
    <div
      style={{
        display: 'flex',
        height: '100vh',
        fontFamily: "'Inter','Segoe UI',sans-serif",
        background: '#F8FAFC',
        color: '#0F172A',
        overflow: 'hidden',
      }}
    >
      <Sidebar />
      <div
        style={{
          flex: 1,
          display: 'flex',
          flexDirection: 'column',
          overflow: 'hidden',
        }}
      >
        <Topbar />
        <div
          style={{
            flex: 1,
            overflow: 'auto',
            padding: 28,
          }}
        >
          {renderContent()}
        </div>
      </div>
    </div>
  );
};

export default AppShell;
