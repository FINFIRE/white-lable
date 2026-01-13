from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group

class IsAdminPermission(BasePermission):
    """
    Custom permission to grant access only to users in the 'Admins' group.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated and belongs to the 'Admins' group
        return request.user.is_authenticated and Group.objects.get(name="Admins") in request.user.groups.all()
