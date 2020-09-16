from rest_framework import serializers

from .models import Post, Comment, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
                                            read_only=True,
                                            slug_field='username')

    class Meta:
        fields = ('__all__')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
                                            read_only=True,
                                            slug_field='username')

    class Meta:
        fields = ('__all__')
        model = Comment


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'id')
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault())

    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username')

    class Meta:
        fields = ('__all__')
        model = Follow
