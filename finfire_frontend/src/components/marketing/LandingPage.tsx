import { Link } from 'react-router-dom';

/**
 * Marketing landing page rendered at "/" on the public host (no tenant
 * resolved). Tenant subdomains skip this entirely — see App.tsx
 * HomeOrShell wrapper. Copy is intentionally placeholder; swap out the
 * arrays below (HERO, FEATURES, STEPS, FAQ) when you have final wording.
 */

const PLATFORM_NAME = 'FINFIRE';
const SUPPORT_EMAIL = 'hello@finfire.com';

const FEATURES = [
  {
    title: 'AI-driven matching algorithm',
    body:
      'Over 100 capital types weighted across 14 signals. Every match is explained, scored, and exportable as a branded letter.',
  },
  {
    title: 'Fully white-labeled',
    body:
      'Your brand, your logo, your colors, your domain. The platform fades into the background so your clients see your firm.',
  },
  {
    title: 'Multi-tenant by design',
    body:
      'Each customer lives in their own isolated Postgres schema. Data never crosses between firms — that part is enforced at the database level.',
  },
  {
    title: 'PDF reports out of the box',
    body:
      'Match letters, $499 follow-up reports, and Truth-in-Capital spreadsheets, all generated automatically and branded with your colors.',
  },
];

const STEPS = [
  {
    n: '01',
    title: 'Pick a plan',
    body: 'Start with a 7-day free trial. Cancel before day 7 at no charge.',
  },
  {
    n: '02',
    title: 'Claim your subdomain',
    body:
      'Type the name your clients will use — yourfirm.appfinfire.com. You can change branding any time.',
  },
  {
    n: '03',
    title: 'Onboard clients, run matches',
    body:
      'Invite enterprise clients, have them complete the 14-step questionnaire, and the platform returns a ranked match with a downloadable report.',
  },
];

const FAQ = [
  {
    q: 'What does the 7-day free trial include?',
    a:
      'Full access to every feature for seven days. We collect a card up front and convert to the monthly plan ($40/mo) automatically on day 7 unless you cancel from your admin panel.',
  },
  {
    q: 'How long does setup take?',
    a:
      'About 5 minutes for the basics — pick a subdomain, set your admin password, and you can start onboarding clients. Adding your logo, signature image, and brand colors usually adds another 10 minutes.',
  },
  {
    q: 'Can I cancel anytime?',
    a:
      'Yes. Cancel from your tenant admin panel and you’ll keep access through the end of the current billing period. No support tickets required.',
  },
  {
    q: 'Is my data isolated from other firms?',
    a:
      'Yes. Every tenant gets its own Postgres schema, every request is routed through schema-aware middleware, and admin tooling is locked down so tenant admins only see their own data.',
  },
  {
    q: 'Do you offer a partnership or volume plan?',
    a: `Email ${SUPPORT_EMAIL} and we'll set up a call.`,
  },
];

const LandingPage: React.FC = () => {
  return (
    <div className="min-h-screen bg-white text-slate-900">
      <Nav />
      <Hero />
      <Features />
      <HowItWorks />
      <CTABanner />
      <FAQSection />
      <Footer />
    </div>
  );
};

// ── Nav ─────────────────────────────────────────────────────────────

const Nav: React.FC = () => (
  <nav className="sticky top-0 z-30 border-b border-slate-200 bg-white/80 backdrop-blur">
    <div className="mx-auto max-w-6xl px-6 py-4 flex items-center justify-between">
      <Link to="/" className="flex items-center gap-2 font-bold text-lg tracking-tight">
        <span className="inline-block h-7 w-7 rounded-md bg-gradient-to-br from-primary-500 to-primary-700" />
        {PLATFORM_NAME}
      </Link>
      <div className="flex items-center gap-1 sm:gap-4 text-sm">
        <a href="#features" className="hidden sm:inline px-3 py-2 text-slate-600 hover:text-slate-900">
          Features
        </a>
        <a href="#how" className="hidden sm:inline px-3 py-2 text-slate-600 hover:text-slate-900">
          How it works
        </a>
        <a href="#faq" className="hidden sm:inline px-3 py-2 text-slate-600 hover:text-slate-900">
          FAQ
        </a>
        <Link
          to="/pricing"
          className="rounded-lg bg-primary-600 px-4 py-2 text-white text-sm font-semibold hover:bg-primary-700"
        >
          Get started
        </Link>
      </div>
    </div>
  </nav>
);

