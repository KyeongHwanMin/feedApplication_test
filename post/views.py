from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import Post
from post.serializers import PostSerializer


class PostListAPIView(APIView):
    def get(self, request):
        qs = Post.objects.all()
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
