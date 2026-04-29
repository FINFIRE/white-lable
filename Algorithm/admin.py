from django.contrib import admin
from .models import CapitalType,capitalTypes

# Register your models here.
@admin.register(capitalTypes)
class capitalTypesName(admin.ModelAdmin):
    ordering = ['name']
admin.site.register(CapitalType)