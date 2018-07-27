from rest_framework import generics

from members.models import User
from members.serializers import UserBaseSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserBaseSerializer