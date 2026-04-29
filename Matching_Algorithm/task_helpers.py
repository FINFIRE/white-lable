"""
Task and capital type creation helpers for the Matching Algorithm.

Contains functions for creating TruthCapitalType records and associated
default tasks when a user is matched to a capital type.
"""
from datetime import timedelta
from django.utils import timezone
from truth_in_capital.models import TruthCapitalType, Task, time as TruthTime, rating as TaskRating
from truth_in_capital.utils import ensure_rominadmin_tasks_exist, get_rominadmin_tasks_for_capital_type
from entreprise_questions.models import PreRating


# ──────────────────────────────────────────────────────────────────────
# Default task definitions used when no rominadmin template is available
# ──────────────────────────────────────────────────────────────────────
DEFAULT_TASKS = [
    {'task_name': 'Finfire Report - Capital Type', 'task_max_hour': 4,
     'task_type': 'FINFIRE Staff Review & Scope of Work', 'task_precedence': 0},
    {'task_name': 'Financial Model, forecast, pro forma', 'task_max_hour': 20,
     'task_type': 'Intermediary Services Scope of Work', 'task_precedence': 0},
    {'task_name': 'Due Diligence Checklist Documents', 'task_max_hour': 4,
     'task_type': 'FINFIRE Staff Review & Scope of Work', 'task_precedence': 1},
    {'task_name': 'Historical Financials (P & L, BS, CF, Aging)', 'task_max_hour': 1,
     'task_type': 'FINFIRE Staff Review & Scope of Work', 'task_precedence': 1},
    {'task_name': 'Tax Returns (Up to 2 years, if applicable)', 'task_max_hour': 1,
     'task_type': 'FINFIRE Staff Review & Scope of Work', 'task_precedence': 1},
    {'task_name': 'Business Valuation (Equity only)', 'task_max_hour': 20,
     'task_type': 'Intermediary Services Scope of Work', 'task_precedence': 1},
    {'task_name': 'Cap Table, Use of Funds, & Capitalization Plan', 'task_max_hour': 5,
     'task_type': 'Intermediary Services Scope of Work', 'task_precedence': 1},
    {'task_name': 'Executive Summary Including Exit Strategy', 'task_max_hour': 2,
     'task_type': 'FINFIRE Staff Review & Scope of Work', 'task_precedence': 2},
    {'task_name': 'Presentation Deck', 'task_max_hour': 10,
     'task_type': 'FINFIRE Staff Review & Scope of Work', 'task_precedence': 2},
    {'task_name': 'Business Model Canvas', 'task_max_hour': 2,
     'task_type': 'FINFIRE Staff Review & Scope of Work', 'task_precedence': 2},
    {'task_name': 'Resume of Founder/CEO Primary Leader', 'task_max_hour': 1,
     'task_type': 'FINFIRE Staff Review & Scope of Work', 'task_precedence': 2},
    {'task_name': 'Application (If Applicable)', 'task_max_hour': 6,
     'task_type': 'FINFIRE Staff Review & Scope of Work', 'task_precedence': 2},
    {'task_name': 'Presentation Video (From the AI Deep Dive)', 'task_max_hour': 10,
     'task_type': 'Intermediary Services Scope of Work', 'task_precedence': 2},
    {'task_name': 'Offering Documents', 'task_max_hour': 25,
     'task_type': 'Intermediary Services Scope of Work', 'task_precedence': 2},
    {'task_name': 'Quality Assurance Checklist (Including AI)', 'task_max_hour': 3,
     'task_type': 'FINFIRE Staff Review & Scope of Work', 'task_precedence': 3},
    {'task_name': 'Capital Match List Generated', 'task_max_hour': 10,
     'task_type': 'FINFIRE Staff Review & Scope of Work', 'task_precedence': 3},
    {'task_name': 'Investor Marketing Campaign', 'task_max_hour': 20,
     'task_type': 'Intermediary Services Scope of Work', 'task_precedence': 4},
    {'task_name': 'Investor Relations', 'task_max_hour': 20,
     'task_type': 'Intermediary Services Scope of Work', 'task_precedence': 4},
    {'task_name': 'Progress Reports', 'task_max_hour': 12,
     'task_type': 'Intermediary Services Scope of Work', 'task_precedence': 4},
]


def create_standard_default_tasks(capital_type):
    """Create standard default tasks when no rominadmin template is available."""
    for task_data in DEFAULT_TASKS:
        Task.objects.create(capital_type=capital_type, **task_data)


def create_default_tasks_for_capital_type(capital_type):
    """Create default tasks for a new capital type based on rominadmin's tasks."""
    try:
        ensure_rominadmin_tasks_exist()
        rominadmin_tasks = get_rominadmin_tasks_for_capital_type("Private Equity Securities")

        if rominadmin_tasks:
            for task in rominadmin_tasks:
                Task.objects.create(
                    capital_type=capital_type,
                    task_name=task.task_name,
                    task_max_hour=task.task_max_hour,
                    task_type=task.task_type,
                    task_precedence=task.task_precedence,
                )
            return

        create_standard_default_tasks(capital_type)
    except Exception as e:
        print(f"Error creating default tasks for capital type {capital_type.id}: {e}")
        create_standard_default_tasks(capital_type)


def _sync_pre_ratings(user, capital_type):
    """Sync task ratings from PreRating records if available."""
    try:
        pre = PreRating.objects.filter(user=user).first()
        if pre and isinstance(pre.preratings, dict):
            for task in Task.objects.filter(capital_type=capital_type):
                if task.task_name in pre.preratings:
                    try:
                        rating_value = int(pre.preratings[task.task_name])
                    except (TypeError, ValueError):
                        continue
                    if 0 <= rating_value <= 10:
                        TaskRating.objects.update_or_create(
                            task=task, defaults={"rating": rating_value},
                        )
    except Exception as e:
        print(f"Error syncing pre-ratings for user {user.id}: {e}")


def create_capital_type_for_user(user, cm1name):
    """Create or update a TruthCapitalType record for a user and associated tasks."""
    try:
        existing = TruthCapitalType.objects.filter(user=user).first()

        if existing:
            existing.capital_type = cm1name
            existing.save()
            capital_type = existing
        else:
            capital_type = TruthCapitalType.objects.create(user=user, capital_type=cm1name)
            create_default_tasks_for_capital_type(capital_type)

        # Create timing record (start_date = matched_date + 7 days)
        matched_date_plus_7 = timezone.now().date() + timedelta(days=7)
        TruthTime.objects.get_or_create(
            capital_type=capital_type,
            defaults={"start_date": matched_date_plus_7},
        )

        _sync_pre_ratings(user, capital_type)

    except Exception as e:
        print(f"Error creating capital type for user {user.id}: {e}")
