from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import TruthCapitalType, Task, time
from .forms import TruthCapitalTypeForm, TaskForm, TimeForm
from .forms import RatingForm
from .models import rating
from entreprise_questions.models import EQuestions2,EQuestions5
from entreprise_questions.forms import RatingForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from datetime import timedelta
from django.http import HttpResponse
from django.db import IntegrityError
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from openpyxl.utils import get_column_letter

def rating_converter(r):
    """
    Convert a rating from 0-10 scale to its inverted equivalent.
    For example: 0->10, 1->9, 2->8, 3->7, 4->6, 5->5, 6->4, 7->3, 8->2, 9->1, 10->0
    """
    # Ensure the rating is within the valid range (0-10)
    if not isinstance(r, int) or r < 0 or r > 10:
        raise ValueError("Rating must be an integer between 0 and 10")
    
    # Convert to inverted scale: 10 - rating
    return 10 - r

@login_required
def dashboard(request):
    """Main dashboard view showing user's capital types and tasks"""
    user_capital_types = TruthCapitalType.objects.filter(user=request.user)
    user_times = time.objects.filter(capital_type__user=request.user)
    
    context = {
        'capital_types': user_capital_types,
        'times': user_times,
    }
    return render(request, 'truth_in_capital/dashboard.html', context)


# TruthCapitalType Views
@login_required
def capital_type_list(request):
    """List all capital types for the current user or all if admin"""
    query = request.GET.get('q', '').strip()
    if request.user.is_staff:
        capital_types = TruthCapitalType.objects.all()
    else:
        capital_types = TruthCapitalType.objects.filter(user=request.user)

    if query:
        from django.db.models import Q
        capital_types = capital_types.filter(
            Q(capital_type__icontains=query) |
            Q(user__username__icontains=query)
        )
    return render(request, 'truth_in_capital/capital_type_list.html', {'capital_types': capital_types})


@login_required
def capital_type_create(request):
    """Create a new capital type"""
    users = None
    if request.user.is_staff:
        users = User.objects.all()
    if request.method == 'POST':
        form = TruthCapitalTypeForm(request.POST)
        if form.is_valid():
            capital_type = form.save(commit=False)
            if request.user.is_staff:
                user_id = request.POST.get('user')
                if user_id:
                    capital_type.user = User.objects.get(pk=user_id)
                else:
                    capital_type.user = request.user
            else:
                capital_type.user = request.user
            try:
                capital_type.save()
            except IntegrityError:
                return HttpResponse('This user is already associated with this capital type. Duplicate entry not allowed.')
            messages.success(request, 'Capital type created successfully!')
            return redirect('truth_in_capital:capital_type_list')
    else:
        form = TruthCapitalTypeForm()
    return render(request, 'truth_in_capital/capital_type_form.html', {'form': form, 'title': 'Create Capital Type', 'users': users})


@login_required
def capital_type_update(request, pk):
    """Update an existing capital type"""
    if request.user.is_staff:
        capital_type = get_object_or_404(TruthCapitalType, pk=pk)
    else:
        capital_type = get_object_or_404(TruthCapitalType, pk=pk, user=request.user)
    users = None
    if request.user.is_staff:
        users = User.objects.all()
    if request.method == 'POST':
        form = TruthCapitalTypeForm(request.POST, instance=capital_type)
        if form.is_valid():
            capital_type = form.save(commit=False)
            if request.user.is_staff:
                user_id = request.POST.get('user')
                if user_id:
                    capital_type.user = User.objects.get(pk=user_id)
            capital_type.save()
            messages.success(request, 'Capital type updated successfully!')
            return redirect('truth_in_capital:capital_type_list')
    else:
        form = TruthCapitalTypeForm(instance=capital_type)
    return render(request, 'truth_in_capital/capital_type_form.html', {
        'form': form, 
        'title': 'Update Capital Type',
        'capital_type': capital_type,
        'users': users
    })


@login_required
def capital_type_delete(request, pk):
    """Delete a capital type"""
    if request.user.is_staff:
        capital_type = get_object_or_404(TruthCapitalType, pk=pk)
    else:
        capital_type = get_object_or_404(TruthCapitalType, pk=pk, user=request.user)
    if request.method == 'POST':
        capital_type.delete()
        messages.success(request, 'Capital type deleted successfully!')
        return redirect('truth_in_capital:capital_type_list')
    return render(request, 'truth_in_capital/capital_type_confirm_delete.html', {'capital_type': capital_type})


# Task Views
@login_required
def task_list(request, capital_type_pk=None):
    """List tasks for a specific capital type or all tasks for user/admin"""
    query = request.GET.get('q', '').strip()
    if capital_type_pk:
        if request.user.is_staff:
            capital_type = get_object_or_404(TruthCapitalType, pk=capital_type_pk)
            ratings = rating.objects.filter(task__capital_type=capital_type)
            tasks = Task.objects.filter(capital_type=capital_type)
        else:
            capital_type = get_object_or_404(TruthCapitalType, pk=capital_type_pk, user=request.user)
            ratings = rating.objects.filter(task__capital_type=capital_type, task__capital_type__user=request.user)
            tasks = Task.objects.filter(capital_type=capital_type)
        context = {'tasks': tasks, 'capital_type': capital_type, 'ratings': ratings}
    else:
        if request.user.is_staff:
            tasks = Task.objects.all()
            ratings = rating.objects.all()
        else:
            tasks = Task.objects.filter(capital_type__user=request.user)
            ratings = rating.objects.filter(task__capital_type__user=request.user)
        context = {'tasks': tasks, 'ratings': ratings}

    if query:
        from django.db.models import Q
        context['tasks'] = context['tasks'].filter(
            Q(task_name__icontains=query) |
            Q(capital_type__capital_type__icontains=query) |
            Q(task_type__icontains=query) |
            Q(capital_type__user__username__icontains=query)
        )
        # Filter ratings in sync with filtered tasks
        task_ids = context['tasks'].values_list('id', flat=True)
        context['ratings'] = context['ratings'].filter(task_id__in=task_ids)
    return render(request, 'truth_in_capital/task_list.html', context)


