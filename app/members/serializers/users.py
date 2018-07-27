from rest_framework import serializers

from members.models import User


class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'img_profile',
            'site',
            'introduce',
            'gender',
            'to_relation_users',
        )
