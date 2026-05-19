import api from './client';

export interface Plan {
  slug: string;
  name: string;
  description: string;
  amount_cents: number;
  amount_dollars: number;
  currency: string;
  interval: 'month' | 'year';
  supports_trial: boolean;
  sort_order: number;
}

export interface CreateCheckoutResponse {
  session_id: string;
  checkout_url: string;
}

export interface CheckoutSessionStatus {
  paid: boolean;
  reason?: string;
  already_onboarded?: boolean;
  email?: string;
  company_name?: string;
  plan_slug?: string;
  with_trial?: boolean;
  onboarding_token?: string;
}

export interface OnboardingResponse {
  schema_name: string;
  name: string;
  domain: string | null;
  support_email: string;
  subscription_status: string;
  subscription_plan_slug: string;
}

export async function fetchPlans(): Promise<Plan[]> {
  const { data } = await api.get<Plan[]>('plans/');
  return data;
}

export async function createCheckoutSession(input: {
  plan: 'monthly' | 'yearly';
  with_trial: boolean;
  email: string;
  company_name: string;
}): Promise<CreateCheckoutResponse> {
  const { data } = await api.post<CreateCheckoutResponse>(
    'checkout/create-session/',
    input,
  );
  return data;
}

export async function getCheckoutSessionStatus(
  sessionId: string,
): Promise<CheckoutSessionStatus> {
  const { data } = await api.get<CheckoutSessionStatus>(
    `checkout/session/${encodeURIComponent(sessionId)}/`,
  );
  return data;
}

export interface OnboardTenantInput {
  // Required
  onboarding_token: string;
  schema_name: string;
  company_name: string;
  admin_email: string;
  admin_password: string;
  // Optional branding (mirrors tenants.Client columns). Anything left
  // blank/null is just not sent and the column keeps its default.
  display_name?: string;
  primary_color?: string; // hex like #1f6feb
  accent_color?: string;
  contact_phone?: string;
  signatory_name?: string;
  signatory_title?: string;
  address?: string;
  logo?: File | null;
  favicon?: File | null;
  signature_image?: File | null;
}

export async function onboardTenant(
  input: OnboardTenantInput,
): Promise<OnboardingResponse> {
  // Build a multipart FormData so image fields ride along with the
  // text fields in a single request. Axios sets the correct
  // Content-Type (incl. boundary) automatically when given a FormData.
  const form = new FormData();
  const append = (key: keyof OnboardTenantInput) => {
    const v = input[key];
    if (v === undefined || v === null) return;
    if (typeof v === 'string') {
      if (v.trim() === '') return; // treat blank as "skipped"
      form.append(key, v);
    } else if (v instanceof File) {
      form.append(key, v);
    }
  };

  (
    [
      'onboarding_token',
      'schema_name',
      'company_name',
      'admin_email',
      'admin_password',
      'display_name',
      'primary_color',
      'accent_color',
      'contact_phone',
      'signatory_name',
      'signatory_title',
      'address',
      'logo',
      'favicon',
      'signature_image',
    ] as (keyof OnboardTenantInput)[]
  ).forEach(append);

  const { data } = await api.post<OnboardingResponse>(
    'tenants/onboard/',
    form,
  );
  return data;
}