@login_required
def task_create(request, capital_type_pk=None):
    """Create a new task"""
    capital_type = None
    if capital_type_pk:
        if request.user.is_staff:
            capital_type = get_object_or_404(TruthCapitalType, pk=capital_type_pk)
        else:
            capital_type = get_object_or_404(TruthCapitalType, pk=capital_type_pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            if not request.user.is_staff:
                # Ensure the selected capital_type belongs to the user
                if task.capital_type.user != request.user:
                    messages.error(request, 'Invalid capital type selection.')
                    return redirect('truth_in_capital:task_create')
            if capital_type:
                task.capital_type = capital_type
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('truth_in_capital:task_list_by_capital_type', capital_type_pk=task.capital_type.pk)
    else:
        form = TaskForm()
        if not request.user.is_staff:
            form.fields['capital_type'].queryset = TruthCapitalType.objects.filter(user=request.user)
        # If capital_type is provided, set it as initial value and hide the field
        if capital_type:
            form.fields['capital_type'].initial = capital_type
            form.fields['capital_type'].widget.attrs['readonly'] = 'readonly'
            form.fields['capital_type'].widget.attrs['style'] = 'background-color: #e9ecef;'
    return render(request, 'truth_in_capital/task_form.html', {
        'form': form,
        'title': 'Create Task',
        'capital_type': capital_type
    })


@login_required
def task_update(request, pk):
    """Update an existing task"""
    if request.user.is_staff:
        task = get_object_or_404(Task, pk=pk)
    else:
        task = get_object_or_404(Task, pk=pk, capital_type__user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            if not request.user.is_staff:
                if task.capital_type.user != request.user:
                    messages.error(request, 'Invalid capital type selection.')
                    return redirect('truth_in_capital:task_update', pk=pk)
            task.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('truth_in_capital:task_list_by_capital_type', capital_type_pk=task.capital_type.pk)
    else:
        form = TaskForm(instance=task)
        if not request.user.is_staff:
            form.fields['capital_type'].queryset = TruthCapitalType.objects.filter(user=request.user)
    return render(request, 'truth_in_capital/task_form.html', {
        'form': form,
        'title': 'Update Task',
        'task': task
    })


@login_required
def task_delete(request, pk):
    """Delete a task"""
    if request.user.is_staff:
        task = get_object_or_404(Task, pk=pk)
    else:
        task = get_object_or_404(Task, pk=pk, capital_type__user=request.user)
    if request.method == 'POST':
        capital_type_pk = task.capital_type.pk
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('truth_in_capital:task_list_by_capital_type', capital_type_pk=int(capital_type_pk))
    return render(request, 'truth_in_capital/task_confirm_delete.html', {'task': task})


# Time Views
@login_required
def time_list(request):
    """List all time entries for the current user or all if admin"""
    query = request.GET.get('q', '').strip()
    if request.user.is_staff:
        times = time.objects.all()
    else:
        times = time.objects.filter(capital_type__user=request.user)

    if query:
        from django.db.models import Q
        # Support searching by capital type label or username
        times = times.filter(
            Q(capital_type__capital_type__icontains=query) |
            Q(capital_type__user__username__icontains=query)
        )
    return render(request, 'truth_in_capital/time_list.html', {'times': times})


@login_required
def time_create(request):
    """Create a new time entry"""
    users = None  # No longer needed for time
    if request.method == 'POST':
        form = TimeForm(request.POST)
        if form.is_valid():
            time_entry = form.save(commit=False)
            # Ensure the selected capital_type belongs to the user (unless admin)
            if not request.user.is_staff:
                if time_entry.capital_type.user != request.user:
                    messages.error(request, 'Invalid capital type selection.')
                    return redirect('truth_in_capital:time_create')
            time_entry.save()
            messages.success(request, 'Time entry created successfully!')
            return redirect('truth_in_capital:time_list')
    else:
        form = TimeForm()
        # Limit capital_type choices to user's own if not admin
        if not request.user.is_staff:
            form.fields['capital_type'].queryset = TruthCapitalType.objects.filter(user=request.user)
    return render(request, 'truth_in_capital/time_form.html', {'form': form, 'title': 'Create Time Entry'})


@login_required
def time_update(request, pk):
    """Update an existing time entry"""
    if request.user.is_staff:
        time_entry = get_object_or_404(time, pk=pk)
    else:
        time_entry = get_object_or_404(time, pk=pk, capital_type__user=request.user)
    if request.method == 'POST':
        form = TimeForm(request.POST, instance=time_entry)
        if form.is_valid():
            time_entry = form.save(commit=False)
            # Ensure the selected capital_type belongs to the user (unless admin)
            if not request.user.is_staff:
                if time_entry.capital_type.user != request.user:
                    messages.error(request, 'Invalid capital type selection.')
                    return redirect('truth_in_capital:time_update', pk=pk)
            time_entry.save()
            messages.success(request, 'Time entry updated successfully!')
            return redirect('truth_in_capital:time_list')
    else:
        form = TimeForm(instance=time_entry)
        if not request.user.is_staff:
            form.fields['capital_type'].queryset = TruthCapitalType.objects.filter(user=request.user)
    return render(request, 'truth_in_capital/time_form.html', {
        'form': form,
        'title': 'Update Time Entry',
        'time_entry': time_entry
    })


@login_required
def time_delete(request, pk):
    """Delete a time entry"""
    if request.user.is_staff:
        time_entry = get_object_or_404(time, pk=pk)
    else:
        time_entry = get_object_or_404(time, pk=pk, capital_type__user=request.user)
    if request.method == 'POST':
        time_entry.delete()
        messages.success(request, 'Time entry deleted successfully!')
        return redirect('truth_in_capital:time_list')
    return render(request, 'truth_in_capital/time_confirm_delete.html', {'time_entry': time_entry})


# Add CRUD views for rating
@login_required
def rating_list(request):
    query = request.GET.get('q', '').strip()
    if request.user.is_staff:
        ratings = rating.objects.all()
    else:
        ratings = rating.objects.filter(task__capital_type__user=request.user)

    if query:
        from django.db.models import Q
        ratings = ratings.filter(
            Q(task__task_name__icontains=query) |
            Q(task__capital_type__capital_type__icontains=query) |
            Q(task__task_type__icontains=query) |
            Q(task__capital_type__user__username__icontains=query)
        )
    return render(request, 'truth_in_capital/rating_list.html', {'ratings': ratings})

@login_required
def rating_create(request):
    task_id = request.GET.get('task_id')
    initial = {}
    if task_id:
        try:
            task_instance = Task.objects.get(pk=task_id)
            initial['task'] = task_instance
        except Task.DoesNotExist:
            pass
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save()
            task_instance = form.cleaned_data['task']
            messages.success(request, 'Rating created successfully!')
            return redirect('truth_in_capital:task_list_by_capital_type', capital_type_pk=task_instance.capital_type.pk)
    else:
        form = RatingForm(initial=initial)
        if not request.user.is_staff:
            form.fields['task'].queryset = Task.objects.filter(capital_type__user=request.user)
    return render(request, 'truth_in_capital/rating_form.html', {'form': form, 'title': 'Create Rating'})

@login_required
def rating_update(request, pk):
    rating_obj = get_object_or_404(rating, pk=pk)
    if not request.user.is_staff and rating_obj.task.capital_type.user != request.user:
        messages.error(request, 'Permission denied.')
        return redirect('truth_in_capital:rating_list')
    if request.method == 'POST':
        form = RatingForm(request.POST, instance=rating_obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rating updated successfully!')
            return redirect('truth_in_capital:task_list_by_capital_type', capital_type_pk=rating_obj.task.capital_type.pk)
    else:
        form = RatingForm(instance=rating_obj)
        if not request.user.is_staff:
            form.fields['task'].queryset = Task.objects.filter(capital_type__user=request.user)
    return render(request, 'truth_in_capital/rating_form.html', {'form': form, 'title': 'Update Rating', 'rating_obj': rating_obj})

@login_required
def rating_delete(request, pk):
    rating_obj = get_object_or_404(rating, pk=pk)
    if not request.user.is_staff and rating_obj.task.capital_type.user != request.user:
        messages.error(request, 'Permission denied.')
        return redirect('truth_in_capital:rating_list')
    if request.method == 'POST':
        rating_obj.delete()
        messages.success(request, 'Rating deleted successfully!')
        return redirect('truth_in_capital:task_list_by_capital_type', capital_type_pk=rating_obj.task.capital_type.pk)
    return render(request, 'truth_in_capital/rating_confirm_delete.html', {'rating_obj': rating_obj})


# AJAX Views for dynamic functionality
@login_required
@require_POST
def reorder_tasks(request):
    """Reorder tasks via AJAX"""
    try:
        task_ids = request.POST.getlist('task_ids[]')
        for index, task_id in enumerate(task_ids):
            Task.objects.filter(
                pk=task_id, 
                capital_type__user=request.user
            ).update(task_precedence=index)
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})


@login_required
def excel_template_view(request, user_id=None):
    User = get_user_model()
    query = request.GET.get('q', '').strip()
    
    # If no user_id provided, show user selection page
    if not user_id:
        if request.user.is_staff:
            # Staff users can see all users who have capital types
            users = User.objects.filter(truthcapitaltype__isnull=False).distinct()
            if query:
                from django.db.models import Q
                users = users.filter(
                    Q(username__icontains=query) |
                    Q(first_name__icontains=query) |
                    Q(last_name__icontains=query)
                )
            context = {
                'users': users,
                'q': query,
            }
            return render(request, 'truth_in_capital/user_selection.html', context)
        else:
            # Non-staff users can only see their own data
            # Redirect to their own excel template
            return redirect('truth_in_capital:excel_template_for_user', user_id=request.user.id)
    
    # Get the selected user
    selected_user = get_object_or_404(User, pk=user_id)
    
    # Security check: Non-staff users can only access their own data
    if not request.user.is_staff and selected_user != request.user:
        return redirect('truth_in_capital:excel_template_for_user', user_id=request.user.id)
    
    try:
        capital_types = TruthCapitalType.objects.filter(user=selected_user)
        try:
            base_tasks = Task.objects.filter(capital_type__user=selected_user)
        except:
            return HttpResponse('No task found go back and fill in task.')
        try:
            times = time.objects.filter(capital_type__user=selected_user)
        except:
            return HttpResponse('No time found go back and fill in time for the user.')
        try:
            base_ratings = rating.objects.filter(task__capital_type__user=selected_user)
        except:
            return HttpResponse('No rating found go back and rate all tasks.')
        try:
            business_name = EQuestions2.objects.filter(user=selected_user).first().Business_Name
        except:
            return HttpResponse('No business name found go back and fill in business name for the user in superuser dashboard.')
        capital_name = capital_types.first().capital_type
        try:
            raisegoal = EQuestions5.objects.filter(user=selected_user).first().Selected_Option
        except:
            return HttpResponse('No raisegoal found go back and fill in raisegoal for the user in superuser dashboard.')
        per_match = 20
        task_dict = {}
    except Exception as e:
        return HttpResponse('No capital type found post capital type for user to see capital types')

    # Apply filtering if a search query is present (without breaking required header info)
    if query:
        from django.db.models import Q
        # Do not alter business_name/capital_name computed above
        capital_types = capital_types.filter(capital_type__icontains=query)
        tasks = base_tasks.filter(
            Q(task_name__icontains=query) |
            Q(task_type__icontains=query) |
            Q(capital_type__capital_type__icontains=query)
        )
        ratings = base_ratings.filter(task__in=tasks)
        times = times.filter(capital_type__capital_type__icontains=query)
    else:
        tasks = base_tasks
        ratings = base_ratings
    
    for task in tasks:
        task_dict[task.task_name] = ['-' for i in range(32)]
        try:
            task_rating = rating.objects.filter(task=task).first().rating
        except:
            return HttpResponse('No rating found go back and rate all tasks.')  
        if type(task_rating) == int:
            eval = task.task_max_hour * (rating_converter(task_rating)/10)
            if eval == 0:
                eval = '-'
            else:        
                if eval>0 and eval<=4:
                    task_dict['type'] = task.task_type
                    task_dict[task.task_name][task.task_precedence]= round(float(eval), 2)
                if eval>=5 and eval<=8:
                    task_dict['type'] = task.task_type
                    task_dict[task.task_name][task.task_precedence]= round(float(eval/2), 2)
                    task_dict[task.task_name][task.task_precedence+1]= round(float(eval/2), 2)
                if eval>=9 and eval<=12:
                    task_dict['type'] = task.task_type
                    task_dict[task.task_name][task.task_precedence]= round(float(eval/3), 2)
                    task_dict[task.task_name][task.task_precedence+1]= round(float(eval/3), 2)
                    task_dict[task.task_name][task.task_precedence+2]= round(float(eval/3), 2)
                if eval>=13 and eval<=16:
                    task_dict['type'] = task.task_type
                    task_dict[task.task_name][task.task_precedence]= round(float(eval/4), 2)
                    task_dict[task.task_name][task.task_precedence+1]= round(float(eval/4), 2)            
                    task_dict[task.task_name][task.task_precedence+2]= round(float(eval/4), 2)
                    task_dict[task.task_name][task.task_precedence+3]= round(float(eval/4), 2)
                if eval>=17 and eval<=20:   
                    task_dict['type'] = task.task_type
                    task_dict[task.task_name][task.task_precedence]= round(float(eval/5), 2)
                    task_dict[task.task_name][task.task_precedence+1]= round(float(eval/5), 2)            
                    task_dict[task.task_name][task.task_precedence+2]= round(float(eval/5), 2)
                    task_dict[task.task_name][task.task_precedence+3]= round(float(eval/5), 2)
                    task_dict[task.task_name][task.task_precedence+4]= round(float(eval/5), 2)
                if eval>=21 and eval<=24:   
                    task_dict['type'] = task.task_type
                    task_dict[task.task_name][task.task_precedence]= round(float(eval/6), 2)
                    task_dict[task.task_name][task.task_precedence+1]= round(float(eval/6), 2)            
                    task_dict[task.task_name][task.task_precedence+2]= round(float(eval/6), 2)
                    task_dict[task.task_name][task.task_precedence+3]= round(float(eval/6), 2)
                    task_dict[task.task_name][task.task_precedence+4]= round(float(eval/6), 2)
                    task_dict[task.task_name][task.task_precedence+5]= round(float(eval/6), 2)                     
                if eval>=25 and eval<=28:   
                    task_dict['type'] = task.task_type
                    task_dict[task.task_name][task.task_precedence]= round(float(eval/7), 2)
                    task_dict[task.task_name][task.task_precedence+1]= round(float(eval/7), 2)            
                    task_dict[task.task_name][task.task_precedence+2]= round(float(eval/7), 2)
                    task_dict[task.task_name][task.task_precedence+3]= round(float(eval/7), 2)
                    task_dict[task.task_name][task.task_precedence+4]= round(float(eval/7), 2)
                    task_dict[task.task_name][task.task_precedence+5]= round(float(eval/7), 2)
                    task_dict[task.task_name][task.task_precedence+6]= round(float(eval/7), 2)

                if eval>=29 and eval<=32:   
                    task_dict['type'] = task.task_type
                    task_dict[task.task_name][task.task_precedence]= round(float(eval/8), 2)
                    task_dict[task.task_name][task.task_precedence+1]= round(float(eval/8), 2)            
                    task_dict[task.task_name][task.task_precedence+2]= round(float(eval/8), 2)
                    task_dict[task.task_name][task.task_precedence+3]= round(float(eval/8), 2)
                    task_dict[task.task_name][task.task_precedence+4]= round(float(eval/8), 2)
                    task_dict[task.task_name][task.task_precedence+5]= round(float(eval/8), 2)
                    task_dict[task.task_name][task.task_precedence+6]= round(float(eval/8), 2)
                    task_dict[task.task_name][task.task_precedence+7]= round(float(eval/8), 2)                                          

    
    # Find the furthest index that has an integer before '-' starts
    max_week_index = 0
    for task_values in task_dict.values():
        if isinstance(task_values, list):  # Only process list values (task data)
            # Find the last index with a numeric value
            for i in range(len(task_values) - 1, -1, -1):  # Start from end, go backwards
                value = task_values[i]
                if value != '-' and value is not None and isinstance(value, (int, float)):
                    max_week_index = max(max_week_index, i)
                    break  # Found the last numeric value for this task, move to next task

    # Now, reduce dashes after the furthest integer
    for key, task_values in task_dict.items():
        if isinstance(task_values, list):
            task_dict[key] = task_values[:max_week_index + 1]            
    
    # Calculate totals for each week
    finfire_staff_totals = [0] * (max_week_index+1)
    intermediary_totals = [0] * (max_week_index+1)
    finfire_staff_grand_total = 0
    intermediary_grand_total = 0
    n = range(1,max_week_index+2)
    
    for task in tasks:
        task_values = task_dict.get(task.task_name, ['-'] * (max_week_index+1))
        for i, value in enumerate(task_values):
            if value != '-' and value is not None:
                try:
                    numeric_value = float(value)
                    if task.task_type == 'FINFIRE Staff Review & Scope of Work':
                        finfire_staff_totals[i] += numeric_value
                        finfire_staff_grand_total += numeric_value
                    elif task.task_type == 'Intermediary Services Scope of Work':
                        intermediary_totals[i] += numeric_value
                        intermediary_grand_total += numeric_value
                except (ValueError, TypeError):
                    continue
    
    # Calculate weekly budgets and cumulative totals
    weekly_budgets = []
    cumulative_budgets = []
    running_total = 0
    
    for i in range(max_week_index+1):
        finfire_cost = finfire_staff_totals[i] * 125  # $125/hour
        intermediary_cost = intermediary_totals[i] * 250  # $250/hour
        weekly_budget = finfire_cost + intermediary_cost
        weekly_budgets.append(round(weekly_budget, 2))
        running_total += weekly_budget
        cumulative_budgets.append(round(running_total, 2))
    
    context = {
        'selected_user': selected_user,
        'capital_types': capital_types,
        'tasks': tasks,
        'times': times,
        'ratings': ratings,
        'n': n,
        'business_name':business_name,
        'start_date':times.first().start_date if times else None,
        'end_date_sunday':times.first().start_date + timedelta(days=6) if times else None,
        'capital_name':capital_name,
        'raisegoal':raisegoal,
        'per_match':per_match,
        'task_dict':task_dict,
        'finfire_staff_totals': [round(float(number),2) for number in finfire_staff_totals],
        'intermediary_totals': [round(float(number),2) for number in intermediary_totals],
        'finfire_staff_grand_total': round(float(finfire_staff_grand_total), 2),
        'intermediary_grand_total': round(float(intermediary_grand_total), 2),
        'weekly_budgets': weekly_budgets,
        'cumulative_budgets': cumulative_budgets,
        'q': query,
    }
    return render(request, 'truth_in_capital/excel_template.html', context)


@login_required
def excel_template_download_view(request, user_id):
    """Download an Excel file mirroring the Excel-like HTML table for the given user."""
    UserModel = get_user_model()
    selected_user = get_object_or_404(UserModel, pk=user_id)

    # Security: only staff or the user themself
    if not request.user.is_staff and selected_user != request.user:
        return redirect('truth_in_capital:excel_template_for_user', user_id=request.user.id)

    # Reuse same data-building logic as the HTML view by inlining core parts
    try:
        capital_types = TruthCapitalType.objects.filter(user=selected_user)
        tasks = Task.objects.filter(capital_type__user=selected_user)
        times = time.objects.filter(capital_type__user=selected_user)
        ratings = rating.objects.filter(task__capital_type__user=selected_user)
        business_name = EQuestions2.objects.filter(user=selected_user).first().Business_Name
        capital_name = capital_types.first().capital_type if capital_types.exists() else ''
        raisegoal = EQuestions5.objects.filter(user=selected_user).first().Selected_Option
        per_match = 20
        task_dict = {}
    except Exception:
        return HttpResponse('Required data missing to generate the Excel.')

    for t in tasks:
        task_dict[t.task_name] = ['-' for _ in range(32)]
        try:
            task_rating_value = rating.objects.filter(task=t).first().rating
        except Exception:
            return HttpResponse('No rating found. Please rate all tasks.')
        if isinstance(task_rating_value, int):
            eval_hours = t.task_max_hour * (rating_converter(task_rating_value) / 10)
            if eval_hours == 0:
                eval_segmented = '-'
            else:
                if eval_hours > 0 and eval_hours <= 4:
                    task_dict['type'] = t.task_type
                    task_dict[t.task_name][t.task_precedence] = round(float(eval_hours), 2)
                if eval_hours >= 5 and eval_hours <= 8:
                    task_dict['type'] = t.task_type
                    task_dict[t.task_name][t.task_precedence] = round(float(eval_hours / 2), 2)
                    task_dict[t.task_name][t.task_precedence + 1] = round(float(eval_hours / 2), 2)
                if eval_hours >= 9 and eval_hours <= 12:
                    task_dict['type'] = t.task_type
                    task_dict[t.task_name][t.task_precedence] = round(float(eval_hours / 3), 2)
                    task_dict[t.task_name][t.task_precedence + 1] = round(float(eval_hours / 3), 2)
                    task_dict[t.task_name][t.task_precedence + 2] = round(float(eval_hours / 3), 2)
                if eval_hours >= 13 and eval_hours <= 16:
                    task_dict['type'] = t.task_type
                    task_dict[t.task_name][t.task_precedence] = round(float(eval_hours / 4), 2)
                    task_dict[t.task_name][t.task_precedence + 1] = round(float(eval_hours / 4), 2)
                    task_dict[t.task_name][t.task_precedence + 2] = round(float(eval_hours / 4), 2)
                    task_dict[t.task_name][t.task_precedence + 3] = round(float(eval_hours / 4), 2)
                if eval_hours >= 17 and eval_hours <= 20:
                    task_dict['type'] = t.task_type
                    task_dict[t.task_name][t.task_precedence] = round(float(eval_hours / 5), 2)
                    task_dict[t.task_name][t.task_precedence + 1] = round(float(eval_hours / 5), 2)
                    task_dict[t.task_name][t.task_precedence + 2] = round(float(eval_hours / 5), 2)
                    task_dict[t.task_name][t.task_precedence + 3] = round(float(eval_hours / 5), 2)
                    task_dict[t.task_name][t.task_precedence + 4] = round(float(eval_hours / 5), 2)
                if eval_hours >= 21 and eval_hours <= 24:
                    task_dict['type'] = t.task_type
                    task_dict[t.task_name][t.task_precedence] = round(float(eval_hours / 6), 2)
                    task_dict[t.task_name][t.task_precedence + 1] = round(float(eval_hours / 6), 2)
                    task_dict[t.task_name][t.task_precedence + 2] = round(float(eval_hours / 6), 2)
                    task_dict[t.task_name][t.task_precedence + 3] = round(float(eval_hours / 6), 2)
                    task_dict[t.task_name][t.task_precedence + 4] = round(float(eval_hours / 6), 2)
                    task_dict[t.task_name][t.task_precedence + 5] = round(float(eval_hours / 6), 2)
                if eval_hours >= 25 and eval_hours <= 28:
                    task_dict['type'] = t.task_type
                    task_dict[t.task_name][t.task_precedence] = round(float(eval_hours / 7), 2)
                    task_dict[t.task_name][t.task_precedence + 1] = round(float(eval_hours / 7), 2)
                    task_dict[t.task_name][t.task_precedence + 2] = round(float(eval_hours / 7), 2)
                    task_dict[t.task_name][t.task_precedence + 3] = round(float(eval_hours / 7), 2)
                    task_dict[t.task_name][t.task_precedence + 4] = round(float(eval_hours / 7), 2)
                    task_dict[t.task_name][t.task_precedence + 5] = round(float(eval_hours / 7), 2)
                    task_dict[t.task_name][t.task_precedence + 6] = round(float(eval_hours / 7), 2)
                if eval_hours >= 29 and eval_hours <= 32:
                    task_dict['type'] = t.task_type
                    task_dict[t.task_name][t.task_precedence] = round(float(eval_hours / 8), 2)
                    task_dict[t.task_name][t.task_precedence + 1] = round(float(eval_hours / 8), 2)
                    task_dict[t.task_name][t.task_precedence + 2] = round(float(eval_hours / 8), 2)
                    task_dict[t.task_name][t.task_precedence + 3] = round(float(eval_hours / 8), 2)
                    task_dict[t.task_name][t.task_precedence + 4] = round(float(eval_hours / 8), 2)
                    task_dict[t.task_name][t.task_precedence + 5] = round(float(eval_hours / 8), 2)
                    task_dict[t.task_name][t.task_precedence + 6] = round(float(eval_hours / 8), 2)
                    task_dict[t.task_name][t.task_precedence + 7] = round(float(eval_hours / 8), 2)

    # Determine max week index
    max_week_index = 0
    for values in task_dict.values():
        if isinstance(values, list):
            for i in range(len(values) - 1, -1, -1):
                v = values[i]
                if v != '-' and v is not None and isinstance(v, (int, float)):
                    max_week_index = max(max_week_index, i)
                    break

    for key, values in task_dict.items():
        if isinstance(values, list):
            task_dict[key] = values[: max_week_index + 1]

    finfire_staff_totals = [0] * (max_week_index + 1)
    intermediary_totals = [0] * (max_week_index + 1)
    finfire_staff_grand_total = 0
    intermediary_grand_total = 0

    for t in tasks:
        vals = task_dict.get(t.task_name, ['-'] * (max_week_index + 1))
        for i, v in enumerate(vals):
            if v != '-' and v is not None:
                try:
                    nv = float(v)
                    if t.task_type == 'FINFIRE Staff Review & Scope of Work':
                        finfire_staff_totals[i] += nv
                        finfire_staff_grand_total += nv
                    elif t.task_type == 'Intermediary Services Scope of Work':
                        intermediary_totals[i] += nv
                        intermediary_grand_total += nv
                except (ValueError, TypeError):
                    continue

    weekly_budgets = []
    cumulative_budgets = []
    running = 0
    for i in range(max_week_index + 1):
        finfire_cost = finfire_staff_totals[i] * 125
        intermediary_cost = intermediary_totals[i] * 250
        weekly = finfire_cost + intermediary_cost
        weekly_budgets.append(round(weekly, 2))
        running += weekly
        cumulative_budgets.append(round(running, 2))

    # Build workbook
    wb = Workbook()
    ws = wb.active
    ws.title = 'Truth in Capital'

    # Header row: Project and weeks
    header = [f"{business_name} - {capital_name}"]
    for idx in range(1, max_week_index + 2):
        header.append(f"Week {idx}")
    header.append('Total')
    ws.append(header)
    last_col = len(header)

    # Week start and end rows
    from datetime import datetime
    if times.exists():
        start_date = times.first().start_date
        end_date_sunday = start_date + timedelta(days=6)
    else:
        start_date = None
        end_date_sunday = None

    def fmt(dt):
        return dt.strftime('%b %d, %Y') if dt else ''

    # Build week dates increasing by 7 days for each Week column
    week_count = max_week_index + 1
    start_cells = []
    end_cells = []
    if start_date:
        start_cells = [fmt(start_date + timedelta(days=7 * (i + 1))) for i in range(week_count)]
    else:
        start_cells = ['' for _ in range(week_count)]
    if end_date_sunday:
        end_cells = [fmt(end_date_sunday + timedelta(days=7 * (i + 1))) for i in range(week_count)]
    else:
        end_cells = ['' for _ in range(week_count)]

    # Include an empty cell for the 'Total' column at the end
    ws.append(['Week Starting Date', fmt(start_date)] + start_cells + [''])
    ws.append(['Week Ending Date', fmt(end_date_sunday)] + end_cells + [''])

    # No charge rows
    ws.append(['Enterprise Registration'] + ['No Charge'] * (max_week_index + 1))
    ws.append(['Finfire Letter - Capital Market'] + ['No Charge'] * (max_week_index + 1))
    ws.append(['Truth in capital type, cost, timeline form'] + ['No Charge'] * (max_week_index + 1))

    # Goal banner (as a row)
    ws.append([f"Goal is to raise {raisegoal} for {business_name} THROUGH {capital_name}"])

    # Sections: FINFIRE Staff
    ws.append(['FINFIRE Staff Review & Scope of Work'])
    for t in tasks:
        if t.task_type == 'FINFIRE Staff Review & Scope of Work':
            values = task_dict.get(t.task_name, [])
            row = [t.task_name] + values + [sum([v for v in values if isinstance(v, (int, float))])]
            ws.append(row)
    ws.append(['Total FINFIRE Staff Hours'] + [round(float(i), 2) for i in finfire_staff_totals] + [round(float(finfire_staff_grand_total), 2)])

    # Sections: Intermediary
    ws.append(['Intermediary Services Scope of Work'])
    for t in tasks:
        if t.task_type == 'Intermediary Services Scope of Work':
            values = task_dict.get(t.task_name, [])
            row = [t.task_name] + values + [sum([v for v in values if isinstance(v, (int, float))])]
            ws.append(row)
    ws.append(['Total Intermediary Services Hours'] + [round(float(i), 2) for i in intermediary_totals] + [round(float(intermediary_grand_total), 2)])

    # Summary of Fee Schedule
    ws.append(['Summary of Fee Schedule'])
    ws.append(['Per contact match fee'] + [20] * (max_week_index + 1) + [20])
    ws.append(['Monthly SaaS Fee'] + ['-'] * (max_week_index + 1) + ['-'])
    ws.append(['Average Finfire Staff Rate'] + [125] * (max_week_index + 1) + [125])
    ws.append(['Average Intermediary Rate'] + [250] * (max_week_index + 1) + [250])

    # Budgets
    ws.append(['Net Budget by Week'] + weekly_budgets + [round(finfire_staff_grand_total * 125 + intermediary_grand_total * 250, 2)])
    ws.append(['Cumulative Budget'] + cumulative_budgets + [round(finfire_staff_grand_total * 125 + intermediary_grand_total * 250, 2)])
    ws.append(['Invoice Due'] + weekly_budgets + [round(finfire_staff_grand_total * 125 + intermediary_grand_total * 250, 2)])

    # ===== Styling to approximate HTML CSS =====
    # Row indices based on the append order above
    row_header = 1
    row_week_start = 2
    row_week_end = 3
    row_nc1 = 4
    row_nc2 = 5
    row_nc3 = 6
    row_goal = 7
    finfire_tasks = [t for t in tasks if t.task_type == 'FINFIRE Staff Review & Scope of Work']
    inter_tasks = [t for t in tasks if t.task_type == 'Intermediary Services Scope of Work']
    row_finfire_header = 8
    row_finfire_total = row_finfire_header + 1 + len(finfire_tasks)
    row_intermediary_header = row_finfire_total + 1
    row_intermediary_total = row_intermediary_header + 1 + len(inter_tasks)
    row_summary_header = row_intermediary_total + 1
    row_fee_1 = row_summary_header + 1
    row_fee_2 = row_summary_header + 2
    row_fee_3 = row_summary_header + 3
    row_fee_4 = row_summary_header + 4
    row_budget_weekly = row_summary_header + 5
    row_budget_cum = row_summary_header + 6
    row_budget_invoice = row_summary_header + 7

    # Styles
    thin_side = Side(style='thin', color='DDDDDD')
    border_all = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)

    def fill_row(r, fg_hex):
        for c in range(1, last_col + 1):
            ws.cell(row=r, column=c).fill = PatternFill('solid', fgColor=fg_hex)

    def bold_row(r):
        for c in range(1, last_col + 1):
            ws.cell(row=r, column=c).font = Font(bold=True)

    def align_row(r, first_left=True):
        for c in range(1, last_col + 1):
            horiz = 'left' if (first_left and c == 1) else 'center'
            ws.cell(row=r, column=c).alignment = Alignment(horizontal=horiz, vertical='center', wrap_text=True)

    def border_table(r1, r2):
        for r in range(r1, r2 + 1):
            for c in range(1, last_col + 1):
                ws.cell(row=r, column=c).border = border_all

    # Column widths
    ws.column_dimensions[get_column_letter(1)].width = 45
    for c in range(2, last_col + 1):
        ws.column_dimensions[get_column_letter(c)].width = 14

    # Header styling
    fill_row(row_header, 'E3F2FD')  # light blue
    bold_row(row_header)
    align_row(row_header)

    # Info rows
    fill_row(row_week_start, 'D1ECF1')
    fill_row(row_week_end, 'D1ECF1')
    bold_row(row_week_start)
    bold_row(row_week_end)
    align_row(row_week_start)
    align_row(row_week_end)

    # No charge rows (light gray)
    for r in [row_nc1, row_nc2, row_nc3]:
        fill_row(r, 'F8F9FA')
        align_row(r)

    # Goal banner (warning gradient approximated)
    fill_row(row_goal, 'FFE082')
    bold_row(row_goal)
    align_row(row_goal)

    # Section headers (secondary)
    for r in [row_finfire_header, row_intermediary_header, row_summary_header]:
        fill_row(r, 'E9ECEF')
        bold_row(r)
        align_row(r)

    # Align other rows
    for r in range(row_finfire_header + 1, ws.max_row + 1):
        align_row(r)

    # Bold totals and budgets
    for r in [row_finfire_total, row_intermediary_total, row_budget_weekly, row_budget_cum, row_budget_invoice]:
        bold_row(r)

    # Number formats
    # Hours 2 decimals on task rows and totals
    def set_two_decimals(r_from, r_to):
        if r_to >= r_from:
            for r in range(r_from, r_to + 1):
                for c in range(2, last_col + 1):
                    ws.cell(row=r, column=c).number_format = '0.00'

    set_two_decimals(row_finfire_header + 1, row_finfire_total)
    set_two_decimals(row_intermediary_header + 1, row_intermediary_total)

    # Currency for budgets
    for r in [row_budget_weekly, row_budget_cum, row_budget_invoice]:
        for c in range(2, last_col + 1):
            ws.cell(row=r, column=c).number_format = '$#,##0.00'

    # Borders for the whole table
    border_table(1, ws.max_row)

    # Freeze panes (sticky header + first column)
    ws.freeze_panes = 'B2'

    # Response
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    filename = f"truth_in_capital_{selected_user.username}.xlsx"
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    wb.save(response)
    return response

