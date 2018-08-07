from rest_framework import serializers

from members.models import User


class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'img_profile',
            'first_name',
            'last_name',
        )
