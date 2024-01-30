from rest_framework import permissions

class IsStaffUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow read-only access for everyone,
    and restrict POST and PUT access to staff users only.
    """
    def has_permission(self, request, view):
        # Allow read-only access for everyone
        if request.method in permissions.SAFE_METHODS:
            return True
        # Restrict POST and PUT access to staff users only
        return request.user and request.user.is_staff