@login_required
def task_rating_form_view(request, user_id=None):
    """
    View to handle the rating form submission from entreprise_questions.forms.ratingForm
    Maps form fields to tasks and saves ratings to the rating model
    """
    User = get_user_model()
    query = request.GET.get('q', '').strip()
    
    # If no user_id provided, show user selection page for staff
    if not user_id:
        if request.user.is_staff:
            # Staff users can see all users who have capital types
            users = User.objects.filter(truthcapitaltype__isnull=False).distinct()
            if query:
                from django.db.models import Q
                users = users.filter(
                    Q(username__icontains=query) |
                    Q(first_name__icontains=query) |
                    Q(last_name__icontains=query)
                )
            context = {
                'users': users,
                'q': query,
            }
            return render(request, 'truth_in_capital/user_selection_rating.html', context)
        else:
            # Non-staff users can only see their own data
            return redirect('truth_in_capital:task_rating_form_for_user', user_id=request.user.id)
    
    # Get the selected user
    selected_user = get_object_or_404(User, pk=user_id)
    
    # Security check: Non-staff users can only access their own data
    if not request.user.is_staff and selected_user != request.user:
        return redirect('truth_in_capital:task_rating_form_for_user', user_id=request.user.id)
    
    # Get user's capital types and tasks
    try:
        capital_types = TruthCapitalType.objects.filter(user=selected_user)
        base_tasks = Task.objects.filter(capital_type__user=selected_user)
        
        if not base_tasks.exists():
            return HttpResponse('No tasks found for this user. Please create tasks first.')
            
    except Exception as e:
        return HttpResponse(f'Error retrieving user data: {str(e)}')

    # Apply filtering for display (GET) while preserving full task set for POST processing
    if query:
        from django.db.models import Q
        tasks = base_tasks.filter(
            Q(task_name__icontains=query) |
            Q(task_type__icontains=query) |
            Q(capital_type__capital_type__icontains=query)
        )
    else:
        tasks = base_tasks
    
    # Mapping of form field names to task names
    field_to_task_mapping = {
        'financial_model_forecast_pro_forma': 'Financial Model, forecast, pro forma',
        'finfire_report_capital_type': 'Finfire Report - Capital Type',
        'due_diligence_checklist_documents': 'Due Diligence Checklist Documents',
        'historical_financials': 'Historical Financials (P & L, BS, CF, Aging)',
        'tax_returns': 'Tax Returns (Up to 2 years, if applicable)',
        'business_valuation_equity_only': 'Business Valuation (Equity only)',
        'cap_table_use_of_funds_and_capitalization_plan': 'Cap Table, Use of Funds, & Capitalization Plan',
        'business_model_canvas': 'Business Model Canvas',
        'offering_documents_rating': 'Offering Documents',
        'presentation_video_ai_deep_dive': 'Presentation Video (From the AI Deep Dive)',
        'application_if_applicable': 'Application (If Applicable)',
        'resume_of_founder_ceo_primary_leader': 'Resume of Founder/CEO Primary Leader',
        'presentation_deck_rating': 'Presentation Deck',
        'executive_summary_including_exit_strategy': 'Executive Summary Including Exit Strategy',
        'quality_assurance_checklist_including_ai': 'Quality Assurance Checklist (Including AI)',
        'capital_match_list_generated': 'Capital Match List Generated',
        'investor_marketing_campaign': 'Investor Marketing Campaign',
        'investor_relations': 'Investor Relations',
        'progress_reports': 'Progress Reports',
    }
    
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            success_count = 0
            error_messages = []
            
            for field_name, task_name in field_to_task_mapping.items():
                try:
                    # Get the rating value from the form
                    rating_value = form.cleaned_data[field_name]
                    
                    # Find the corresponding task
                    # Always search across all tasks for updates, not just filtered display set
                    task = base_tasks.filter(task_name=task_name).first()
                    
                    if task:
                        # Check if rating already exists for this task
                        existing_rating = rating.objects.filter(task=task).first()
                        
                        if existing_rating:
                            # Update existing rating
                            existing_rating.rating = rating_value
                            existing_rating.save()
                        else:
                            # Create new rating
                            rating.objects.create(task=task, rating=rating_value)
                        
                        success_count += 1
                    else:
                        error_messages.append(f"Task '{task_name}' not found for user {selected_user.username}")
                        
                except Exception as e:
                    error_messages.append(f"Error processing {field_name}: {str(e)}")
            
            if success_count > 0:
                messages.success(request, f'Successfully saved {success_count} ratings for {selected_user.username}')
            
            if error_messages:
                for error in error_messages:
                    messages.warning(request, error)
            
            # Redirect back to the form or to a success page
            return redirect('truth_in_capital:excel_template_for_user', user_id=user_id)
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        # Pre-populate form with existing ratings
        initial_data = {}
        for field_name, task_name in field_to_task_mapping.items():
            task = tasks.filter(task_name=task_name).first()
            if task:
                existing_rating = rating.objects.filter(task=task).first()
                if existing_rating:
                    initial_data[field_name] = existing_rating.rating
        
        form = RatingForm(initial=initial_data)
    
    context = {
        'form': form,
        'selected_user': selected_user,
        'tasks': tasks,
        'capital_types': capital_types,
        'field_to_task_mapping': field_to_task_mapping,
        'q': query,
    }
    
    return render(request, 'truth_in_capital/task_rating_form.html', context)
