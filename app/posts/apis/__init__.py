# /api/posts/
# 1. posts.serializers -> PostSerializer
# 2. apis.__init__
#   class PostList(APIView):
#       def get(self, request):
#           <logic>

# 3. config.urls에서 (posts.urls는 무시)
#   /api/posts/ 가 위의 PostList.as_view()와 연결되도록 처리
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.serializers import PostBaseSerializer
from ..models import Post


class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostBaseSerializer(posts, many=True)
        return Response(serializer.data)
