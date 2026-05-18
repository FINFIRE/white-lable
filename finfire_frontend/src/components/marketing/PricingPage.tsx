import { useEffect, useState } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';
import axios from 'axios';
import {
  createCheckoutSession,
  fetchPlans,
  type Plan,
} from '../../api/checkout';
import LoadingSpinner from '../ui/LoadingSpinner';

/**
 * Three-card pricing layout that drives the marketing -> Checkout funnel.
 * Visible on the public host (no tenant resolved). Cards:
 *  - "Free 7-day trial"  -> monthly plan, with_trial=true
 *  - "Monthly"           -> monthly plan, no trial
 *  - "Yearly"            -> yearly plan, no trial
 * Click -> backend creates a Stripe Checkout Session and we redirect
 * the browser to the hosted Checkout URL.
 */
type Tier = {
  id: 'trial' | 'monthly' | 'yearly';
  highlightLabel?: string;
  buttonLabel: string;
  // Returns the (plan_slug, with_trial) the backend expects.
  resolve: (plans: Plan[]) => { plan: 'monthly' | 'yearly'; with_trial: boolean } | null;
  cardTitle: string;
  cardSubtitle: string;
  features: string[];
};

const TIERS: Tier[] = [
  {
    id: 'trial',
    highlightLabel: 'Recommended',
    buttonLabel: 'Start 7-day free trial',
    cardTitle: '7-Day Free Trial',
    cardSubtitle: 'Card required, charged $40/mo after the trial unless canceled.',
    features: [
      'Full access to every feature for 7 days',
      'Automatic conversion to the monthly plan',
      'Cancel anytime before day 7 at no charge',
    ],
    resolve: (plans) => {
      const monthly = plans.find((p) => p.slug === 'monthly');
      if (!monthly || !monthly.supports_trial) return null;
      return { plan: 'monthly', with_trial: true };
    },
  },
  {
    id: 'monthly',
    buttonLabel: 'Subscribe monthly',
    cardTitle: 'Monthly',
    cardSubtitle: 'Pay-as-you-go — cancel anytime from your tenant settings.',
    features: [
      'Full access to every feature',
      'Billed every month',
      'Cancel anytime from the admin panel',
    ],
    resolve: (plans) => {
      const monthly = plans.find((p) => p.slug === 'monthly');
      return monthly ? { plan: 'monthly', with_trial: false } : null;
    },
  },
  {
    id: 'yearly',
    highlightLabel: 'Save 25%',
    buttonLabel: 'Subscribe yearly',
    cardTitle: 'Yearly',
    cardSubtitle: 'Pay once for the year, save $120 vs. monthly.',
    features: [
      'Full access to every feature',
      'Billed annually',
      'Lock in this year’s pricing',
    ],
    resolve: (plans) => {
      const yearly = plans.find((p) => p.slug === 'yearly');
      return yearly ? { plan: 'yearly', with_trial: false } : null;
    },
  },
];

const PricingPage: React.FC = () => {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const [plans, setPlans] = useState<Plan[]>([]);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  // Lead-capture inputs — collected here so we can pass them to Stripe
  // and have the email pre-filled in Checkout.
  const [email, setEmail] = useState('');
  const [companyName, setCompanyName] = useState('');

  const canceled = searchParams.get('canceled') === '1';

  useEffect(() => {
    fetchPlans()
      .then(setPlans)
      .catch(() => setError('Could not load pricing. Please try again later.'))
      .finally(() => setLoading(false));
  }, []);

  const handleSubscribe = async (tier: Tier) => {
    setError(null);

    if (!email.trim()) {
      setError('Please enter your email so we can attach it to your subscription.');
      return;
    }

    const selection = tier.resolve(plans);
    if (!selection) {
      setError('That plan is unavailable right now.');
      return;
    }

    setSubmitting(tier.id);
    try {
      const { checkout_url } = await createCheckoutSession({
        ...selection,
        email: email.trim(),
        company_name: companyName.trim(),
      });
      window.location.href = checkout_url;
    } catch (err) {
      let msg = 'Could not start checkout. Please try again.';
      if (axios.isAxiosError(err)) {
        const detail = err.response?.data?.detail;
        if (typeof detail === 'string') msg = detail;
      }
      setError(msg);
      setSubmitting(null);
    }
  };

  if (loading) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-gradient-to-br from-primary-50 via-white to-primary-100">
        <LoadingSpinner size="lg" />
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-primary-50 via-white to-primary-100 py-16 px-6">
      <div className="mx-auto max-w-6xl">
        <header className="text-center mb-10">
          <p className="text-sm font-semibold uppercase tracking-wide text-primary-600">
            Pricing
          </p>
          <h1 className="mt-2 text-4xl font-bold text-slate-900">
            Pick a plan and start in minutes
          </h1>
          <p className="mt-3 text-base text-slate-600 max-w-2xl mx-auto">
            One subscription gives your whole team access to the capital-matching
            platform on your own branded subdomain.
          </p>
        </header>

        {canceled && (
          <div className="mb-6 mx-auto max-w-2xl rounded-lg border border-amber-200 bg-amber-50 px-4 py-3 text-sm text-amber-800">
            Checkout was canceled. Pick a plan when you’re ready.
          </div>
        )}

        {/* Lead capture */}
        <div className="mx-auto max-w-2xl mb-10 bg-white rounded-2xl shadow-sm border border-slate-200 p-6">
          <div className="grid gap-4 sm:grid-cols-2">
            <div>
              <label htmlFor="lead-email" className="block text-sm font-medium text-slate-900">
                Work email *
              </label>
              <input
                id="lead-email"
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="you@company.com"
                className="mt-1 block w-full rounded-lg border border-slate-300 bg-white px-3 py-2 text-sm focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-200"
              />
            </div>
            <div>
              <label htmlFor="lead-company" className="block text-sm font-medium text-slate-900">
                Company name
              </label>
              <input
                id="lead-company"
                type="text"
                value={companyName}
                onChange={(e) => setCompanyName(e.target.value)}
                placeholder="Acme Capital"
                className="mt-1 block w-full rounded-lg border border-slate-300 bg-white px-3 py-2 text-sm focus:border-primary-500 focus:outline-none focus:ring-2 focus:ring-primary-200"
              />
            </div>
          </div>
        </div>

        {error && (
          <div className="mx-auto max-w-2xl mb-6 rounded-lg border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700">
            {error}
          </div>
        )}

        <div className="grid gap-6 md:grid-cols-3">
          {TIERS.map((tier) => {
            const selection = tier.resolve(plans);
            const targetPlan = selection ? plans.find((p) => p.slug === selection.plan) : null;
            const priceLabel = targetPlan
              ? selection?.with_trial
                ? `$${targetPlan.amount_dollars.toFixed(0)} / mo after trial`
                : `$${targetPlan.amount_dollars.toFixed(0)} / ${targetPlan.interval}`
              : '—';
            const isRecommended = tier.highlightLabel === 'Recommended';
            const cardClass = isRecommended
              ? 'border-primary-500 shadow-lg shadow-primary-200/40 -translate-y-1'
              : 'border-slate-200';

            return (
              <article
                key={tier.id}
                className={`relative rounded-2xl border-2 bg-white p-6 flex flex-col transition-transform ${cardClass}`}
              >
                {tier.highlightLabel && (
                  <span className="absolute -top-3 right-4 rounded-full bg-primary-500 px-3 py-1 text-xs font-semibold text-white shadow">
                    {tier.highlightLabel}
                  </span>
                )}

                <h2 className="text-lg font-semibold text-slate-900">
                  {tier.cardTitle}
                </h2>
                <p className="mt-1 text-sm text-slate-500">{tier.cardSubtitle}</p>

                <div className="mt-5 text-3xl font-bold text-slate-900">
                  {priceLabel}
                </div>

                <ul className="mt-5 space-y-2 text-sm text-slate-700 flex-1">
                  {tier.features.map((f) => (
                    <li key={f} className="flex items-start gap-2">
                      <span className="mt-1 inline-block h-1.5 w-1.5 rounded-full bg-primary-500 flex-shrink-0" />
                      <span>{f}</span>
                    </li>
                  ))}
                </ul>

                <button
                  type="button"
                  onClick={() => handleSubscribe(tier)}
                  disabled={submitting !== null}
                  className={`mt-6 inline-flex items-center justify-center rounded-lg px-4 py-2.5 text-sm font-semibold transition-colors ${
                    isRecommended
                      ? 'bg-primary-600 text-white hover:bg-primary-700 disabled:opacity-60'
                      : 'border border-primary-600 text-primary-700 hover:bg-primary-50 disabled:opacity-60'
                  }`}
                >
                  {submitting === tier.id ? 'Redirecting…' : tier.buttonLabel}
                </button>
              </article>
            );
          })}
        </div>

        <footer className="mt-12 text-center text-xs text-slate-500">
          Payments handled securely by{' '}
          <button
            type="button"
            onClick={() => navigate('/login')}
            className="underline hover:text-slate-700"
          >
            Stripe
          </button>
          . You can cancel anytime from your tenant admin panel.
        </footer>
      </div>
    </div>
  );
};

export default PricingPage;
