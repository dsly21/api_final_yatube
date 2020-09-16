from rest_framework import viewsets, filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

from .permissions import CheckAuthorPermission
from .models import Post, Group, Follow
from .serializers import (
                            PostSerializer,
                            CommentSerializer,
                            GroupSerializer,
                            FollowSerializer,)


User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [CheckAuthorPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group', ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, CheckAuthorPermission]

    def perform_create(self, serializer):
        get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments


class GroupListCreate(viewsets.ViewSetMixin, generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [CheckAuthorPermission]


class FollowListCreate(viewsets.ViewSetMixin, generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=user__username', '=following__username']
    permission_classes = [CheckAuthorPermission]
