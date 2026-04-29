import { create } from 'zustand';
import * as authApi from '../api/auth';
import { getAccount } from '../api/connections';
import { useQuestionnaireStore } from './questionnaireStore';

interface User {
  username: string;
  email: string;
}

interface AuthState {
  token: string | null;
  user: User | null;
  isAdmin: boolean;

  login: (username: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
  checkAuth: () => Promise<void>;
}

export const useAuthStore = create<AuthState>((set, get) => ({
  token: localStorage.getItem('finfire_token'),
  user: null,
  isAdmin: false,

  login: async (username: string, password: string) => {
    const { auth_token } = await authApi.login(username, password);
    localStorage.setItem('finfire_token', auth_token);
    set({ token: auth_token });

    // Fetch user profile after login
    await get().checkAuth();
  },

  logout: async () => {
    try {
      await authApi.logout();
    } catch {
      // Token may already be invalid; proceed with local cleanup
    }
    localStorage.removeItem('finfire_token');
    set({ token: null, user: null, isAdmin: false });
    useQuestionnaireStore.getState().setAccountType(null);
  },

  checkAuth: async () => {
    const token = get().token;
    if (!token) {
      set({ user: null, isAdmin: false });
      return;
    }
    try {
      const user = await authApi.getCurrentUser();
      set({
        user: { username: user.username, email: user.email },
        isAdmin: user.is_staff ?? false,
      });

      // Try to restore account type from backend
      try {
        const account = await getAccount();
        if (account?.primaryAppUse?.length > 0) {
          // Account type is derived from the account endpoint existing
          // The actual account type comes from a separate field not exposed yet,
          // but having account data means they completed setup
          const qStore = useQuestionnaireStore.getState();
          if (!qStore.accountType) {
            // Default to Enterprise if account exists but type unknown
            qStore.setAccountType('Enterprise/Business');
          }
        }
      } catch {
        // Account not set up yet — that's fine
      }
    } catch {
      localStorage.removeItem('finfire_token');
      set({ token: null, user: null, isAdmin: false });
    }
  },
}));
