from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    """Администратор или кто-то с более серьезными правами."""
    def has_permission(self, request, view):
        # не нравится, переделать
        if request.user.is_superuser:
            return True
        # если аноним пробился, false
        elif request.user.is_anonymous:
            return False
        # если админ или модер
        return request.user.role == 'admin'


class IsModer(permissions.BasePermission):
    """Модератор или кто-то с более серьезными правами."""
    def has_permission(self, request, view):
        # не нравится, переделать

        # если суперюзер, сразу true
        if request.user.is_superuser:
            return True
        # если аноним пробился, false
        elif request.user.is_anonymous:
            return False
        # если админ или модер
        return request.user.role == 'admin' or request.user.role == 'moderator'


class OwnerOrReadOnly(permissions.BasePermission):
    """Автор или кто-то с более серьезными правами."""
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
