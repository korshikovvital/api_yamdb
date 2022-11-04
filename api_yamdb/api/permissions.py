from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):
    """Автор или кто-то с более серьезными правами."""
    def has_permission(self, request, view):
        return (
                request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
            )
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class IsModer(permissions.BasePermission):
    """Модератор или кто-то с более серьезными правами."""
    def has_permission(self, request, view):
        # не нравится, переделать
        if request.user.is_anonymous:
            return False
        # true, если суперюзер или админ, или модер
        return request.user.is_superuser or request.user.role=='adm' or request.user.role=='mdr'


class IsAdmin(permissions.BasePermission):
    """Администратор или кто-то с более серьезными правами."""
    def has_permission(self, request, view):
        # не нравится, переделать
        if request.user.is_anonymous:
            return False
        return request.user.is_superuser or request.user.role=='adm'
