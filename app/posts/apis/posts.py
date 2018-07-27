# /api/posts/
# 1. posts.serializers -> PostSerializer
# 2. apis.__init__
#   class PostList(APIView):
#       def get(self, request):
#           <logic>

# 3. config.urls에서 (posts.urls는 무시)
#   /api/posts/ 가 위의 PostList.as_view()와 연결되도록 처리
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.serializers import PostBaseSerializer
from ..models import Post


# ListCreateAPIView를 사용해서 Post Create를 Postman으로 실행해보기
# 관련 테스트 짜오기 (List 및 Create)
class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostBaseSerializer
