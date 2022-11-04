
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from .views import create_user, send_jwt, self_patch_user, UserViewSet
from rest_framework.routers import DefaultRouter

# Создаётся роутер
router = DefaultRouter()
# Вызываем метод .register с нужными параметрами
router.register('users', UserViewSet)
# В роутере можно зарегистрировать любое количество пар "URL, viewset":
# например
# router.register('owners', OwnerViewSet)
# Но нам это пока не нужно

urlpatterns = [
    path('auth/signup/', create_user, name='create_user'),
    path('auth/token/', send_jwt, name = 'send_jwt'),
    path('users/me/', self_patch_user, name = 'self_patch_user'),
    path('', include(router.urls)),
]
