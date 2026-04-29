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

/** Redirects unauthenticated users to /login */
function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const token = useAuthStore((s) => s.token);

  if (!token) {
    return <Navigate to="/login" replace />;
  }

  return <>{children}</>;
}

function App() {
  const loadBranding = useBrandingStore((s) => s.load);
  useEffect(() => {
    loadBranding();
  }, [loadBranding]);

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
