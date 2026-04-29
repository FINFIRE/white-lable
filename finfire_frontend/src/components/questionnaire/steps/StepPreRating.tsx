import React, { useEffect } from 'react';
import { useForm, Controller } from 'react-hook-form';
import { useQuery, useMutation } from '@tanstack/react-query';
import axios from 'axios';
import { getPreRating, postPreRating } from '../../../api/questionnaire';
import RangeSlider from '../../ui/RangeSlider';
import LoadingSpinner from '../../ui/LoadingSpinner';

interface Props {
  onComplete: () => void;
}

const FORM_ID = 'questionnaire-step-form';

/**
 * 19 rating fields from the Django RatingForm.
 * Each is rated 0–10 via a slider.
 */
const RATING_FIELDS: { key: string; label: string; tooltip: string }[] = [
  {
    key: 'financial_model_forecast_pro_forma',
    label: 'Financial Model, Forecast, Pro Forma',
    tooltip: 'Rate the completion of this task on a scale of 0-10.',
  },
  {
    key: 'finfire_report_capital_type',
    label: 'Finfire Report - Capital Type',
    tooltip: 'Rate the completion of this task on a scale of 0-10.',
  },
  {
    key: 'due_diligence_checklist_documents',
    label: 'Due Diligence Checklist Documents',
    tooltip: 'Rate the completion of this task on a scale of 0-10.',
  },
  {
    key: 'historical_financials',
    label: 'Historical Financials (P & L, BS, CF, Aging)',
    tooltip: 'Rate the completion of this task on a scale of 0-10.',
  },
  {
    key: 'tax_returns',
    label: 'Tax Returns (Up to 2 years, if applicable)',
    tooltip: 'Rate the completion of this task on a scale of 0-10.',
  },
  {
    key: 'business_valuation_equity_only',
    label: 'Business Valuation (Equity only)',
    tooltip: 'Rate the completion of this task on a scale of 0-10.',
  },
  {
    key: 'cap_table_use_of_funds_and_capitalization_plan',
    label: 'Cap Table, Use of Funds, & Capitalization Plan',
    tooltip: 'Rate the completion of this task on a scale of 0-10.',
  },
  {
    key: 'business_model_canvas',
    label: 'Business Model Canvas',
    tooltip: 'Rate the completion of this task on a scale of 0-10.',
  },
  {
    key: 'offering_documents_rating',
    label: 'Offering Documents',
    tooltip: 'Rate the completion of this task on a scale of 0-10.',
  },
  {
    key: 'presentation_video_ai_deep_dive',
    label: 'Presentation Video (From the AI Deep Dive)',
    tooltip: 'Rate the completion of this task on a scale of 0-10.',
  },
  {
    key: 'application_if_applicable',
    label: 'Application (If Applicable)',
    tooltip: 'Rate the completion of this task on a scale of 0-10.',
  },
  {
    key: 'resume_of_founder_ceo_primary_leader',
    label: 'Resume of Founder/CEO Primary Leader',
    tooltip: 'Rate the completion of this task on a scale of 0-10.',
  },
  {
    key: 'presentation_deck_rating',
    label: 'Presentation Deck',
    tooltip: 'Rate the completion of this task on a scale of 0-10.',
  },
  {
    key: 'executive_summary_including_exit_strategy',
    label: 'Executive Summary Including Exit Strategy',
    tooltip: 'Rate the completion of this task on a scale of 0-10.',
  },
  {
    key: 'quality_assurance_checklist_including_ai',
    label: 'Quality Assurance Checklist (Including AI)',
    tooltip: 'Rate the completion of this task on a scale of 0-10.',
  },
  {
    key: 'capital_match_list_generated',
    label: 'Capital Match List Generated',
    tooltip: 'Rate the completion of this task on a scale of 0-10.',
  },
  {
    key: 'investor_marketing_campaign',
    label: 'Investor Marketing Campaign',
    tooltip: 'Rate the completion of this task on a scale of 0-10.',
  },
  {
    key: 'investor_relations',
    label: 'Investor Relations',
    tooltip: 'Rate the completion of this task on a scale of 0-10.',
  },
  {
    key: 'progress_reports',
    label: 'Progress Reports',
    tooltip: 'Rate the completion of this task on a scale of 0-10.',
  },
];

interface PreRatingFormValues {
  preratings: Record<string, number>;
}

const StepPreRating: React.FC<Props> = ({ onComplete }) => {
  const { control, handleSubmit, reset } = useForm<PreRatingFormValues>({
    defaultValues: {
      preratings: Object.fromEntries(
        RATING_FIELDS.map((f) => [f.key, 0])
      ),
    },
  });

  const { data: existing, isLoading } = useQuery({
    queryKey: ['preRating'],
    queryFn: getPreRating,
    retry: false,
  });

  useEffect(() => {
    if (existing?.preratings) {
      const parsed =
        typeof existing.preratings === 'string'
          ? JSON.parse(existing.preratings)
          : existing.preratings;
      const merged: Record<string, number> = {};
      for (const f of RATING_FIELDS) {
        merged[f.key] =
          typeof parsed[f.key] === 'number' ? parsed[f.key] : 0;
      }
      reset({ preratings: merged });
    }
  }, [existing, reset]);

  const mutation = useMutation({
    mutationFn: (values: PreRatingFormValues) =>
      postPreRating({ preratings: values.preratings }),
    onSuccess: () => onComplete(),
    onError: (error: unknown) => {
      if (axios.isAxiosError(error) && error.response?.status === 409) {
        onComplete();
      }
    },
  });

  const onSubmit = (data: PreRatingFormValues) => {
    mutation.mutate(data);
  };

  if (isLoading) {
    return (
      <div className="flex items-center justify-center py-12">
        <LoadingSpinner />
      </div>
    );
  }

  return (
    <form
      id={FORM_ID}
      onSubmit={handleSubmit(onSubmit)}
      className="space-y-5"
    >
      <p className="text-sm text-slate-500 mb-2">
        Rate each item on a scale of 0 to 10. 10 indicates the task is fully
        completed; 0 indicates it has not been initiated.
      </p>

      {RATING_FIELDS.map((field) => (
        <Controller
          key={field.key}
          name={`preratings.${field.key}`}
          control={control}
          render={({ field: formField }) => (
            <RangeSlider
              name={field.key}
              label={field.label}
              tooltip={field.tooltip}
              value={typeof formField.value === 'number' ? formField.value : 0}
              onChange={formField.onChange}
              min={0}
              max={10}
            />
          )}
        />
      ))}

      {mutation.isError && !axios.isAxiosError(mutation.error) && (
        <p className="text-sm text-red-600">
          Something went wrong. Please try again.
        </p>
      )}
    </form>
  );
};

export default StepPreRating;
