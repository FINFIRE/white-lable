import { useEffect } from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { useAuthStore } from './stores/authStore';
import { useBrandingStore } from './stores/brandingStore';
import LoginPage from './components/auth/LoginPage';
import RegisterPage from './components/auth/RegisterPage';
import ForgotPasswordPage from './components/auth/ForgotPasswordPage';
import ResetPasswordConfirmPage from './components/auth/ResetPasswordConfirmPage';
import ActivateAccountPage from './components/auth/ActivateAccountPage';
import './styles/tailwind.css';

import AppShell from './components/layout/AppShell';

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retry: 1,
      refetchOnWindowFocus: false,
    },
  },
});

/** Redirects unauthenticated users to /login.
 * Waits for the auth store to bootstrap (checkAuth resolved) so
 * isAdmin/user are correct before rendering the shell — otherwise an
 * admin refreshing the page sees the regular-user view for a tick.
 */
function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const token = useAuthStore((s) => s.token);
  const bootstrapped = useAuthStore((s) => s.bootstrapped);

  if (!bootstrapped) {
    return (
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          minHeight: '100vh',
          color: '#64748B',
          fontSize: 14,
        }}
      >
        Loading…
      </div>
    );
  }

  if (!token) {
    return <Navigate to="/login" replace />;
  }

  return <>{children}</>;
}

function App() {
  const loadBranding = useBrandingStore((s) => s.load);
  const checkAuth = useAuthStore((s) => s.checkAuth);
  useEffect(() => {
    loadBranding();
    // Restore user/isAdmin from the persisted token on every page load.
    // Without this, a refresh leaves user=null, isAdmin=false even though
    // the token is still valid, and the shell renders the wrong view.
    checkAuth();
  }, [loadBranding, checkAuth]);

  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/forgot-password" element={<ForgotPasswordPage />} />
          <Route
            path="/resetPasswordConfirm/:uid/:token"
            element={<ResetPasswordConfirmPage />}
          />
          <Route
            path="/userActivate/:uid/:token"
            element={<ActivateAccountPage />}
          />

          {/* All authenticated routes go through ProtectedRoute */}
          <Route
            path="/*"
            element={
              <ProtectedRoute>
                <AppShell />
              </ProtectedRoute>
            }
          />
        </Routes>
      </BrowserRouter>
    </QueryClientProvider>
  );
}

export default App;
