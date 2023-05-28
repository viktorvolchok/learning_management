from rest_framework.permissions import BasePermission

SAFE_HTTP_METHODS = ["GET", "HEAD"]


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        if user and user.is_authenticated and user.is_staff:
            return True
        if request.method in SAFE_HTTP_METHODS:
            return True

        return False
