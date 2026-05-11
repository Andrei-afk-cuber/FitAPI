from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    This permission provide access to object if user is resource owner
    """

    def has_permission(self, request, view):
        if request.user.is_staff or request.user.is_superuser:
            return True

        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.is_superuser:
            return True

        if obj.id == request.user.id:
            return True

        return False
