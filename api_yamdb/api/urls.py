
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import create_user, send_jwt, self_patch_user, UserViewSet


router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('auth/signup/', create_user, name='create_user'),
    path('auth/token/', send_jwt, name='send_jwt'),
    path('users/me/', self_patch_user, name='self_patch_user'),
    path('', include(router.urls)),
]
