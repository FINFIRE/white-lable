import React from 'react';
import { useBrandingStore } from '../../stores/brandingStore';

interface BrandLogoProps {
  className?: string;
  fallbackSrc?: string;
  fallbackAlt?: string;
}

/** Renders the active tenant's logo, falling back to the bundled default. */
const BrandLogo: React.FC<BrandLogoProps> = ({
  className,
  fallbackSrc = '/logo.png',
  fallbackAlt = 'FINFIRE',
}) => {
  const branding = useBrandingStore((s) => s.branding);
  const src = branding?.logo || fallbackSrc;
  const alt = branding?.display_name || branding?.name || fallbackAlt;
  return <img src={src} alt={alt} className={className} />;
};

export default BrandLogo;
