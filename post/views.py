from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import Post
from post.serializers import PostSerializer


class MyPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_count"

    def get_page_size(self, request):
        page_count_value = request.query_params.get(self.page_size_query_param)
        if page_count_value and page_count_value.isdigit():
            return int(page_count_value)
        else:
            return self.page_size


class PostListAPIView(APIView):
    def get(self, request):
        qs = Post.objects.all()

        hashtag = request.query_params.get("hashtag")
        if hashtag:
            qs = qs.filter(hashtags__name=hashtag)

        paginator = MyPageNumberPagination()
        paginated_qs = paginator.paginate_queryset(qs, request)

        if paginated_qs is not None:
            serializer = PostSerializer(paginated_qs, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
