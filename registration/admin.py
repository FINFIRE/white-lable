from django.contrib import admin
from .models import UserDetail,UserDetail2

# Register your models here.
#admin.site.register(UserDetail)
#admin.site.register(UserDetail2)

@admin.register(UserDetail)
class UserDetailOneAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)

@admin.register(UserDetail2)
class UserDetailTwoAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)