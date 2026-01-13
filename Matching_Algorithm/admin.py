from django.contrib import admin
from .models import Letter_Response,allCapitalMatchValues

# Register your models here.
#admin.site.register(Capital_Matches)
#admin.site.register(Letter_Response)
#admin.site.register(Matches_Purchased)
@admin.register(Letter_Response)
class letterResponseAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)

@admin.register(allCapitalMatchValues)
class allCapitalMatchValuesAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)