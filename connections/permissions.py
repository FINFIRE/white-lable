from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group

class IsAdminPermission(BasePermission):
    """
    Custom permission to grant access to users who are either:
    - In the 'Admins' group, OR
    - Have is_staff=True (Django staff status)
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        # Staff users always have admin access
        if request.user.is_staff:
            return True
        # Check Admins group
        try:
            return Group.objects.get(name="Admins") in request.user.groups.all()
        except Group.DoesNotExist:
            return False
