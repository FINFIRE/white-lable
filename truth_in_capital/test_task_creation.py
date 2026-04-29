"""
Test script to verify the task creation functionality
"""
import os
import sys
import django

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finfire_whitelable.settings')
django.setup()

from django.contrib.auth.models import User
from truth_in_capital.models import TruthCapitalType, Task
from truth_in_capital.utils import ensure_rominadmin_tasks_exist, get_rominadmin_tasks_for_capital_type

def test_task_creation():
    """Test the task creation functionality"""
    print("Testing task creation functionality...")
    
    # 1. Ensure rominadmin tasks exist
    print("1. Setting up rominadmin tasks...")
    ensure_rominadmin_tasks_exist()
    
    # 2. Create a test user
    print("2. Creating test user...")
    test_user, created = User.objects.get_or_create(
        username='testuser_task_creation',
        defaults={
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        }
    )
    
    if created:
        test_user.set_password('testpass123')
        test_user.save()
        print(f"   Created test user: {test_user.username}")
    else:
        print(f"   Test user already exists: {test_user.username}")
    
    # 3. Create a capital type for the test user
    print("3. Creating capital type for test user...")
    capital_type, created = TruthCapitalType.objects.get_or_create(
        user=test_user,
        capital_type='Venture Capital'
    )
    
    if created:
        print(f"   Created capital type: {capital_type.capital_type}")
    else:
        print(f"   Capital type already exists: {capital_type.capital_type}")
    
    # 4. Check if tasks were created
    tasks = Task.objects.filter(capital_type=capital_type)
    print(f"4. Found {tasks.count()} tasks for the test user")
    
    for task in tasks:
        print(f"   - {task.task_name} ({task.task_max_hour} hours, precedence: {task.task_precedence})")
    
    # 5. Test getting rominadmin tasks
    print("5. Testing rominadmin task retrieval...")
    rominadmin_tasks = get_rominadmin_tasks_for_capital_type('Venture Capital')
    print(f"   Found {rominadmin_tasks.count()} rominadmin tasks for Venture Capital")
    
    for task in rominadmin_tasks:
        print(f"   - {task.task_name} ({task.task_max_hour} hours, precedence: {task.task_precedence})")
    
    # 6. Clean up test user
    print("6. Cleaning up test user...")
    test_user.delete()
    print("   Test user deleted")
    
    print("\n✅ Task creation test completed successfully!")

if __name__ == '__main__':
    test_task_creation()
