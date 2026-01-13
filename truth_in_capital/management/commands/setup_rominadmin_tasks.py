from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from truth_in_capital.models import TruthCapitalType, Task

class Command(BaseCommand):
    help = 'Set up default tasks for rominadmin user for all capital types'

    def handle(self, *args, **options):
        # Get or create rominadmin user
        rominadmin_user, created = User.objects.get_or_create(
            username='rominadmin',
            defaults={
                'email': 'rominadmin@example.com',
                'first_name': 'Romin',
                'last_name': 'Admin',
                'is_staff': True,
                'is_superuser': True
            }
        )
        
        if created:
            rominadmin_user.set_password('admin123')
            rominadmin_user.save()
            self.stdout.write(
                self.style.SUCCESS('Created rominadmin user')
            )
        else:
            self.stdout.write(
                self.style.SUCCESS('rominadmin user already exists')
            )

        # Define the standard tasks for all capital types
        standard_tasks = [
            {'task_name': 'Finfire Report - Capital Type', 'task_max_hour': 4, 'task_type': 'FINFIRE Staff Review & Scope of Work', 'task_precedence': 0},
            {'task_name': 'Financial Model, forecast, pro forma', 'task_max_hour': 20, 'task_type': 'Intermediary Services Scope of Work', 'task_precedence': 0},
            {'task_name': 'Due Diligence Checklist Documents', 'task_max_hour': 4, 'task_type': 'FINFIRE Staff Review & Scope of Work', 'task_precedence': 1},
            {'task_name': 'Historical Financials (P & L, BS, CF, Aging)', 'task_max_hour': 1, 'task_type': 'FINFIRE Staff Review & Scope of Work', 'task_precedence': 1},
            {'task_name': 'Tax Returns (Up to 2 years, if applicable)', 'task_max_hour': 1, 'task_type': 'FINFIRE Staff Review & Scope of Work', 'task_precedence': 1},
            {'task_name': 'Business Valuation (Equity only)', 'task_max_hour': 20, 'task_type': 'Intermediary Services Scope of Work', 'task_precedence': 1},
            {'task_name': 'Cap Table, Use of Funds, & Capitalization Plan', 'task_max_hour': 5, 'task_type': 'Intermediary Services Scope of Work', 'task_precedence': 1},
            {'task_name': 'Executive Summary Including Exit Strategy', 'task_max_hour': 2, 'task_type': 'FINFIRE Staff Review & Scope of Work', 'task_precedence': 2},
            {'task_name': 'Presentation Deck', 'task_max_hour': 10, 'task_type': 'FINFIRE Staff Review & Scope of Work', 'task_precedence': 2},
            {'task_name': 'Business Model Canvas', 'task_max_hour': 2, 'task_type': 'FINFIRE Staff Review & Scope of Work', 'task_precedence': 2},
            {'task_name': 'Resume of Founder/CEO Primary Leader', 'task_max_hour': 1, 'task_type': 'FINFIRE Staff Review & Scope of Work', 'task_precedence': 2},
            {'task_name': 'Application (If Applicable)', 'task_max_hour': 6, 'task_type': 'FINFIRE Staff Review & Scope of Work', 'task_precedence': 2},
            {'task_name': 'Presentation Video (From the AI Deep Dive)', 'task_max_hour': 10, 'task_type': 'Intermediary Services Scope of Work', 'task_precedence': 2},
            {'task_name': 'Offering Documents', 'task_max_hour': 25, 'task_type': 'Intermediary Services Scope of Work', 'task_precedence': 2},
            {'task_name': 'Quality Assurance Checklist (Including AI)', 'task_max_hour': 3, 'task_type': 'FINFIRE Staff Review & Scope of Work', 'task_precedence': 3},
            {'task_name': 'Capital Match List Generated', 'task_max_hour': 10, 'task_type': 'FINFIRE Staff Review & Scope of Work', 'task_precedence': 3},
            {'task_name': 'Investor Marketing Campaign', 'task_max_hour': 20, 'task_type': 'Intermediary Services Scope of Work', 'task_precedence': 4},
            {'task_name': 'Investor Relations', 'task_max_hour': 20, 'task_type': 'Intermediary Services Scope of Work', 'task_precedence': 4},
            {'task_name': 'Progress Reports', 'task_max_hour': 12, 'task_type': 'Intermediary Services Scope of Work', 'task_precedence': 4},
        ]
        
        # All capital types will use the same tasks
        capital_types = [
            'Accelerator', 'Bonds', 'Bootstrapped', 'Commercial Banking', 
            'Cryptocurrency', 'Factoring', 'Grants', 'Hedge Funds', 
            'Incubator', 'Investment Banking', 'Private Debt', 
            'Private Equity Securities', 'Royalty Financing', 
            'Small Business Administration (SBA)', 'Third Party Corporate Credit', 
            'Tokenization', 'Venture Capital'
        ]
        
        default_tasks_by_capital_type = {}
        for capital_type in capital_types:
            default_tasks_by_capital_type[capital_type] = standard_tasks

        # Create capital types and tasks for rominadmin
        for capital_type_name, tasks in default_tasks_by_capital_type.items():
            # Get or create capital type for rominadmin
            capital_type, created = TruthCapitalType.objects.get_or_create(
                user=rominadmin_user,
                capital_type=capital_type_name
            )
            
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created capital type: {capital_type_name}')
                )
            
            # Clear existing tasks for this capital type
            Task.objects.filter(capital_type=capital_type).delete()
            
            # Create new tasks
            for task_data in tasks:
                Task.objects.create(
                    capital_type=capital_type,
                    **task_data
                )
            
            self.stdout.write(
                self.style.SUCCESS(f'Created {len(tasks)} tasks for {capital_type_name}')
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully set up rominadmin tasks for all capital types')
        )
