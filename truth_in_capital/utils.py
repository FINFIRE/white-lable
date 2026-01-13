from django.contrib.auth.models import User
from .models import TruthCapitalType, Task

def ensure_rominadmin_tasks_exist():
    """
    Ensure that rominadmin user has tasks for all capital types.
    This function can be called to set up the template tasks if they don't exist.
    """
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
    
    # Check if rominadmin has any tasks
    existing_tasks = Task.objects.filter(capital_type__user=rominadmin_user).count()
    
    if existing_tasks == 0:
        # Import and run the management command logic
        from .management.commands.setup_rominadmin_tasks import Command
        command = Command()
        command.handle()
        return True
    
    return False

def get_rominadmin_tasks_for_capital_type(capital_type_name):
    """
    Get tasks from rominadmin for a specific capital type
    """
    try:
        rominadmin_user = User.objects.get(username='rominadmin')
        capital_type = TruthCapitalType.objects.get(
            user=rominadmin_user,
            capital_type=capital_type_name
        )
        return Task.objects.filter(capital_type=capital_type).order_by('task_precedence')
    except (User.DoesNotExist, TruthCapitalType.DoesNotExist):
        return []
