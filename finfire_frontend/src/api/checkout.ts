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

export async function onboardTenant(input: {
  onboarding_token: string;
  schema_name: string;
  company_name: string;
  admin_email: string;
  admin_password: string;
}): Promise<OnboardingResponse> {
  const { data } = await api.post<OnboardingResponse>(
    'tenants/onboard/',
    input,
  );
  return data;
}
