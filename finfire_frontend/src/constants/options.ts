export const STAGE_OPTIONS = [
  'Idea',
  'Formation',
  'Start Up',
  'Growth',
  'M & A',
  'Preparing for Public',
  'Distressed',
] as const;

export const ENTITY_OPTIONS = [
  'None (To be Determined)',
  'Sole Proprietorship',
  'LLC',
  'LP',
  'GP',
  'S Corporation',
  'C Corp',
  'Other',
] as const;

export const PRE_CAPITAL_OPTIONS = [
  'Less than $25,000',
  '$26,000 to $100,000',
  '$101,000 to $250,000',
  '$251,000 to $500,000',
  '$501,000 to $1,000,000',
  '$1,000,001 to $2,000,000',
  '$2,000,001 to $5,000,000',
  '$5,000,001 to $10,000,000',
  'More than $10,000,000',
] as const;

export const PRE_MARKET_OPTIONS = [
  'Accelerator',
  'Bonds',
  'Commercial Banks',
  'Cryptocurrency',
  'EB5 Immigration',
  'Enterprise Zones',
  'Factoring',
  'Grants',
  'Hedge Funds',
  'Incubator',
  'Investment Banking',
  'Other (Owner Equity)',
  'Private Debt (Officer Loans to Startup)',
  'Private Equity Securities',
  'Public Offering',
  'Real Estate',
  'Royalty Financing',
  'Small Business Administration (SBA)',
  'Venture Capital',
  'Unsure/Do not Know',
] as const;

export const PLANNED_RAISE_OPTIONS = [
  'Less than $25,000',
  '$25,000 to $100,000',
  '$100,000 to $249,999',
  '$250,000 to $499,999',
  '$500,000 to $999,999',
  '$1,000,000 to $1,349,999',
  '$1,350,000 to $1,999,999',
  '$2,000,000 to $4,999,999',
  '$5,000,000 to $9,999,999',
  '$10,000,000 to $19,999,999',
  'More Than $20 Million',
  'Unsure/Do not Know/TBD',
] as const;

export const ROUNDS_OPTIONS = [
  'Founders Round',
  'Pre-Seed',
  'Seed',
  'Series A',
  'Series B',
  'Series C',
  'Pre-IPO',
  'IPO',
  'Unsure/Do not Know/TBD',
] as const;

export const ROUNDS_COUNT_OPTIONS = [
  'One',
  'Two',
  'TBD',
] as const;

export const USE_OF_FUNDS_OPTIONS = [
  'Start Up',
  'Growth/Scalability',
  'Marketing and Sales',
  'Cash Flow Capital',
  'Human Capital',
  'Equipment',
  'Merger and Acquisitions',
  'Inventory',
  'Real Estate',
  'Other',
  'Unsure',
] as const;

export const RISK_TOLERANCE_OPTIONS = [
  'Very Low/Low Risk Tolerance (Expect to at least recoup principle)',
  'Medium Risk Tolerance (Can lose some or most of the funding)',
  'High Risk Tolerance (Can lose most or all of the funding)',
] as const;

export const COST_TOLERANCE_OPTIONS = [
  'Low Cost of Capital (1-4%)',
  'Medium Cost of Capital (5-10%)',
  'High Cost of Capital (11-18%)',
  'Very High Cost of Capital (19%+)',
  'As long as the enterprise receives the net amount it needs, the cost is immaterial',
] as const;

export const COST_RANGE_OPTIONS = [
  'Minimum $0 - Maximum $499',
  '$500 - $999',
  '$1000 - $2499',
  '$2500 - $4999',
  '$5000 - $9999',
  '$10000 - $24999',
  '$25000 - $49999',
  '$50000+',
] as const;

export const TIMING_OPTIONS = [
  '1 Day to 1 Week',
  '1 Week to 2 Weeks',
  '2 Weeks to 4 Weeks',
  '1 Month to 2 Months',
  '2 Months to 3 Months',
  '3 Months to 6 Months',
  '6 Months to 12 Months',
  'More than 1 year',
] as const;

// Must stay in sync with ReferalResponse.referral_source choices
// in entreprise_questions/models.py.
export const REFERRAL_OPTIONS = [
  'A Friend / Colleague',
  'Financial Advisor / Consultant',
  'Social Media',
  'Online Search',
  'News / Article / Blog',
  'Event / Webinar',
  'Other',
] as const;

export const AFFILIATION_OPTIONS = [
  'Self-Funded',
  'Angel Investor',
  'Venture Capital Firm',
  'Private Equity Firm',
  'Incubator/Accelerator',
  'Government Agency',
  'Non-Profit',
  'University/Research Institution',
  'Other',
] as const;

export const SPECIAL_PROGRAMS_OPTIONS = [
  'Minority-Owned',
  'Woman-Owned',
  'Veteran-Owned',
  'Disabled-Owned',
  'LGBTQ+-Owned',
  'None',
] as const;

// ── Account Type & Purpose ──────────────────────────────────────────────────

export const ACCOUNT_TYPE_OPTIONS = [
  'Enterprise/Business',
  'Intermediary',
  'Capital Market',
] as const;

