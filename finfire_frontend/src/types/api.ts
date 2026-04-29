// ── Auth ─────────────────────────────────────────────────────────────────────

export interface LoginResponse {
  auth_token: string;
}

export interface RegisterPayload {
  username: string;
  email: string;
  password: string;
}

export interface User {
  id?: number;
  username: string;
  email: string;
  is_staff?: boolean;
}

// ── Questionnaire Step Data ──────────────────────────────────────────────────

/** Step 1 - Contact Information */
export interface ContactData {
  display_name: string;
  companyAffiliation: string[];
  email: string;
  companyWebsite: string;
  primaryBusinessAddress: string;
  businessPhone: string;
  mobilePhone: string;
  specialPrograms: string[];
}

/** Step 2 - Stage of Development */
export interface StageData {
  stageofCompany: string;
}

/** Step 3 - Entity Type */
export interface EntityData {
  entityType: string;
  entityName: string;
  entityStateofRegistration: string;
}

/** Step 4 - Pre-Capital Raised */
export interface PreCapitalData {
  preCapitalRaise: string;
}

/** Step 5 - Pre-Market Capital Types */
export interface PreMarketData {
  capitalPreMarkets: string[];
}

/** Step 6 - Amount of Planned Raise */
export interface PlannedRaiseData {
  plannedRaise: string;
}

/** Step 7 - Rounds of Capital */
export interface RoundsData {
  currentRounds: string[];
  howManyRounds: string;
}

/** Step 8 - Use of Funds */
export interface UseOfFundsData {
  fundsUse: string[];
}

/** Step 9 - Risk & Capital Cost */
export interface RiskData {
  riskToleranceInvestor: string;
  riskToleranceFounder: string;
}

/** Step 10 - Up Front Cost & Timing */
export interface CostTimeData {
  rangeofCost: string;
  timing: string;
}

/** Step 11 - Pre-Rating */
export interface PreRatingData {
  preratings: Record<string, number | string>;
}

/** Step 12 - Referral */
export interface ReferralData {
  referralSource: string;
  referrerName: string;
  referralOther: string;
}

// ── Account Setup ───────────────────────────────────────────────────────────

export interface AccountData {
  accountType: string;
  primaryAppUse: string[];
}

// ── Documents & Due Diligence ───────────────────────────────────────────────

/** All Documents Prepared (boolean checklist) */
export interface DocumentsPreparedData {
  summaryofOffering: boolean;
  financialForecast: boolean;
  leanBusinessModelCanvas: boolean;
  presentationDeck: boolean;
  leadershipOverview: boolean;
  exitStrategy: boolean;
  offeringDocuments: boolean;
  aiGeneratedDeepDive: boolean;
  virtualDataroom: boolean;
}

/** Document Details (status strings) */
export interface DocumentsDetailData {
  onePageTearSheet: string;
  elevatorPitch: string;
  businessPlan: string;
  corporateIdentityDueDiligence: string;
  technologyDueDiligence: string;
  executiveSummary: string;
  virtualPortal: string;
}

/** Financials Prepared */
export interface FinancialsData {
  assumptionsWorksheets: string;
  capitalSourceStructure: string;
  capitalizationTable: string;
  financialModelingFixedCosts: string;
  financialModelingRevenuesCosts: string;
  financialModelingSummaryPage: string;
  sourcesUses: string;
  valuationSpreadsheets: string;
  valuationLetterFinal: string;
}

/** Marketing & Presentation */
export interface MarketingData {
  businessModelCanvas: string;
  companyWeb3: string;
  competitiveAnalysis: string;
  marketing: string;
  marketingPlanBudget: string;
  marketResearchReport: string;
  presentationDeck: string;
  strategicTacticalPlan: string;
}

/** People & Culture */
export interface PeopleCultureData {
  leadership: string;
  managementExperience: string;
  consultantsAdvisors: string;
  staff: string;
  culture: string;
}

/** Legal, Offering & Risk */
export interface LegalRiskData {
  capitalMarketPlan: string;
  capitalOfferingDocuments: string;
  intellectualPropertyDueDiligence: string;
  legalDueDiligence: string;
  riskAssessmentDueDiligence: string;
  exitStrategy: string;
}

/** NAICS / Industry */
export interface NaicsData {
  naicsCode: string;
}

/** Lending Information */
export interface LendingData {
  collateralStatus: string;
  creditScore: string;
  criminalHistory: string;
}

// ── Intermediary Questions ──────────────────────────────────────────────────

export interface IntermediaryQ1Data {
  First_Name: string;
  Last_Name: string;
  Company_Name: string;
  Primary_Phone: string;
  Secondary_Phone: string;
  Alternate_Phone: string;
  Email: string;
  Adress: string;
  City: string;
  State: string;
  Zip_Code: string;
  I_Type: string;
  Prefered_CM: string[];
  Specialized_Industry: string[];
  Regions_Served: string[];
  Selected_Options: string[];
}

export interface IntermediaryQ2Data {
  Type: string;
  Explanation: string;
  Rate: string;
}

// ── Capital Market (Vendor) Questions ───────────────────────────────────────

export interface VendorQ1Data {
  First_Name: string;
  Last_Name: string;
  Company_Name: string;
  Primary_Phone: string;
  Secondary_Phone: string;
  Alternate_Phone: string;
  Email: string;
  Adress: string;
  City: string;
  State: string;
  Zip_Code: string;
  CM_Type: string;
}

// ── Payload ─────────────────────────────────────────────────────────────────

export interface PayloadData {
  payLoadString: Record<string, unknown>;
}

// ── Auth Extras ─────────────────────────────────────────────────────────────

export interface PasswordResetRequest {
  email: string;
}

export interface PasswordResetConfirm {
  uid: string;
  token: string;
  new_password: string;
  re_new_password: string;
}

// ── Match Results ────────────────────────────────────────────────────────────

export interface MatchCapitalType {
  capital_type: string;
  score: number;
  rank: number;
  definition: string;
  faq: string;
  title: string;
}

export interface MatchData {
  matches: MatchCapitalType[];
  generated_at: string;
}