// ── Hero ────────────────────────────────────────────────────────────

const Hero: React.FC = () => (
  <header className="relative overflow-hidden">
    <div className="absolute inset-0 -z-10 bg-gradient-to-br from-primary-50 via-white to-primary-100" />
    <div className="mx-auto max-w-6xl px-6 py-20 sm:py-28">
      <div className="max-w-3xl">
        <span className="inline-flex items-center gap-2 rounded-full bg-primary-100 px-3 py-1 text-xs font-semibold text-primary-700">
          <span className="h-1.5 w-1.5 rounded-full bg-primary-500" />
          New: 7-day free trial — card required, cancel anytime
        </span>
        <h1 className="mt-6 text-4xl sm:text-5xl font-bold tracking-tight leading-tight">
          The capital-matching platform for{' '}
          <span className="text-primary-600">modern advisory firms</span>
        </h1>
        <p className="mt-5 text-lg text-slate-600 max-w-2xl">
          Stand up your own white-labeled capital-matching service in minutes.
          Match enterprise clients to the right capital source in days — not
          months — with an AI-driven algorithm and ready-to-send PDF reports.
        </p>
        <div className="mt-8 flex flex-wrap gap-3">
          <Link
            to="/pricing"
            className="inline-flex items-center justify-center rounded-lg bg-primary-600 px-6 py-3 text-white font-semibold hover:bg-primary-700"
          >
            See pricing →
          </Link>
          <a
            href="#features"
            className="inline-flex items-center justify-center rounded-lg border border-primary-600 px-6 py-3 text-primary-700 font-semibold hover:bg-primary-50"
          >
            How it works
          </a>
        </div>
        <p className="mt-4 text-xs text-slate-500">
          Already a customer? Sign in at <code>your-firm.appfinfire.com</code>.
        </p>
      </div>
    </div>
  </header>
);

// ── Features ────────────────────────────────────────────────────────

const Features: React.FC = () => (
  <section id="features" className="py-20 sm:py-24">
    <div className="mx-auto max-w-6xl px-6">
      <div className="text-center max-w-2xl mx-auto">
        <p className="text-sm font-semibold uppercase tracking-wide text-primary-600">
          What you get
        </p>
        <h2 className="mt-2 text-3xl sm:text-4xl font-bold tracking-tight">
          Built for the firms that match capital
        </h2>
        <p className="mt-4 text-slate-600">
          Four things that take months to build in-house, available the day you
          finish onboarding.
        </p>
      </div>
      <div className="mt-12 grid gap-6 md:grid-cols-2">
        {FEATURES.map((f) => (
          <article
            key={f.title}
            className="rounded-2xl border border-slate-200 bg-white p-6 hover:border-primary-300 hover:shadow-sm transition-all"
          >
            <div className="flex items-start gap-4">
              <div className="flex h-10 w-10 flex-shrink-0 items-center justify-center rounded-lg bg-primary-100">
                <span className="h-2.5 w-2.5 rounded-full bg-primary-500" />
              </div>
              <div>
                <h3 className="text-lg font-semibold">{f.title}</h3>
                <p className="mt-1 text-slate-600">{f.body}</p>
              </div>
            </div>
          </article>
        ))}
      </div>
    </div>
  </section>
);

// ── How it works ────────────────────────────────────────────────────

const HowItWorks: React.FC = () => (
  <section id="how" className="py-20 sm:py-24 bg-slate-50">
    <div className="mx-auto max-w-6xl px-6">
      <div className="text-center max-w-2xl mx-auto">
        <p className="text-sm font-semibold uppercase tracking-wide text-primary-600">
          How it works
        </p>
        <h2 className="mt-2 text-3xl sm:text-4xl font-bold tracking-tight">
          Three steps from signup to first match
        </h2>
      </div>
      <ol className="mt-12 grid gap-6 md:grid-cols-3">
        {STEPS.map((s) => (
          <li
            key={s.n}
            className="rounded-2xl border border-slate-200 bg-white p-6"
          >
            <div className="text-sm font-bold text-primary-600">{s.n}</div>
            <h3 className="mt-2 text-lg font-semibold">{s.title}</h3>
            <p className="mt-2 text-slate-600">{s.body}</p>
          </li>
        ))}
      </ol>
    </div>
  </section>
);

