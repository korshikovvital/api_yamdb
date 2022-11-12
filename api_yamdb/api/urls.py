from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, UserViewSet, create_user,
                    self_patch_user, send_jwt)

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
    CommentViewSet,
    basename='comments')

urlpatterns = [
    path('v1/', include([
        path('auth/', include([
            path('signup/', create_user, name='create_user'),
            path('token/', send_jwt, name='send_jwt'),
        ])),
        path('users/me/', self_patch_user, name='self_patch_user'),
        path('', include(router_v1.urls)),
    ])),
]
