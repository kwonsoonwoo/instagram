from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.compat import authenticate
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from members.models import User
from members.serializers import UserBaseSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserBaseSerializer


# class AuthToken1(ObtainAuthToken):
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#         })


class AuthToken(APIView):
    def post(self, request):
        # 전달받은 데이터에서 username, password추출
        username = request.data.get('username')
        password = request.data.get('password')

        # authenticate 실행
        user = authenticate(username=username, password=password)

        # authenticate가 성공한 경우
        if user:
            # Token을 가져오거나 없으면 생성
            token, __ = Token.objects.get_or_create(user=user)
            # Response에 돌려줄 데이터
            data = {
                'token': token.key,
            }
            return Response(data)
        # authenticate에 실패한 경우
        raise AuthenticationFailed('인증정보가 올바르지 않습니다.')


class AuthenticationTest(APIView):
    # URL: /api/users/auth-test/
    def get(self, request):
        # request.user가 인증 된 상태일 경우, UserSerializer를 사용해 렌더링한 데이터를 보내줌
        # 인증되지 않았을 경우 NotAuthenticated Exception을 raise
        if request.user.is_authenticated:
            return Response(UserBaseSerializer(request.user).data)
        raise NotAuthenticated('로그인 되어있지 않습니다')


class FacebookAuthToken(APIView):
    def post(self, request):
        #   URL: /api/users/facebook-login/
        # request.data에 'facebook_id'와 'first_name', 'last_name'이 올 것으로 예상
        # 1. 전달받은 facebook_id에 해당하는 유저가 존재하면 해당 User에
        # 2. 존재하지 않는다면 'first_name'과 'last_name'값을 추가로 사용해 생성한 User에
        #   -> 해당하는 Token을 가져오거나 새로 생성해서 리턴
        # 결과는 Postman으로 확인
        facebook_id = request.data.get('facebook_id')
        last_name = request.data.get('last_name')
        first_name = request.data.get('first_name')
        user, __ = User.objects.get_or_create(
            username=facebook_id,
            defaults={
                'last_name': last_name,
                'first_name': first_name,
            }
        )
        # facebook_id에 해당하는 User가 있는지 검사, 있으면 해당 User를 사용
        # if User.objects.filter(username=facebook_id).exists():
        #     user = User.objects.get(username=facebook_id)
        # 없으면 생성
        # else:
        #     user = User.objects.create_user(
        #         username=facebook_id,
        #         last_name=last_name,
        #         first_name=first_name,
        #     )
        # 해당 User와 연결되는 Token생성
        token, __ = Token.objects.get_or_create(user=user)
        data = {
            'token': token.key,
            'user': UserBaseSerializer(user).data,
        }
        return Response(data)
        print(request.data)
        return Response()

