from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework import generics, permissions
from .permissions import IsAuthorOrReadOnly


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
