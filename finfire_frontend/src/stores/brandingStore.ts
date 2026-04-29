import { create } from 'zustand';
import { fetchBranding, type TenantBranding } from '../api/branding';

interface BrandingState {
  branding: TenantBranding | null;
  loaded: boolean;
  load: () => Promise<void>;
}

export const useBrandingStore = create<BrandingState>((set, get) => ({
  branding: null,
  loaded: false,
  load: async () => {
    if (get().loaded) return;
    const branding = await fetchBranding();
    set({ branding, loaded: true });
    applyBrandingToDocument(branding);
  },
}));

function applyBrandingToDocument(branding: TenantBranding | null) {
  if (!branding) return;

  if (branding.display_name || branding.name) {
    document.title = branding.display_name || branding.name;
  }

  if (branding.favicon) {
    let link = document.querySelector<HTMLLinkElement>("link[rel~='icon']");
    if (!link) {
      link = document.createElement('link');
      link.rel = 'icon';
      document.head.appendChild(link);
    }
    link.href = branding.favicon;
  }

  const root = document.documentElement;
  if (branding.primary_color) {
    root.style.setProperty('--brand-primary', branding.primary_color);
  }
  if (branding.accent_color) {
    root.style.setProperty('--brand-accent', branding.accent_color);
  }
}
