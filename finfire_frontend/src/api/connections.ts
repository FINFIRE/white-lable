import api from './client';
import type {
  AccountData,
  DocumentsPreparedData,
  DocumentsDetailData,
  FinancialsData,
  MarketingData,
  PeopleCultureData,
  LegalRiskData,
  NaicsData,
  IntermediaryQ1Data,
  IntermediaryQ2Data,
  VendorQ1Data,
  PayloadData,
  LendingData,
} from '../types/api';

/**
 * The backend ViewSet list() returns an array. For non-admin users this is
 * always a single-element array. Unwrap it so components always get an object.
 */
function unwrap<T>(data: T | T[]): T {
  return Array.isArray(data) ? data[0] : data;
}

// Account Setup
export async function getAccount(): Promise<AccountData> {
  const { data } = await api.get<AccountData | AccountData[]>('account');
  return unwrap(data);
}

export async function postAccount(payload: AccountData): Promise<AccountData> {
  const { data } = await api.post<AccountData>('account', payload);
  return data;
}

// All Documents Prepared (boolean checklist)
export async function getAllDocuments(): Promise<DocumentsPreparedData> {
  const { data } = await api.get<DocumentsPreparedData | DocumentsPreparedData[]>('all-documents');
  return unwrap(data);
}

export async function postAllDocuments(
  payload: DocumentsPreparedData
): Promise<DocumentsPreparedData> {
  const { data } = await api.post<DocumentsPreparedData>(
    'all-documents',
    payload
  );
  return data;
}

// Documents Prepared Details
export async function getDocumentsPrepared(): Promise<DocumentsDetailData> {
  const { data } = await api.get<DocumentsDetailData | DocumentsDetailData[]>('documents-prepared');
  return unwrap(data);
}

export async function postDocumentsPrepared(
  payload: DocumentsDetailData
): Promise<DocumentsDetailData> {
  const { data } = await api.post<DocumentsDetailData>(
    'documents-prepared',
    payload
  );
  return data;
}

// Financials Prepared
export async function getFinancials(): Promise<FinancialsData> {
  const { data } = await api.get<FinancialsData | FinancialsData[]>('financials-prepared');
  return unwrap(data);
}

export async function postFinancials(
  payload: FinancialsData
): Promise<FinancialsData> {
  const { data } = await api.post<FinancialsData>(
    'financials-prepared',
    payload
  );
  return data;
}

// Marketing & Presentation
export async function getMarketing(): Promise<MarketingData> {
  const { data } = await api.get<MarketingData | MarketingData[]>('marketing-and-presentation');
  return unwrap(data);
}

export async function postMarketing(
  payload: MarketingData
): Promise<MarketingData> {
  const { data } = await api.post<MarketingData>(
    'marketing-and-presentation',
    payload
  );
  return data;
}

// People & Culture
export async function getPeopleCulture(): Promise<PeopleCultureData> {
  const { data } = await api.get<PeopleCultureData | PeopleCultureData[]>('people-and-culture');
  return unwrap(data);
}

export async function postPeopleCulture(
  payload: PeopleCultureData
): Promise<PeopleCultureData> {
  const { data } = await api.post<PeopleCultureData>(
    'people-and-culture',
    payload
  );
  return data;
}

// Legal, Offering & Risk
export async function getLegalRisk(): Promise<LegalRiskData> {
  const { data } = await api.get<LegalRiskData | LegalRiskData[]>('legal-offering-risk');
  return unwrap(data);
}

export async function postLegalRisk(
  payload: LegalRiskData
): Promise<LegalRiskData> {
  const { data } = await api.post<LegalRiskData>(
    'legal-offering-risk',
    payload
  );
  return data;
}

// NAICS / Industry
export async function getNaics(): Promise<NaicsData> {
  const { data } = await api.get<NaicsData | NaicsData[]>('naics');
  return unwrap(data);
}

export async function postNaics(payload: NaicsData): Promise<NaicsData> {
  const { data } = await api.post<NaicsData>('naics', payload);
  return data;
}

// Intermediary Questions (POST only — CreateAPIView on backend)
export async function postIntermediaryQ1(
  payload: IntermediaryQ1Data
): Promise<IntermediaryQ1Data> {
  const { data } = await api.post<IntermediaryQ1Data>(
    'iquestion-one',
    payload
  );
  return data;
}

export async function postIntermediaryQ2(
  payload: IntermediaryQ2Data
): Promise<IntermediaryQ2Data> {
  const { data } = await api.post<IntermediaryQ2Data>(
    'iquestion-two',
    payload
  );
  return data;
}

// Capital Market Vendor Question (POST only — CreateAPIView on backend)
export async function postVendorQ1(
  payload: VendorQ1Data
): Promise<VendorQ1Data> {
  const { data } = await api.post<VendorQ1Data>('vquestion-one', payload);
  return data;
}

// Payload String (webhook trigger)
export async function getPayload(): Promise<PayloadData> {
  const { data } = await api.get<PayloadData | PayloadData[]>('pay-load-string');
  return unwrap(data);
}

export async function postPayload(
  payload: PayloadData
): Promise<PayloadData> {
  const { data } = await api.post<PayloadData>('pay-load-string', payload);
  return data;
}

// Lending Information
export async function getLending(): Promise<LendingData> {
  const { data } = await api.get<LendingData | LendingData[]>('lending-info');
  return unwrap(data);
}

export async function postLending(
  payload: LendingData
): Promise<LendingData> {
  const { data } = await api.post<LendingData>('lending-info', payload);
  return data;
}
