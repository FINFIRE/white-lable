import React, { useState, useEffect } from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import {
  getAdminUserData,
  postAdminUserStepData,
  activateUser,
  getAdminMatchPDF,
} from '../../api/admin';
import { useQuestionnaireStore } from '../../stores/questionnaireStore';
import LoadingSpinner from '../ui/LoadingSpinner';
import RadioGroup from '../ui/RadioGroup';
import CheckboxGroup from '../ui/CheckboxGroup';
import SelectDropdown from '../ui/SelectDropdown';
import RangeSlider from '../ui/RangeSlider';
import {
  STAGE_OPTIONS, ENTITY_OPTIONS, PRE_CAPITAL_OPTIONS, PRE_MARKET_OPTIONS,
  PLANNED_RAISE_OPTIONS, ROUNDS_OPTIONS, ROUNDS_COUNT_OPTIONS,
  USE_OF_FUNDS_OPTIONS, RISK_TOLERANCE_OPTIONS, COST_TOLERANCE_OPTIONS,
  COST_RANGE_OPTIONS,
  TIMING_OPTIONS, REFERRAL_OPTIONS, AFFILIATION_OPTIONS,
  SPECIAL_PROGRAMS_OPTIONS, US_STATES,
  COLLATERAL_OPTIONS, CREDIT_SCORE_OPTIONS, CRIMINAL_HISTORY_OPTIONS,
  PRIMARY_PURPOSE_OPTIONS,
} from '../../constants/options';

/* ── Field / Step definitions ──────────────────────────────────────────────── */

interface FieldDef {
  name: string;
  label: string;
  type: 'text' | 'email' | 'radio' | 'select' | 'checkbox-group' | 'checkbox' | 'slider';
  options?: readonly string[] | string[];
}

interface StepDef {
  backendKey: string;
  label: string;
  shortLabel: string;
  fields: FieldDef[];
}

