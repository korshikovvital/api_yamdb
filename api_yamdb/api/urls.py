from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ReviewViewSet, CommentsViewSet

router = SimpleRouter()
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentsViewSet,
    basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
]
