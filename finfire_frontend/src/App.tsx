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
import PricingPage from './components/marketing/PricingPage';
import CheckoutSuccessPage from './components/marketing/CheckoutSuccessPage';
import LandingPage from './components/marketing/LandingPage';
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

/** Loading placeholder shown while branding + auth bootstrap resolve. */
function BootstrapFiller() {
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

/** Picks what to render at "/":
 *   - Public host (no tenant resolved -> branding stays null after the
 *     /api/branding/ 404) -> marketing LandingPage.
 *   - Tenant subdomain, not authenticated -> redirect to /login.
 *   - Tenant subdomain, authenticated -> AppShell.
 * Waits for both `bootstrapped` (auth) and `loaded` (branding) before
 * deciding, so we don't flash the wrong UI on cold load.
 */
function HomeOrShell() {
  const bootstrapped = useAuthStore((s) => s.bootstrapped);
  const token = useAuthStore((s) => s.token);
  const brandingLoaded = useBrandingStore((s) => s.loaded);
  const branding = useBrandingStore((s) => s.branding);

  if (!bootstrapped || !brandingLoaded) {
    return <BootstrapFiller />;
  }

  // Public host: no tenant resolved -> marketing site.
  if (!branding) {
    return <LandingPage />;
  }

  // Tenant host: gate on the auth token.
  if (!token) {
    return <Navigate to="/login" replace />;
  }
  return <AppShell />;
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

          {/* Public marketing + Stripe-driven onboarding routes.
              Reachable without authentication so prospects can buy. */}
          <Route path="/pricing" element={<PricingPage />} />
          <Route path="/checkout/success" element={<CheckoutSuccessPage />} />

          {/* "/" routes to the marketing site on the public host and
              the protected app shell on tenant subdomains. The decision
              is host-driven via the branding store. */}
          <Route path="/*" element={<HomeOrShell />} />
        </Routes>
      </BrowserRouter>
    </QueryClientProvider>
  );
}

export default App;