const ADMIN_STEPS: StepDef[] = [
  {
    backendKey: 'contact', label: 'Contact Information', shortLabel: 'Contact',
    fields: [
      { name: 'display_name', label: 'Display Name', type: 'text' },
      { name: 'companyAffiliation', label: 'Company Affiliation', type: 'checkbox-group', options: AFFILIATION_OPTIONS },
      { name: 'email', label: 'Email', type: 'email' },
      { name: 'companyWebsite', label: 'Company Website', type: 'text' },
      { name: 'primaryBusinessAddress', label: 'Business Address', type: 'text' },
      { name: 'businessPhone', label: 'Business Phone', type: 'text' },
      { name: 'mobilePhone', label: 'Mobile Phone', type: 'text' },
      { name: 'specialPrograms', label: 'Special Programs', type: 'checkbox-group', options: SPECIAL_PROGRAMS_OPTIONS },
    ],
  },
  {
    backendKey: 'account', label: 'Account Setup', shortLabel: 'Account',
    fields: [
      { name: 'accountType', label: 'Account Type', type: 'radio', options: ['Enterprise/Business'] },
      { name: 'primaryAppUse', label: 'Primary purpose for using FinFire', type: 'checkbox-group', options: PRIMARY_PURPOSE_OPTIONS },
    ],
  },
  {
    backendKey: 'stage', label: 'Stage of Development', shortLabel: 'Stage',
    fields: [{ name: 'stageofCompany', label: 'What stage is the company in?', type: 'radio', options: STAGE_OPTIONS }],
  },
  {
    backendKey: 'entity', label: 'Entity Type', shortLabel: 'Entity',
    fields: [
      { name: 'entityType', label: 'Entity Type', type: 'radio', options: ENTITY_OPTIONS },
      { name: 'entityName', label: 'Entity Name', type: 'text' },
      { name: 'entityStateofRegistration', label: 'State of Registration', type: 'select', options: US_STATES },
    ],
  },
  {
    backendKey: 'preCapital', label: 'Pre-Capital Raised', shortLabel: 'Pre-Capital',
    fields: [{ name: 'preCapitalRaise', label: 'How much capital has been raised?', type: 'radio', options: PRE_CAPITAL_OPTIONS }],
  },
  {
    backendKey: 'preMarket', label: 'Pre-Market Capital Types', shortLabel: 'Pre-Market',
    fields: [{ name: 'capitalPreMarkets', label: 'Which capital markets have been utilized?', type: 'checkbox-group', options: PRE_MARKET_OPTIONS }],
  },
  {
    backendKey: 'plannedRaise', label: 'Amount of Planned Raise', shortLabel: 'Planned Raise',
    fields: [{ name: 'plannedRaise', label: 'How much capital to be raised?', type: 'radio', options: PLANNED_RAISE_OPTIONS }],
  },
  {
    backendKey: 'rounds', label: 'Rounds of Capital', shortLabel: 'Rounds',
    fields: [
      { name: 'currentRounds', label: 'Current round of capital', type: 'checkbox-group', options: ROUNDS_OPTIONS },
      { name: 'howManyRounds', label: 'How many rounds?', type: 'radio', options: ROUNDS_COUNT_OPTIONS },
    ],
  },
  {
    backendKey: 'useOfFunds', label: 'Use of Funds', shortLabel: 'Use of Funds',
    fields: [{ name: 'fundsUse', label: 'Primary uses of funds', type: 'checkbox-group', options: USE_OF_FUNDS_OPTIONS }],
  },
  {
    backendKey: 'risk', label: 'Risk & Capital Cost', shortLabel: 'Risk',
    fields: [
      { name: 'riskToleranceInvestor', label: 'Investor risk tolerance', type: 'radio', options: RISK_TOLERANCE_OPTIONS },
      // riskToleranceFounder maps to EQuestions8.Selected_Option2, which is
      // the founder's cost-of-capital tolerance — NOT a duplicate risk-tolerance
      // question. Must use COST_TOLERANCE_OPTIONS so the value the admin picks
      // is in the model's CHOICES2 list (otherwise the new ChoiceField on the
      // serializer rejects the POST with 400 and the row never updates).
      { name: 'riskToleranceFounder', label: "Founder's tolerance for cost of capital", type: 'radio', options: COST_TOLERANCE_OPTIONS },
    ],
  },
  {
    backendKey: 'costTime', label: 'Up Front Cost & Timing', shortLabel: 'Cost & Timing',
    fields: [
      { name: 'rangeofCost', label: 'Range of cost', type: 'radio', options: COST_RANGE_OPTIONS },
      { name: 'timing', label: 'Timing', type: 'radio', options: TIMING_OPTIONS },
    ],
  },
  {
    backendKey: 'docsPrepared', label: 'Documents Prepared', shortLabel: 'Docs Prepared',
    fields: [
      { name: 'summaryofOffering', label: 'Summary of Offering', type: 'checkbox' },
      { name: 'financialForecast', label: 'Financial Forecast', type: 'checkbox' },
      { name: 'leanBusinessModelCanvas', label: 'Lean Business Model Canvas', type: 'checkbox' },
      { name: 'presentationDeck', label: 'Presentation Deck', type: 'checkbox' },
      { name: 'leadershipOverview', label: 'Leadership Overview', type: 'checkbox' },
      { name: 'exitStrategy', label: 'Exit Strategy', type: 'checkbox' },
      { name: 'offeringDocuments', label: 'Offering Documents', type: 'checkbox' },
      { name: 'aiGeneratedDeepDive', label: 'AI Generated Deep Dive', type: 'checkbox' },
      { name: 'virtualDataroom', label: 'Virtual Data Room', type: 'checkbox' },
    ],
  },
  {
    backendKey: 'preRating', label: 'Pre-Rating', shortLabel: 'Pre-Rating',
    fields: [
      { name: 'financial_model_forecast_pro_forma', label: 'Financial Model, Forecast, Pro Forma', type: 'slider' },
      { name: 'finfire_report_capital_type', label: 'Finfire Report - Capital Type', type: 'slider' },
      { name: 'due_diligence_checklist_documents', label: 'Due Diligence Checklist Documents', type: 'slider' },
      { name: 'historical_financials', label: 'Historical Financials', type: 'slider' },
      { name: 'tax_returns', label: 'Tax Returns', type: 'slider' },
      { name: 'business_valuation_equity_only', label: 'Business Valuation (Equity only)', type: 'slider' },
      { name: 'cap_table_use_of_funds_and_capitalization_plan', label: 'Cap Table & Capitalization Plan', type: 'slider' },
      { name: 'business_model_canvas', label: 'Business Model Canvas', type: 'slider' },
      { name: 'offering_documents_rating', label: 'Offering Documents', type: 'slider' },
      { name: 'presentation_video_ai_deep_dive', label: 'Presentation Video (AI Deep Dive)', type: 'slider' },
      { name: 'application_if_applicable', label: 'Application (If Applicable)', type: 'slider' },
      { name: 'resume_of_founder_ceo_primary_leader', label: 'Resume of Founder/CEO', type: 'slider' },
      { name: 'presentation_deck_rating', label: 'Presentation Deck', type: 'slider' },
      { name: 'executive_summary_including_exit_strategy', label: 'Executive Summary & Exit Strategy', type: 'slider' },
      { name: 'quality_assurance_checklist_including_ai', label: 'QA Checklist (Including AI)', type: 'slider' },
      { name: 'capital_match_list_generated', label: 'Capital Match List Generated', type: 'slider' },
      { name: 'investor_marketing_campaign', label: 'Investor Marketing Campaign', type: 'slider' },
      { name: 'investor_relations', label: 'Investor Relations', type: 'slider' },
      { name: 'progress_reports', label: 'Progress Reports', type: 'slider' },
    ],
  },
  {
    backendKey: 'lending', label: 'Lending Information', shortLabel: 'Lending',
    fields: [
      { name: 'collateralStatus', label: 'Collateral availability', type: 'radio', options: COLLATERAL_OPTIONS },
      { name: 'creditScore', label: 'Credit score', type: 'radio', options: CREDIT_SCORE_OPTIONS },
      { name: 'criminalHistory', label: 'Criminal history', type: 'radio', options: CRIMINAL_HISTORY_OPTIONS },
    ],
  },
  {
    backendKey: 'referral', label: 'Referral', shortLabel: 'Referral',
    fields: [
      { name: 'referralSource', label: 'How did they hear about FinFire?', type: 'radio', options: REFERRAL_OPTIONS },
      { name: 'referrerName', label: 'Referrer Name', type: 'text' },
      { name: 'referralOther', label: 'Additional Details', type: 'text' },
    ],
  },
];

