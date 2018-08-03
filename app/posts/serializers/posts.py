from rest_framework import serializers

from members.serializers import UserBaseSerializer
from ..models import Post

__all__ = (
    'PostBaseSerializer',
)


class PostBaseSerializer(serializers.ModelSerializer):
    author = UserBaseSerializer(required=False)

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

    read_only_fields = (
        'author',
    )
