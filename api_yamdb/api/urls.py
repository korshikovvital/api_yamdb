from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (create_user, send_jwt, self_patch_user, CategoryViewSet,
                    GenreViewSet, TitleViewSet, UserViewSet,
                    ReviewViewSet, CommentsViewSet)

router_v1 = DefaultRouter()

router_v1.register('categories', CategoryViewSet)
router_v1.register('genres', GenreViewSet)
router_v1.register('titles', TitleViewSet)
router_v1.register('users', UserViewSet)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentsViewSet,
    basename='comments')

urlpatterns = [
    path('v1/auth/signup/', create_user, name='create_user'),
    path('v1/auth/token/', send_jwt, name='send_jwt'),
    path('v1/users/me/', self_patch_user, name='self_patch_user'),
    path('v1/', include(router_v1.urls)),
]
