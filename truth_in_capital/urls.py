from django.urls import path
from . import views

app_name = 'truth_in_capital'

urlpatterns = [
    # Dashboard
    path('capital/', views.dashboard, name='dashboard'),
    
    # Capital Type URLs
    path('capital-types/', views.capital_type_list, name='capital_type_list'),
    path('capital-types/create/', views.capital_type_create, name='capital_type_create'),
    path('capital-types/<int:pk>/update/', views.capital_type_update, name='capital_type_update'),
    path('capital-types/<int:pk>/delete/', views.capital_type_delete, name='capital_type_delete'),
    
    # Task URLs
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('capital-types/<int:capital_type_pk>/tasks/', views.task_list, name='task_list_by_capital_type'),
    path('capital-types/<int:capital_type_pk>/tasks/create/', views.task_create, name='task_create_for_capital_type'),
    path('tasks/<int:pk>/update/', views.task_update, name='task_update'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    
    # Time URLs
    path('times/', views.time_list, name='time_list'),
    path('times/create/', views.time_create, name='time_create'),
    path('times/<int:pk>/update/', views.time_update, name='time_update'),
    path('times/<int:pk>/delete/', views.time_delete, name='time_delete'),
    
    # AJAX URLs
    path('tasks/reorder/', views.reorder_tasks, name='reorder_tasks'),
    # Rating URLs
    path('ratings/', views.rating_list, name='rating_list'),
    path('ratings/create/', views.rating_create, name='rating_create'),
    path('ratings/<int:pk>/update/', views.rating_update, name='rating_update'),
    path('ratings/<int:pk>/delete/', views.rating_delete, name='rating_delete'),
    # Excel-like template UI
    path('excel-template/', views.excel_template_view, name='excel_template'),
    path('excel-template/<int:user_id>/', views.excel_template_view, name='excel_template_for_user'),
    path('excel-template/<int:user_id>/download/', views.excel_template_download_view, name='excel_template_download_for_user'),
    # Task Rating Form URLs
    path('task-rating-form/', views.task_rating_form_view, name='task_rating_form'),
    path('task-rating-form/<int:user_id>/', views.task_rating_form_view, name='task_rating_form_for_user'),
] 