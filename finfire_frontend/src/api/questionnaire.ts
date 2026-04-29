import api from './client';
import type {
  ContactData,
  StageData,
  EntityData,
  PreCapitalData,
  PreMarketData,
  PlannedRaiseData,
  RoundsData,
  UseOfFundsData,
  RiskData,
  CostTimeData,
  PreRatingData,
  ReferralData,
  DocumentsPreparedData,
  AccountData,
} from '../types/api';

/**
 * The backend ViewSet list() returns an array. For non-admin users this is
 * always a single-element array. Unwrap it so components always get an object.
 */
function unwrap<T>(data: T | T[]): T {
  return Array.isArray(data) ? data[0] : data;
}

// Step 1 - Contact Information
export async function getContact(): Promise<ContactData> {
  const { data } = await api.get<ContactData | ContactData[]>('contact');
  return unwrap(data);
}

export async function postContact(payload: ContactData): Promise<ContactData> {
  const { data } = await api.post<ContactData>('contact', payload);
  return data;
}

// Account Setup
export async function getAccountSetup(): Promise<AccountData> {
  const { data } = await api.get<AccountData | AccountData[]>('account');
  return unwrap(data);
}

export async function postAccountSetup(payload: AccountData): Promise<AccountData> {
  const { data } = await api.post<AccountData>('account', payload);
  return data;
}

// Step 2 - Stage of Development
export async function getStage(): Promise<StageData> {
  const { data } = await api.get<StageData | StageData[]>('stage');
  return unwrap(data);
}

export async function postStage(payload: StageData): Promise<StageData> {
  const { data } = await api.post<StageData>('stage', payload);
  return data;
}

// Step 3 - Entity Type
export async function getEntity(): Promise<EntityData> {
  const { data } = await api.get<EntityData | EntityData[]>('entity');
  return unwrap(data);
}

export async function postEntity(payload: EntityData): Promise<EntityData> {
  const { data } = await api.post<EntityData>('entity', payload);
  return data;
}

// Step 4 - Pre-Capital Raised
export async function getPreCapital(): Promise<PreCapitalData> {
  const { data } = await api.get<PreCapitalData | PreCapitalData[]>('pre-capital');
  return unwrap(data);
}

export async function postPreCapital(
  payload: PreCapitalData
): Promise<PreCapitalData> {
  const { data } = await api.post<PreCapitalData>('pre-capital', payload);
  return data;
}

// Step 5 - Pre-Market Capital Types
export async function getPreMarket(): Promise<PreMarketData> {
  const { data } = await api.get<PreMarketData | PreMarketData[]>('pre-market');
  return unwrap(data);
}

export async function postPreMarket(
  payload: PreMarketData
): Promise<PreMarketData> {
  const { data } = await api.post<PreMarketData>('pre-market', payload);
  return data;
}

// Step 6 - Amount of Planned Raise
export async function getPlannedRaise(): Promise<PlannedRaiseData> {
  const { data } = await api.get<PlannedRaiseData | PlannedRaiseData[]>('planned-raise');
  return unwrap(data);
}

export async function postPlannedRaise(
  payload: PlannedRaiseData
): Promise<PlannedRaiseData> {
  const { data } = await api.post<PlannedRaiseData>('planned-raise', payload);
  return data;
}

// Step 7 - Rounds of Capital
export async function getRounds(): Promise<RoundsData> {
  const { data } = await api.get<RoundsData | RoundsData[]>('rounds');
  return unwrap(data);
}

export async function postRounds(payload: RoundsData): Promise<RoundsData> {
  const { data } = await api.post<RoundsData>('rounds', payload);
  return data;
}

// Step 8 - Use of Funds
export async function getUseOfFunds(): Promise<UseOfFundsData> {
  const { data } = await api.get<UseOfFundsData | UseOfFundsData[]>('use-of-funds');
  return unwrap(data);
}

export async function postUseOfFunds(
  payload: UseOfFundsData
): Promise<UseOfFundsData> {
  const { data } = await api.post<UseOfFundsData>('use-of-funds', payload);
  return data;
}

// Step 9 - Risk & Capital Cost
export async function getRisk(): Promise<RiskData> {
  const { data } = await api.get<RiskData | RiskData[]>('risk-assesments');
  return unwrap(data);
}

export async function postRisk(payload: RiskData): Promise<RiskData> {
  const { data } = await api.post<RiskData>('risk-assesments', payload);
  return data;
}

// Step 10 - Up Front Cost & Timing
export async function getCostTime(): Promise<CostTimeData> {
  const { data } = await api.get<CostTimeData | CostTimeData[]>('cost-time');
  return unwrap(data);
}

export async function postCostTime(
  payload: CostTimeData
): Promise<CostTimeData> {
  const { data } = await api.post<CostTimeData>('cost-time', payload);
  return data;
}

// Documents Prepared (boolean checklist) — /api/all-documents
export async function getDocsPrepared(): Promise<DocumentsPreparedData> {
  const { data } = await api.get<DocumentsPreparedData | DocumentsPreparedData[]>('all-documents');
  return unwrap(data);
}

export async function postDocsPrepared(
  payload: DocumentsPreparedData
): Promise<DocumentsPreparedData> {
  const { data } = await api.post<DocumentsPreparedData>('all-documents', payload);
  return data;
}

// Pre-Rating (JSON ratings)
export async function getPreRating(): Promise<PreRatingData> {
  const { data } = await api.get<PreRatingData | PreRatingData[]>('pre-rating');
  return unwrap(data);
}

export async function postPreRating(
  payload: PreRatingData
): Promise<PreRatingData> {
  const { data } = await api.post<PreRatingData>('pre-rating', payload);
  return data;
}

// Referral
export async function getReferral(): Promise<ReferralData> {
  const { data } = await api.get<ReferralData | ReferralData[]>('referal-response');
  return unwrap(data);
}

export async function postReferral(
  payload: ReferralData
): Promise<ReferralData> {
  const { data } = await api.post<ReferralData>('referal-response', payload);
  return data;
}
