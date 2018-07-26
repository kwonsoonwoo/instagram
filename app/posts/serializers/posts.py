from rest_framework import serializers

from ..models import Post

__all__ = (
    'PostBaseSerializer',
)


class PostBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'pk',
            'author',
            'photo',
            'content',
            'created_at',
            'tags',
            'like_users',
        )
