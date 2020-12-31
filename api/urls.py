from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )

from .views import PostsViewSet, CommentsViewSet, GroupViewSet, FollowViewSet


v1_router = DefaultRouter()
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentsViewSet,
                   basename='CommentsViewSet')
v1_router.register(r'posts', PostsViewSet, basename='PostsViewSet')
v1_router.register(r'group', GroupViewSet, basename='GroupViewSet')
v1_router.register(r'follow', FollowViewSet, basename='FollowViewSet')


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path(
        'token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'),
    path(
        'token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'),
]
