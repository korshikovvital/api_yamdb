from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """Администратор или суперпользователь."""

    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.is_admin


class ReviewsComments(permissions.BasePermission):
    """Права для отзывов и комментов. Необходим, так как не отрабатывает строка
    permission_classes = (OwnerOrReadOnly | IsAdmin | IsModer,), вероятно
    иp-за бага в используемой версии DRF."""

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user or request.user.is_moderator
            or request.user.is_admin
        )


class SafeMethods(permissions.BasePermission):
    """Безопасные методы."""

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS
