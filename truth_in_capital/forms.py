from django.forms import ModelForm
from django import forms
from .models import TruthCapitalType, Task, time
from .models import rating


class TruthCapitalTypeForm(ModelForm):
    class Meta:
        model = TruthCapitalType
        fields = ['capital_type']
        labels = {
            'capital_type': 'Capital Type'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['capital_type'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter capital type name'
        })


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['capital_type', 'task_name', 'task_max_hour', 'task_type', 'task_precedence']
        labels = {
            'capital_type': 'Capital Type',
            'task_name': 'Task Name',
            'task_max_hour': 'Task Hours',
            'task_type': 'Task Type',
            'task_precedence': 'Task Precedence'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['capital_type'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['task_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter task name'
        })
        self.fields['task_max_hour'].widget.attrs.update({
            'class': 'form-control',
            'min': '1',
            'max': '1000'
        })
        self.fields['task_type'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['task_precedence'].widget.attrs.update({
            'class': 'form-control',
            'min': '0'
        })


class TimeForm(ModelForm):
    class Meta:
        model = time
        fields = ['capital_type', 'start_date']
        labels = {
            'start_date': 'Start Date'
        }
        widgets = {
            'start_date': forms.DateInput(attrs={
                'type': 'date', 
                'class': 'form-control'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['capital_type'].widget.attrs.update({
            'class': 'form-control',
        })


class RatingForm(ModelForm):
    class Meta:
        model = rating
        fields = ['task', 'rating']
        labels = {
            'task': 'Task',
            'rating': 'Rating',
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['task'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['rating'].widget.attrs.update({
            'class': 'form-control',
            'min': '0',
            'max': '10',
            'placeholder': 'Enter rating (0-10)'
        })

