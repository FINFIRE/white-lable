from django.test import TestCase
from django.contrib.auth.models import User
from .models import TruthCapitalType, Task, time
from datetime import date, timedelta
from Algorithm.models import capitalTypes

# Create your tests here.
class TruthCapitalTypeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_create_truth_capital_type(self):
        capital_type = TruthCapitalType.objects.create(user=self.user, capital_type='Equity')
        self.assertEqual(capital_type.user, self.user)
        self.assertEqual(capital_type.capital_type, 'Equity')

    def test_unique_together_constraint(self):
        TruthCapitalType.objects.create(user=self.user, capital_type='Debt')
        with self.assertRaises(Exception):
            # Should raise IntegrityError on duplicate
            TruthCapitalType.objects.create(user=self.user, capital_type='Debt')

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser2', password='testpass2')
        self.capital_type = capitalTypes.objects.create(name='Convertible Note')

    def test_create_task(self):
        task = Task.objects.create(
            capital_type=self.capital_type,
            task_name='Review Documents',
            task_hour=5
        )
        self.assertEqual(task.capital_type, self.capital_type)
        self.assertEqual(task.task_name, 'Review Documents')
        self.assertEqual(task.task_hour, 5)

    def test_user_property(self):
        task = Task.objects.create(
            capital_type=self.capital_type,
            task_name='Prepare Pitch',
            task_hour=2
        )
        self.assertEqual(task.user, self.user)

    def test_related_name_tasks(self):
        Task.objects.create(capital_type=self.capital_type, task_name='A', task_hour=1)
        Task.objects.create(capital_type=self.capital_type, task_name='B', task_hour=2)
        self.assertEqual(self.capital_type.tasks.count(), 2)

    def test_multiple_tasks_for_capitaltype(self):
        # Create multiple tasks for the same capital type
        names = ['Task1', 'Task2', 'Task3', 'Task4']
        hours = [1, 2, 3, 4]
        for n, h in zip(names, hours):
            Task.objects.create(capital_type=self.capital_type, task_name=n, task_hour=h)
        tasks = self.capital_type.tasks.all()
        self.assertEqual(tasks.count(), 4)
        self.assertListEqual(
            sorted([t.task_name for t in tasks]),
            sorted(names)
        )
        self.assertListEqual(
            sorted([t.task_hour for t in tasks]),
            sorted(hours)
        )

class TimeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser3', password='testpass3')

    def test_create_time(self):
        t = time.objects.create(
            user=self.user,
            start_date=date(2024, 1, 1),
            duration_capital_weeks=timedelta(weeks=4)
        )
        self.assertEqual(t.user, self.user)
        self.assertEqual(t.start_date, date(2024, 1, 1))
        self.assertEqual(t.duration_capital_weeks, timedelta(weeks=4))
