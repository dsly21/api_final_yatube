from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)

from .views import (
                    PostViewSet,
                    CommentViewSet,
                    FollowListCreate,
                    GroupListCreate,)


router = DefaultRouter()

router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comment')
router.register('posts', PostViewSet)
router.register('group', GroupListCreate)
router.register('follow', FollowListCreate)

urlpatterns = [
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(
        'v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/', include(router.urls)),
    ]