// ── CTA banner ──────────────────────────────────────────────────────

const CTABanner: React.FC = () => (
  <section className="py-20">
    <div className="mx-auto max-w-4xl px-6">
      <div className="rounded-2xl bg-gradient-to-br from-primary-600 to-primary-800 px-8 py-12 text-center text-white shadow-lg">
        <h2 className="text-3xl font-bold tracking-tight">
          Try it free for 7 days
        </h2>
        <p className="mt-3 text-primary-100 max-w-xl mx-auto">
          Card required, no charge during the trial. Cancel anytime from your
          admin panel before day 7.
        </p>
        <Link
          to="/pricing"
          className="mt-6 inline-flex items-center justify-center rounded-lg bg-white px-6 py-3 text-primary-700 font-semibold hover:bg-primary-50"
        >
          Start your free trial →
        </Link>
      </div>
    </div>
  </section>
);

// ── FAQ ─────────────────────────────────────────────────────────────

const FAQSection: React.FC = () => (
  <section id="faq" className="py-20 sm:py-24 bg-slate-50">
    <div className="mx-auto max-w-3xl px-6">
      <div className="text-center max-w-2xl mx-auto">
        <p className="text-sm font-semibold uppercase tracking-wide text-primary-600">
          FAQ
        </p>
        <h2 className="mt-2 text-3xl sm:text-4xl font-bold tracking-tight">
          Common questions
        </h2>
      </div>
      <div className="mt-10 space-y-3">
        {FAQ.map((item) => (
          <details
            key={item.q}
            className="group rounded-xl border border-slate-200 bg-white p-5 open:shadow-sm"
          >
            <summary className="cursor-pointer list-none flex items-center justify-between font-semibold">
              <span>{item.q}</span>
              <span className="ml-4 text-primary-500 transition-transform group-open:rotate-45">
                +
              </span>
            </summary>
            <p className="mt-3 text-slate-600">{item.a}</p>
          </details>
        ))}
      </div>
    </div>
  </section>
);

// ── Footer ──────────────────────────────────────────────────────────

const Footer: React.FC = () => (
  <footer className="border-t border-slate-200 bg-white">
    <div className="mx-auto max-w-6xl px-6 py-10 flex flex-col sm:flex-row justify-between items-start gap-6 text-sm text-slate-500">
      <div>
        <div className="flex items-center gap-2 font-bold text-slate-900">
          <span className="inline-block h-6 w-6 rounded-md bg-gradient-to-br from-primary-500 to-primary-700" />
          {PLATFORM_NAME}
        </div>
        <p className="mt-2 max-w-xs">
          The capital-matching platform for advisory firms. Built with secure
          multi-tenancy and full white-labeling.
        </p>
      </div>
      <div className="flex flex-wrap gap-x-8 gap-y-2">
        <Link to="/pricing" className="hover:text-slate-900">
          Pricing
        </Link>
        <a href="#features" className="hover:text-slate-900">
          Features
        </a>
        <a href="#faq" className="hover:text-slate-900">
          FAQ
        </a>
        <a href={`mailto:${SUPPORT_EMAIL}`} className="hover:text-slate-900">
          {SUPPORT_EMAIL}
        </a>
      </div>
    </div>
    <div className="border-t border-slate-100">
      <div className="mx-auto max-w-6xl px-6 py-4 text-xs text-slate-400 flex flex-col sm:flex-row justify-between gap-2">
        <span>© {new Date().getFullYear()} {PLATFORM_NAME}. All rights reserved.</span>
        <span>
          Existing customers sign in at <code>your-firm.appfinfire.com</code>.
        </span>
      </div>
    </div>
  </footer>
);

export default LandingPage;
