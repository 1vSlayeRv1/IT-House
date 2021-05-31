from django.db.models import query
from django.db.models.query import QuerySet
from rest_framework import serializers
from rest_framework.generics import ListAPIView
from .models import Post, Comment
from django.contrib.auth import get_user_model
from .serializers import CommentSerializer, PostSerializer, PostWithCommentsSerializer
User = get_user_model()

class ListPosts(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ListDetailPosts(ListAPIView):
    serializer_class = PostWithCommentsSerializer
    model = serializer_class.Meta.model
    def get_queryset(self):
        post_id = self.kwargs['pk']
        queryset = self.model.objects.filter(id=post_id)
        return queryset
