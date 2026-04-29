"""
Test script to verify that all capital types use the same unified tasks
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
from truth_in_capital.utils import ensure_rominadmin_tasks_exist

def test_unified_tasks():
    """Test that all capital types use the same tasks"""
    print("Testing unified task structure for all capital types...")
    
    # 1. Ensure rominadmin tasks exist
    print("1. Setting up rominadmin tasks...")
    ensure_rominadmin_tasks_exist()
    
    # 2. Get rominadmin user
    rominadmin_user = User.objects.get(username='rominadmin')
    
    # 3. Test a few different capital types
    test_capital_types = ['Venture Capital', 'Cryptocurrency', 'Bonds', 'Accelerator']
    
    expected_tasks = [
        'Finfire Report - Capital Type',
        'Financial Model, forecast, pro forma',
        'Due Diligence Checklist Documents',
        'Historical Financials (P & L, BS, CF, Aging)',
        'Tax Returns (Up to 2 years, if applicable)',
        'Business Valuation (Equity only)',
        'Cap Table, Use of Funds, & Capitalization Plan',
        'Executive Summary Including Exit Strategy',
        'Presentation Deck',
        'Business Model Canvas',
        'Resume of Founder/CEO Primary Leader',
        'Application (If Applicable)',
        'Presentation Video (From the AI Deep Dive)',
        'Offering Documents',
        'Quality Assurance Checklist (Including AI)',
        'Capital Match List Generated',
        'Investor Marketing Campaign',
        'Investor Relations',
        'Progress Reports'
    ]
    
    for capital_type_name in test_capital_types:
        print(f"\n2. Testing {capital_type_name}...")
        
        # Get the capital type
        capital_type = TruthCapitalType.objects.get(
            user=rominadmin_user,
            capital_type=capital_type_name
        )
        
        # Get tasks
        tasks = Task.objects.filter(capital_type=capital_type).order_by('task_precedence')
        print(f"   Found {tasks.count()} tasks")
        
        # Verify task names
        actual_task_names = [task.task_name for task in tasks]
        if actual_task_names == expected_tasks:
            print(f"   ✅ {capital_type_name} has correct tasks")
        else:
            print(f"   ❌ {capital_type_name} has incorrect tasks")
            print(f"   Expected: {expected_tasks}")
            print(f"   Actual: {actual_task_names}")
        
        # Show task details
        for task in tasks:
            print(f"   - {task.task_name} ({task.task_max_hour} hours, precedence: {task.task_precedence})")
    
    # 4. Test that all capital types exist
    print("\n3. Verifying all 17 capital types exist...")
    all_capital_types = TruthCapitalType.objects.filter(user=rominadmin_user)
    print(f"   Found {all_capital_types.count()} capital types for rominadmin")
    
    if all_capital_types.count() == 17:
        print("   ✅ All 17 capital types exist")
    else:
        print("   ❌ Missing some capital types")
    
    # 5. Verify all have the same number of tasks
    print("\n4. Verifying all capital types have the same number of tasks...")
    task_counts = []
    for capital_type in all_capital_types:
        task_count = Task.objects.filter(capital_type=capital_type).count()
        task_counts.append(task_count)
        print(f"   {capital_type.capital_type}: {task_count} tasks")
    
    if len(set(task_counts)) == 1 and task_counts[0] == 19:
        print("   ✅ All capital types have exactly 19 tasks")
    else:
        print("   ❌ Inconsistent task counts")
    
    print("\n✅ Unified task structure test completed successfully!")

if __name__ == '__main__':
    test_unified_tasks()