// "Match" is a virtual tab index after all real steps
const MATCH_TAB_INDEX = ADMIN_STEPS.length;

const inputClass =
  'block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-sm text-slate-900 outline-none transition focus:border-blue-500 focus:ring-2 focus:ring-blue-200';

const AdminUserEdit: React.FC = () => {
  const adminEditUserId = useQuestionnaireStore((s) => s.adminEditUserId);
  const setView = useQuestionnaireStore((s) => s.setView);
  const queryClient = useQueryClient();

  const [activeTab, setActiveTab] = useState(0);
  const [formData, setFormData] = useState<Record<string, Record<string, unknown>>>({});
  const [saveMsg, setSaveMsg] = useState<string | null>(null);
  const [pdfUrl, setPdfUrl] = useState<string | null>(null);
  const [matchLoading, setMatchLoading] = useState(false);
  const [matchError, setMatchError] = useState<string | null>(null);

  const { data, isLoading } = useQuery({
    queryKey: ['adminUserData', adminEditUserId],
    queryFn: () => getAdminUserData(adminEditUserId!),
    enabled: !!adminEditUserId,
  });

  useEffect(() => {
    if (data?.steps) {
      const initial: Record<string, Record<string, unknown>> = {};
      for (const step of ADMIN_STEPS) {
        const serverData = data.steps[step.backendKey];
        if (serverData) {
          initial[step.backendKey] = { ...serverData };
        }
      }
      setFormData(initial);
    }
  }, [data]);

  const saveMutation = useMutation({
    mutationFn: ({ stepKey, payload }: { stepKey: string; payload: Record<string, unknown> }) =>
      postAdminUserStepData(adminEditUserId!, stepKey, payload),
    onSuccess: (_d, vars) => {
      const stepLabel = ADMIN_STEPS.find((s) => s.backendKey === vars.stepKey)?.label ?? vars.stepKey;
      setSaveMsg(`${stepLabel} saved successfully.`);
      queryClient.invalidateQueries({ queryKey: ['adminUserData', adminEditUserId] });
      setTimeout(() => setSaveMsg(null), 3000);
    },
    onError: () => setSaveMsg(null),
  });

  const activateMutation = useMutation({
    mutationFn: () => activateUser(adminEditUserId!),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['adminUserData', adminEditUserId] });
      queryClient.invalidateQueries({ queryKey: ['adminUsers'] });
      setSaveMsg('User activated.');
      setTimeout(() => setSaveMsg(null), 3000);
    },
  });

  const handleMatch = async () => {
    if (!adminEditUserId) return;
    setMatchLoading(true);
    setMatchError(null);
    if (pdfUrl) URL.revokeObjectURL(pdfUrl);
    setPdfUrl(null);
    try {
      const blob = await getAdminMatchPDF(adminEditUserId);
      setPdfUrl(URL.createObjectURL(blob));
    } catch {
      setMatchError('Matching failed. Ensure all questionnaire steps are completed for this user.');
    } finally {
      setMatchLoading(false);
    }
  };

  if (!adminEditUserId) {
    return <div style={{ padding: 32, textAlign: 'center', color: '#94A3B8' }}>No user selected.</div>;
  }

  if (isLoading) {
    return (
      <div className="flex items-center justify-center py-24">
        <LoadingSpinner />
      </div>
    );
  }

  const userData = data?.steps || {};
  const userInfo = data?.user;
  const isMatchTab = activeTab === MATCH_TAB_INDEX;
  const currentStep = !isMatchTab ? ADMIN_STEPS[activeTab] : null;

  /* ── Value helpers ─────────────────────────────────────────────────────── */
  const getVal = (fieldName: string): unknown => {
    if (!currentStep) return '';
    return formData[currentStep.backendKey]?.[fieldName] ?? '';
  };

  const setVal = (fieldName: string, value: unknown) => {
    if (!currentStep) return;
    setFormData((prev) => ({
      ...prev,
      [currentStep.backendKey]: { ...prev[currentStep.backendKey], [fieldName]: value },
    }));
  };

  const getPreRatingVal = (fieldName: string): number => {
    const preratings = formData['preRating']?.['preratings'];
    if (preratings && typeof preratings === 'object' && !Array.isArray(preratings)) {
      return Number((preratings as Record<string, unknown>)[fieldName]) || 0;
    }
    return 0;
  };

  const setPreRatingVal = (fieldName: string, value: number) => {
    setFormData((prev) => {
      const existing = prev['preRating']?.['preratings'];
      const ratings = (existing && typeof existing === 'object' && !Array.isArray(existing))
        ? { ...(existing as Record<string, unknown>) }
        : {};
      ratings[fieldName] = value;
      return { ...prev, preRating: { ...prev['preRating'], preratings: ratings } };
    });
  };

  /* ── Save handler ──────────────────────────────────────────────────────── */
  const handleSave = () => {
    if (!currentStep) return;
    const payload: Record<string, unknown> = {};

    if (currentStep.backendKey === 'preRating') {
      const ratings: Record<string, number> = {};
      for (const f of currentStep.fields) {
        ratings[f.name] = Number(getPreRatingVal(f.name)) || 0;
      }
      saveMutation.mutate({ stepKey: 'preRating', payload: { preratings: ratings } });
      return;
    }

    if (currentStep.backendKey === 'docsPrepared') {
      for (const f of currentStep.fields) {
        payload[f.name] = !!getVal(f.name);
      }
      saveMutation.mutate({ stepKey: currentStep.backendKey, payload });
      return;
    }

    for (const f of currentStep.fields) {
      payload[f.name] = getVal(f.name);
    }
    saveMutation.mutate({ stepKey: currentStep.backendKey, payload });
  };

  /* ── Render a single form field ────────────────────────────────────────── */
  const renderField = (field: FieldDef) => {
    const isPreRating = currentStep?.backendKey === 'preRating';

    if (field.type === 'radio' && field.options) {
      return (
        <RadioGroup key={field.name} name={field.name} label={field.label}
          options={[...field.options]} value={String(getVal(field.name) ?? '')}
          onChange={(v) => setVal(field.name, v)} />
      );
    }
    if (field.type === 'select' && field.options) {
      return (
        <SelectDropdown key={field.name} name={field.name} label={field.label}
          options={[...field.options]} value={String(getVal(field.name) ?? '')}
          onChange={(v) => setVal(field.name, v)} />
      );
    }
    if (field.type === 'checkbox-group' && field.options) {
      const raw = getVal(field.name);
      const values = Array.isArray(raw) ? raw.map(String) : [];
      return (
        <CheckboxGroup key={field.name} name={field.name} label={field.label}
          options={[...field.options]} values={values}
          onChange={(v) => setVal(field.name, v)} />
      );
    }
    if (field.type === 'checkbox') {
      const checked = !!getVal(field.name);
      return (
        <label key={field.name}
          className="flex items-center gap-3 rounded-lg border-2 px-4 py-3 text-sm cursor-pointer transition-colors"
          style={{ borderColor: checked ? '#3B82F6' : '#E5E7EB', background: checked ? '#EFF6FF' : '#fff' }}>
          <input type="checkbox" checked={checked}
            onChange={(e) => setVal(field.name, e.target.checked)}
            className="h-4 w-4 rounded border-gray-300 text-blue-500 focus:ring-blue-200" />
          <span className="text-slate-700">{field.label}</span>
        </label>
      );
    }
    if (field.type === 'slider') {
      const val = isPreRating ? getPreRatingVal(field.name) : Number(getVal(field.name)) || 0;
      return (
        <RangeSlider key={field.name} name={field.name} label={field.label}
          value={val} onChange={(v) => isPreRating ? setPreRatingVal(field.name, v) : setVal(field.name, v)}
          min={0} max={10} />
      );
    }
    return (
      <div key={field.name}>
        <label className="block text-sm font-medium text-slate-900 mb-1">{field.label}</label>
        <input type={field.type === 'email' ? 'email' : 'text'}
          value={String(getVal(field.name) ?? '')}
          onChange={(e) => setVal(field.name, e.target.value)} className={inputClass} />
      </div>
    );
  };

  /* ── Render ────────────────────────────────────────────────────────────── */
  return (
    <div>
      {/* Header */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 20 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 14 }}>
          <button onClick={() => setView('dashboard')}
            style={{ background: 'none', border: '1px solid #E2E8F0', borderRadius: 8, padding: '6px 12px', cursor: 'pointer', fontSize: 13, color: '#334155' }}>
            &larr; Back
          </button>
          <div>
            <div style={{ fontSize: 18, fontWeight: 700, color: '#0F172A' }}>{userInfo?.username || 'User'}</div>
            <div style={{ fontSize: 12, color: '#94A3B8' }}>{userInfo?.email}</div>
          </div>
        </div>
        <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
          {userInfo && !userInfo.is_active && (
            <button onClick={() => activateMutation.mutate()} disabled={activateMutation.isPending}
              style={{ background: '#059669', color: '#fff', border: 'none', borderRadius: 8, padding: '7px 14px', fontSize: 13, fontWeight: 600, cursor: 'pointer' }}>
              {activateMutation.isPending ? 'Activating...' : 'Activate User'}
            </button>
          )}
          <span style={{
            padding: '4px 10px', borderRadius: 20, fontSize: 12, fontWeight: 600,
            background: userInfo?.is_active ? '#DCFCE7' : '#FEF3C7', color: userInfo?.is_active ? '#166534' : '#92400E',
          }}>
            {userInfo?.is_active ? 'Active' : 'Inactive'}
          </span>
        </div>
      </div>

      {saveMsg && (
        <div style={{ background: '#DCFCE7', border: '1px solid #BBF7D0', borderRadius: 10, padding: '10px 16px', fontSize: 13, color: '#166534', marginBottom: 16 }}>
          {saveMsg}
        </div>
      )}

      <div style={{ display: 'flex', gap: 20 }}>
        {/* Tab sidebar */}
        <div style={{ width: 200, flexShrink: 0, background: '#fff', borderRadius: 16, border: '1px solid #E2E8F0', padding: '12px 10px', alignSelf: 'flex-start', maxHeight: 'calc(100vh - 180px)', overflowY: 'auto' }}>
          {ADMIN_STEPS.map((step, i) => {
            const hasData = userData[step.backendKey] != null;
            return (
              <button key={step.backendKey} onClick={() => setActiveTab(i)}
                style={{
                  display: 'flex', alignItems: 'center', gap: 8, width: '100%', padding: '8px 10px', borderRadius: 8,
                  border: 'none', cursor: 'pointer', fontFamily: 'inherit',
                  background: activeTab === i ? '#EFF6FF' : 'transparent',
                  color: activeTab === i ? '#1D4ED8' : '#334155', fontWeight: activeTab === i ? 600 : 400,
                  fontSize: 12, textAlign: 'left', marginBottom: 2,
                }}>
                <span style={{ width: 8, height: 8, borderRadius: '50%', flexShrink: 0, background: hasData ? '#059669' : '#E2E8F0' }} />
                {step.shortLabel}
              </button>
            );
          })}

          {/* Match tab */}
          <div style={{ height: 1, background: '#E2E8F0', margin: '8px 0' }} />
          <button onClick={() => setActiveTab(MATCH_TAB_INDEX)}
            style={{
              display: 'flex', alignItems: 'center', gap: 8, width: '100%', padding: '8px 10px', borderRadius: 8,
              border: 'none', cursor: 'pointer', fontFamily: 'inherit',
              background: isMatchTab ? '#F0FDF4' : 'transparent',
              color: isMatchTab ? '#166534' : '#059669', fontWeight: 600,
              fontSize: 12, textAlign: 'left',
            }}>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
              <path d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z" />
            </svg>
            Match & PDF
          </button>
        </div>

        {/* Content area */}
        <div style={{ flex: 1, maxWidth: 600, background: '#fff', borderRadius: 16, border: '1px solid #E2E8F0', padding: '28px 32px', maxHeight: 'calc(100vh - 180px)', overflowY: 'auto' }}>

          {/* ── Match tab content ─────────────────────────────────────── */}
          {isMatchTab && (
            <div>
              <div style={{ fontSize: 16, fontWeight: 700, color: '#0F172A', marginBottom: 8 }}>
                Match Capital & Generate PDF
              </div>
              <p style={{ fontSize: 13, color: '#64748B', marginBottom: 20 }}>
                Run the matching algorithm for this user and generate their match letter PDF.
              </p>

              <button onClick={handleMatch} disabled={matchLoading}
                style={{
                  background: 'linear-gradient(135deg, #059669, #065F46)', color: '#fff', border: 'none',
                  borderRadius: 10, padding: '12px 28px', fontSize: 14, fontWeight: 600,
                  cursor: matchLoading ? 'not-allowed' : 'pointer', opacity: matchLoading ? 0.7 : 1,
                  marginBottom: 20,
                }}>
                {matchLoading ? 'Matching...' : 'Run Match'}
              </button>

              {matchError && (
                <div style={{ background: '#FEF2F2', border: '1px solid #FECACA', borderRadius: 10, padding: '12px 16px', fontSize: 13, color: '#991B1B', marginBottom: 16 }}>
                  {matchError}
                </div>
              )}

              {pdfUrl && (
                <div>
                  <div style={{ border: '1px solid #E2E8F0', borderRadius: 12, overflow: 'hidden', marginBottom: 16 }}>
                    <iframe src={pdfUrl} title="Match Letter PDF" style={{ width: '100%', height: 550, border: 'none' }} />
                  </div>
                  <div style={{ display: 'flex', gap: 10 }}>
                    <button onClick={() => {
                      const a = document.createElement('a');
                      a.href = pdfUrl;
                      a.download = `match-letter-${userInfo?.username || 'user'}.pdf`;
                      a.click();
                    }}
                      style={{ flex: 1, padding: 10, borderRadius: 10, border: 'none', background: 'linear-gradient(135deg, #3B82F6, #1D4ED8)', color: '#fff', fontWeight: 600, fontSize: 13, cursor: 'pointer' }}>
                      Download PDF
                    </button>
                    <button onClick={() => { const w = window.open(pdfUrl, '_blank'); w?.addEventListener('load', () => w.print()); }}
                      style={{ flex: 1, padding: 10, borderRadius: 10, border: '1.5px solid #E2E8F0', background: '#fff', color: '#334155', fontWeight: 600, fontSize: 13, cursor: 'pointer' }}>
                      Print
                    </button>
                  </div>
                </div>
              )}
            </div>
          )}

          {/* ── Regular step form content ─────────────────────────────── */}
          {!isMatchTab && currentStep && (
            <div>
              <div style={{ fontSize: 16, fontWeight: 700, color: '#0F172A', marginBottom: 20 }}>
                {currentStep.label}
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
                {currentStep.fields.map(renderField)}
              </div>

              <div style={{ marginTop: 24 }}>
                <button onClick={handleSave} disabled={saveMutation.isPending}
                  style={{
                    background: 'linear-gradient(135deg, #3B82F6, #1D4ED8)', color: '#fff', border: 'none',
                    borderRadius: 10, padding: '10px 24px', fontSize: 14, fontWeight: 600,
                    cursor: saveMutation.isPending ? 'not-allowed' : 'pointer', opacity: saveMutation.isPending ? 0.7 : 1,
                  }}>
                  {saveMutation.isPending ? 'Saving...' : 'Save Changes'}
                </button>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default AdminUserEdit;
