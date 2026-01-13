from django.contrib import admin
from .models import pay_load_string,Match_Data

# Register your models here.
#admin.site.register(pay_load_string)
#admin.site.register(Match_Data)

@admin.register(pay_load_string)
class payLoadStringAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)

@admin.register(Match_Data)
class MatchDataAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)