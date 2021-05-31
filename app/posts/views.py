from rest_framework import serializers
from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework import mixins, views, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Post, Comment

from django.contrib.auth import get_user_model
from .serializers import CommentSerializer, PostSerializer, PostWithCommentsSerializer
User = get_user_model()


class ListPosts(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ListDetailPosts(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = PostWithCommentsSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        post_id = self.kwargs['pk']
        queryset = self.model.objects.filter(id=post_id)
        return queryset


class CreateUpdateDestroyComments(mixins.CreateModelMixin,
                                  mixins.UpdateModelMixin,
                                  mixins.DestroyModelMixin,
                                  views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def put(self, request):
        comment = Comment.objects.filter(pk=request.data['id']).first()
        serializer = CommentSerializer(comment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request):
        comment = Comment.objects.get(pk=request.data['id'])
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
