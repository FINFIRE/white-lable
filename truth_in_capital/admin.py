from django.contrib import admin
from .models import TruthCapitalType, Task, time,rating

@admin.register(TruthCapitalType)
class TruthCapitalTypeAdmin(admin.ModelAdmin):
    list_display = ('user', 'capital_type')
    search_fields = ('capital_type', 'user__username')
    list_filter = ('capital_type',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('user', 'task_name', 'capital_type', 'task_max_hour', 'task_precedence')
    search_fields = ('capital_type__user__username','task_name', 'capital_type__capital_type')
    list_filter = ('capital_type',)
    ordering = ('capital_type', 'task_precedence')

@admin.register(time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('id', 'capital_type')
    search_fields = ('capital_type__user__username',)
    #list_filter = ('capital_type','duration_capital_weeks')

@admin.register(rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id','task','rating')
    search_fields = ('task__capital_type__user__username','task__capital_type__capital_type',)
    #list_filter = ('task', 'capital_type')