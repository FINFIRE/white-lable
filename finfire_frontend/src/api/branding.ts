import api from './client';

export interface TenantBranding {
  schema_name: string;
  name: string;
  display_name: string;
  domain: string | null;
  logo: string | null;
  favicon: string | null;
  primary_color: string;
  accent_color: string;
  support_email: string;
  contact_phone: string;
  signature_image: string | null;
  signatory_name: string;
}

export async function fetchBranding(): Promise<TenantBranding | null> {
  try {
    const { data } = await api.get<TenantBranding>('branding/');
    return data;
  } catch {
    return null;
  }
}
