import type { AccountType } from '../stores/questionnaireStore';

export interface StepConfig {
  label: string;
  shortLabel: string;
  key: string;
}

/** Enterprise-only step flow */
const STEPS: StepConfig[] = [
  { label: 'Contact Information', shortLabel: 'Contact', key: 'contact' },
  { label: 'Account Setup', shortLabel: 'Account', key: 'accountSetup' },
  { label: 'Stage of Development', shortLabel: 'Stage', key: 'stage' },
  { label: 'Entity Type', shortLabel: 'Entity', key: 'entity' },
  { label: 'Pre-Capital Raised', shortLabel: 'Pre-Capital', key: 'preCapital' },
  { label: 'Pre-Market Capital Types', shortLabel: 'Pre-Market', key: 'preMarket' },
  { label: 'Amount of Planned Raise', shortLabel: 'Planned Raise', key: 'plannedRaise' },
  { label: 'Rounds of Capital', shortLabel: 'Rounds', key: 'rounds' },
  { label: 'Use of Funds', shortLabel: 'Use of Funds', key: 'useOfFunds' },
  { label: 'Risk & Capital Cost', shortLabel: 'Risk', key: 'risk' },
  { label: 'Up Front Cost & Timing', shortLabel: 'Cost & Timing', key: 'costTime' },
  { label: 'Documents Prepared', shortLabel: 'Docs Prepared', key: 'documentsPrepared' },
  { label: 'Pre-Rating', shortLabel: 'Pre-Rating', key: 'preRating' },
  { label: 'Lending Information', shortLabel: 'Lending', key: 'lending' },
  { label: 'How Did You Hear About Us', shortLabel: 'Referral', key: 'referral' },
];

export function getStepConfig(_accountType?: AccountType): StepConfig[] {
  return STEPS;
}

export function getTotalSteps(_accountType?: AccountType): number {
  return STEPS.length;
}

export const STEP_CONFIG = STEPS;
export const TOTAL_STEPS = STEPS.length;