export const PRIMARY_PURPOSE_OPTIONS = [
  'Consultant and/or Intermediary Seeking Leads & Providing Advice',
  'Cost to Package the Right Capital Type to the Situation',
  'Education - Learn the Capital Markets & Capital Types Available',
  "I Don't Know - TBD",
  'Identify Documents Required for the Most Probable Capital Type',
  'Information - Match the Right Capital to the Situation',
  'Introductions to Capital Sources Currently Funding',
  'Introductions to Qualified Companies Seeking Capital',
  'Timeline to Capital',
] as const;

// ── Document Status (0-5 scale) ─────────────────────────────────────────────

export const DOCUMENT_STATUS_OPTIONS = [
  { value: '0', label: '0 - Not Started' },
  { value: '1', label: '1 - Planning' },
  { value: '2', label: '2 - In Progress' },
  { value: '3', label: '3 - Draft Complete' },
  { value: '4', label: '4 - Under Review' },
  { value: '5', label: '5 - Complete' },
] as const;

// ── NAICS / Industry ────────────────────────────────────────────────────────

export const NAICS_INDUSTRY_OPTIONS = [
  'Administration',
  'Agriculture',
  'Arts',
  'Energy/Utilities',
  'Entertainment',
  'Finance',
  'High tech',
  'Hospitality, F & B',
  'Info Services',
  'Manufacturing',
  'Mining',
  'Professional Insurance/Mgmt',
  'Real State',
  'Science - Health - Medicine',
  'Sector/Sub-Sector',
  'Trades - Construction',
  'Transportation & Logistics',
  'Waste Management',
  'Wholesale & Retail',
  'Other',
] as const;

// ── Intermediary Options ────────────────────────────────────────────────────

export const INTERMEDIARY_TYPE_OPTIONS = [
  'Technical_Writer',
  'Content_Creator',
  'Business_Consultant',
  'Marketing_Analyst',
  'Business_Plan_Writer',
  'Business_Attorney',
  'Exempt Securities',
  'Researcher',
  'Subject_Matter_Expert',
  'Business_Analyst',
  'Data_Entry',
  'Financial_Analyst',
  'Accountant',
  'CPA',
  'Financial Modeler',
  'Valuation_Analyst',
  'Banker',
  'Web_Developer',
  'Marketing_Consultant',
  'Transfer_Agency',
  'Graphic_Designer',
  'Hr_Due_Diligence',
  'Management_Consultant',
  'Hr_Consultant',
  'Culture_Subject_Matter_Expert',
  'Broker_Agency',
  'Platform',
  'Securities_Attorney',
  'Paralegal',
  'Intelectual_Property_Attorney',
  'Legal_Assistant',
  'Risk_Analyst',
  'Underwritter',
] as const;

export const INTERMEDIARY_PRICING_TYPE_OPTIONS = [
  'Hourly',
  'Fixed Price',
  'Commission',
  'Royalty',
  'By the Project',
  'Success Fees',
  'Others',
] as const;

// ── Capital Market (Vendor) Options ─────────────────────────────────────────

export const CM_TYPE_OPTIONS = [
  '66- Private Equity Securities - Regulation CF Tittle III',
  '65- Private Equity Securities - Regulation A',
  '1- Private Equity',
  '77- Small Business Administration (SBA) - SBA 504B',
  '21- Commercial Banking - Line of Credit',
  'Regulation D 506B',
  'Exempt Securities',
  '75- Private Equity Securities - Simple Agreement Future Equity',
  'Business Accelerator',
  'Business Incubator',
  '79- Small Business Administration (SBA) - SBA Micro Lender',
] as const;

// ── Lending Information ─────────────────────────────────────────────────────

export const COLLATERAL_OPTIONS = [
  'Not Applicable',
  'Yes',
  'No',
  'Unknown',
] as const;

export const CREDIT_SCORE_OPTIONS = [
  '<580',
  '>620',
  '>680',
  '>720',
  '>760',
] as const;

export const CRIMINAL_HISTORY_OPTIONS = [
  'None',
  'Misdemeanor',
  'Felony',
  'Fraud',
  'Securities Violation',
] as const;

// ── US States ───────────────────────────────────────────────────────────────

export const US_STATES = [
  'Alabama',
  'Alaska',
  'Arizona',
  'Arkansas',
  'California',
  'Colorado',
  'Connecticut',
  'Delaware',
  'Florida',
  'Georgia',
  'Hawaii',
  'Idaho',
  'Illinois',
  'Indiana',
  'Iowa',
  'Kansas',
  'Kentucky',
  'Louisiana',
  'Maine',
  'Maryland',
  'Massachusetts',
  'Michigan',
  'Minnesota',
  'Mississippi',
  'Missouri',
  'Montana',
  'Nebraska',
  'Nevada',
  'New Hampshire',
  'New Jersey',
  'New Mexico',
  'New York',
  'North Carolina',
  'North Dakota',
  'Ohio',
  'Oklahoma',
  'Oregon',
  'Pennsylvania',
  'Rhode Island',
  'South Carolina',
  'South Dakota',
  'Tennessee',
  'Texas',
  'Utah',
  'Vermont',
  'Virginia',
  'Washington',
  'West Virginia',
  'Wisconsin',
  'Wyoming',
] as const;
