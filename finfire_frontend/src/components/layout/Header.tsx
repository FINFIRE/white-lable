import React from 'react';
import { LogOut } from 'lucide-react';
import { useAuthStore } from '../../stores/authStore';
import BrandLogo from './BrandLogo';

const Header: React.FC = () => {
  const user = useAuthStore((s) => s.user);
  const logout = useAuthStore((s) => s.logout);

  return (
    <header className="flex h-[60px] items-center justify-between border-b border-gray-200 bg-white px-6 shadow-sm">
      {/* Logo */}
      <BrandLogo className="h-8 w-auto" />

      {/* User info + logout */}
      <div className="flex items-center gap-4">
        {user && (
          <span className="text-sm font-medium text-slate-900">
            {user.username}
          </span>
        )}
        <button
          onClick={() => logout()}
          className="inline-flex items-center gap-1.5 rounded-lg px-3 py-1.5 text-sm text-gray-500 transition-colors hover:bg-gray-100 hover:text-slate-900"
        >
          <LogOut className="h-4 w-4" />
          Logout
        </button>
      </div>
    </header>
  );
};

export default Header;
