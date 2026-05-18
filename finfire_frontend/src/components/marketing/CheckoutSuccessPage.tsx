import { useEffect, useRef, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import axios from 'axios';
import {
  getCheckoutSessionStatus,
  onboardTenant,
  type CheckoutSessionStatus,
  type OnboardingResponse,
} from '../../api/checkout';
import LoadingSpinner from '../ui/LoadingSpinner';

/**
 * Stripe redirects here after a successful Checkout. We:
 *   1. Poll GET /api/checkout/session/<id>/ until the webhook has fired
 *      and minted an onboarding token.
 *   2. Show a tenant-onboarding form (subdomain, admin email, admin
 *      password) pre-filled with what we already know.
 *   3. POST /api/tenants/onboard/ -> Client + Domain + admin user
 *      created. Show success card with the login URL.
 */
const POLL_INTERVAL_MS = 2000;
const POLL_TIMEOUT_MS = 60_000;

const CheckoutSuccessPage: React.FC = () => {
  const [searchParams] = useSearchParams();
  const sessionId = searchParams.get('session_id') || '';

  const [pollState, setPollState] = useState<'polling' | 'ready' | 'already' | 'timeout' | 'error'>(
    sessionId ? 'polling' : 'error',
  );
  const [session, setSession] = useState<CheckoutSessionStatus | null>(null);
  const [errorMsg, setErrorMsg] = useState<string | null>(
    sessionId ? null : 'Missing session_id in the redirect URL.',
  );

  // Onboarding form state
  const [schemaName, setSchemaName] = useState('');
  const [companyName, setCompanyName] = useState('');
  const [adminEmail, setAdminEmail] = useState('');
  const [adminPassword, setAdminPassword] = useState('');
  const [submitting, setSubmitting] = useState(false);
  const [formError, setFormError] = useState<string | null>(null);
  const [onboarded, setOnboarded] = useState<OnboardingResponse | null>(null);

  const pollTimerRef = useRef<number | null>(null);
  const pollStartRef = useRef<number>(Date.now());

  // Poll for the webhook to have created the PendingOnboarding row.
  useEffect(() => {
    if (!sessionId) return;
    let cancelled = false;

    const poll = async () => {
      if (cancelled) return;
      try {
        const status = await getCheckoutSessionStatus(sessionId);
        if (cancelled) return;
        if (status.paid) {
          setSession(status);
          if (status.already_onboarded) {
            setPollState('already');
          } else {
            setPollState('ready');
            // Pre-fill form with what we know from the payment.
            setCompanyName(status.company_name || '');
            setAdminEmail(status.email || '');
            if (status.company_name) {
              setSchemaName(slugify(status.company_name));
            }
          }
          return;
        }
        if (Date.now() - pollStartRef.current > POLL_TIMEOUT_MS) {
          setPollState('timeout');
          return;
        }
        pollTimerRef.current = window.setTimeout(poll, POLL_INTERVAL_MS);
      } catch {
        if (cancelled) return;
        setPollState('error');
        setErrorMsg('Could not check the payment status. Please refresh.');
      }
    };

    poll();
    return () => {
      cancelled = true;
      if (pollTimerRef.current !== null) window.clearTimeout(pollTimerRef.current);
    };
  }, [sessionId]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setFormError(null);
    if (!session?.onboarding_token) {
      setFormError('Missing onboarding token; please refresh the page.');
      return;
    }
    if (!/^[a-z][a-z0-9_-]{1,62}$/.test(schemaName)) {
      setFormError(
        'Subdomain must start with a letter and contain only lower-case letters, digits, hyphens, or underscores.',
      );
      return;
    }
    if (adminPassword.length < 8) {
      setFormError('Password must be at least 8 characters.');
      return;
    }

    setSubmitting(true);
    try {
      const res = await onboardTenant({
        onboarding_token: session.onboarding_token,
        schema_name: schemaName,
        company_name: companyName,
        admin_email: adminEmail,
        admin_password: adminPassword,
      });
      setOnboarded(res);
    } catch (err) {
      let msg = 'Could not create your tenant. Please try again or contact support.';
      if (axios.isAxiosError(err)) {
        const data = err.response?.data;
        if (typeof data === 'string') {
          msg = data;
        } else if (data && typeof data === 'object') {
          const first = Object.entries(data)[0];
          if (first) {
            const [field, value] = first;
            const v = Array.isArray(value) ? value[0] : value;
            msg = field === 'detail' ? String(v) : `${field}: ${v}`;
          }
        }
      }
      setFormError(msg);
    } finally {
      setSubmitting(false);
    }
  };

  // ── Render branches ─────────────────────────────────────────────────

  if (onboarded) {
    const loginUrl = onboarded.domain
      ? `${window.location.protocol}//${onboarded.domain}${
          window.location.port ? `:${window.location.port}` : ''
        }/login`
      : '#';
    return (
      <CenterCard>
        <h1 className="text-2xl font-bold text-slate-900">All set!</h1>
        <p className="mt-2 text-slate-600">
          Your tenant <strong>{onboarded.name}</strong> is ready at{' '}
          <code className="text-primary-700">{onboarded.domain}</code>.
        </p>
        <a
          href={loginUrl}
          className="mt-6 inline-flex items-center justify-center rounded-lg bg-primary-600 px-5 py-2.5 text-sm font-semibold text-white hover:bg-primary-700"
        >
          Go to your login page →
        </a>
        <p className="mt-4 text-xs text-slate-500">
          Log in with <strong>{adminEmail}</strong> and the password you just set.
        </p>
      </CenterCard>
    );
  }

  if (pollState === 'error') {
    return (
      <CenterCard tone="error">
        <h1 className="text-2xl font-bold text-slate-900">Something went wrong</h1>
        <p className="mt-2 text-slate-600">{errorMsg}</p>
      </CenterCard>
    );
  }

  if (pollState === 'timeout') {
    return (
      <CenterCard tone="warning">
        <h1 className="text-2xl font-bold text-slate-900">Still confirming your payment</h1>
        <p className="mt-2 text-slate-600">
          Your card was charged but our system hasn’t received Stripe’s confirmation yet.
          Refresh in a moment, or contact support with session id{' '}
          <code className="text-xs">{sessionId}</code>.
        </p>
      </CenterCard>
    );
  }

  if (pollState === 'already') {
    return (
      <CenterCard tone="info">
        <h1 className="text-2xl font-bold text-slate-900">Already onboarded</h1>
        <p className="mt-2 text-slate-600">
          This payment was already used to create a tenant. Sign in from your subdomain.
        </p>
      </CenterCard>
    );
  }

  if (pollState === 'polling') {
    return (
      <CenterCard>
        <LoadingSpinner size="lg" />
        <p className="mt-4 text-slate-600">Confirming your payment with Stripe…</p>
      </CenterCard>
    );
  }

  // pollState === 'ready' → show the onboarding form
  return (
    <div className="min-h-screen bg-gradient-to-br from-primary-50 via-white to-primary-100 py-12 px-6">
      <div className="mx-auto max-w-xl bg-white rounded-2xl border border-slate-200 shadow-sm p-8">
        <h1 className="text-2xl font-bold text-slate-900">Set up your tenant</h1>
        <p className="mt-2 text-sm text-slate-600">
          Payment confirmed. Just one step left — pick a subdomain and create
          your admin login.
        </p>

        <form onSubmit={handleSubmit} className="mt-6 space-y-5">
          <Field
            label="Subdomain"
            hint="Lower-case letters, digits, hyphens. You’ll log in at <subdomain>.appfinfire.com."
            id="onboard-schema"
          >
            <div className="flex items-stretch">
              <input
                id="onboard-schema"
                value={schemaName}
                onChange={(e) => setSchemaName(e.target.value.toLowerCase())}
                placeholder="acme"
                className="block w-full rounded-l-lg border border-slate-300 bg-white px-3 py-2 text-sm focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-200"
                required
              />
              <span className="inline-flex items-center rounded-r-lg border border-l-0 border-slate-300 bg-slate-50 px-3 text-sm text-slate-500">
                .appfinfire.com
              </span>
            </div>
          </Field>

          <Field label="Company name" id="onboard-company">
            <input
              id="onboard-company"
              value={companyName}
              onChange={(e) => setCompanyName(e.target.value)}
              className="block w-full rounded-lg border border-slate-300 bg-white px-3 py-2 text-sm focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-200"
              required
            />
          </Field>

          <Field label="Admin email" id="onboard-email">
            <input
              id="onboard-email"
              type="email"
              value={adminEmail}
              onChange={(e) => setAdminEmail(e.target.value)}
              className="block w-full rounded-lg border border-slate-300 bg-white px-3 py-2 text-sm focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-200"
              required
            />
          </Field>

          <Field
            label="Admin password"
            id="onboard-password"
            hint="Minimum 8 characters. You’ll use this to log in."
          >
            <input
              id="onboard-password"
              type="password"
              value={adminPassword}
              onChange={(e) => setAdminPassword(e.target.value)}
              className="block w-full rounded-lg border border-slate-300 bg-white px-3 py-2 text-sm focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-200"
              minLength={8}
              required
            />
          </Field>

          {formError && (
            <div className="rounded-lg border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
              {formError}
            </div>
          )}

          <button
            type="submit"
            disabled={submitting}
            className="w-full inline-flex items-center justify-center rounded-lg bg-primary-600 px-4 py-2.5 text-sm font-semibold text-white hover:bg-primary-700 disabled:opacity-60"
          >
            {submitting ? 'Creating your tenant…' : 'Create my tenant'}
          </button>
        </form>
      </div>
    </div>
  );
};

// ── Tiny shared helpers ──────────────────────────────────────────────

function slugify(s: string): string {
  return s
    .toLowerCase()
    .replace(/[^a-z0-9-_ ]/g, '')
    .trim()
    .replace(/\s+/g, '-')
    .slice(0, 63);
}

const CenterCard: React.FC<{
  tone?: 'error' | 'warning' | 'info';
  children: React.ReactNode;
}> = ({ tone, children }) => {
  const toneClass =
    tone === 'error'
      ? 'border-red-200'
      : tone === 'warning'
        ? 'border-amber-200'
        : tone === 'info'
          ? 'border-blue-200'
          : 'border-slate-200';
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-primary-50 via-white to-primary-100 px-6">
      <div className={`max-w-md rounded-2xl border-2 bg-white p-8 text-center shadow-sm ${toneClass}`}>
        {children}
      </div>
    </div>
  );
};

const Field: React.FC<{
  label: string;
  id: string;
  hint?: string;
  children: React.ReactNode;
}> = ({ label, id, hint, children }) => (
  <div>
    <label htmlFor={id} className="block text-sm font-medium text-slate-900">
      {label}
    </label>
    <div className="mt-1">{children}</div>
    {hint && <p className="mt-1 text-xs text-slate-500">{hint}</p>}
  </div>
);

export default CheckoutSuccessPage;
