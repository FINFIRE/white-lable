import { create } from 'zustand';
import { getTotalSteps } from '../constants/stepConfig';

export type AccountType = 'Enterprise/Business' | 'Intermediary' | 'Capital Market' | null;
type View = 'dashboard' | 'newUser' | 'users' | 'matched' | 'adminEditUser' | 'adminCreateUser';

interface QuestionnaireState {
  currentStep: number;
  completedSteps: Set<number>;
  view: View;
  matchedCapital: string | null;
  matchPdfUrl: string | null;
  animating: boolean;
  accountType: AccountType;
  adminEditUserId: number | null;

  goNext: () => void;
  goPrev: () => void;
  goToStep: (step: number) => void;
  markComplete: (step: number) => void;
  setView: (view: View) => void;
  setMatchedCapital: (capital: string | null) => void;
  setMatchPdfUrl: (url: string | null) => void;
  setAnimating: (v: boolean) => void;
  setAccountType: (type: AccountType) => void;
  setAdminEditUserId: (id: number | null) => void;
  resetQuestionnaire: () => void;
}

export const useQuestionnaireStore = create<QuestionnaireState>((set, get) => ({
  currentStep: 0,
  completedSteps: new Set<number>(),
  view: 'dashboard',
  matchedCapital: null,
  matchPdfUrl: null,
  animating: false,
  accountType: null,
  adminEditUserId: null,

  goNext: () => {
    const total = getTotalSteps(get().accountType);
    set((s) => ({ currentStep: Math.min(s.currentStep + 1, total - 1) }));
  },
  goPrev: () => set((s) => ({ currentStep: Math.max(s.currentStep - 1, 0) })),
  goToStep: (step) => {
    const total = getTotalSteps(get().accountType);
    set({ animating: true });
    setTimeout(
      () =>
        set({
          currentStep: Math.max(0, Math.min(step, total - 1)),
          animating: false,
        }),
      150
    );
  },
  markComplete: (step) =>
    set((s) => {
      const next = new Set(s.completedSteps);
      next.add(step);
      return { completedSteps: next };
    }),
  setView: (view) => set({ view }),
  setMatchedCapital: (capital) => set({ matchedCapital: capital }),
  setMatchPdfUrl: (url) => set({ matchPdfUrl: url }),
  setAnimating: (v) => set({ animating: v }),
  setAccountType: (type) => set({ accountType: type }),
  setAdminEditUserId: (id) => set({ adminEditUserId: id }),
  resetQuestionnaire: () =>
    set({
      currentStep: 0,
      completedSteps: new Set<number>(),
      matchedCapital: null,
      matchPdfUrl: null,
      animating: false,
    }),
}));
