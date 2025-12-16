from rest_framework import permissions


class IsStaffPermission(permissions.BasePermission):
    """
    Custom permission to only allow admin users to access certain views.
    """
    
    def has_permission(self, request, view):
        user = request.user

        if user and user.is_staff_member:
            return True
        return False


class IsStaffOrOwnerPermission(permissions.BasePermission):
    """
    Custom permission to only allow staff members or the owner of the object to access it.
    """
    
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user and (user.is_staff_member or obj == user):
            return True
        
        return False
    
    


