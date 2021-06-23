from django.contrib.auth import get_user_model
from rest_framework import mixins, status, views
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Comment, Post
from .serializers import (CommentSerializer, PostSerializer,
                          PostWithCommentsSerializer)

User = get_user_model()


class ListPosts(ListAPIView):
    permission_classes = (AllowAny, )
    throttle_scope = 'posts'
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ListDetailPosts(ListAPIView):
    permission_classes = (AllowAny, )
    throttle_scope = 'posts'
    serializer_class = PostWithCommentsSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        post_id = self.kwargs['pk']
        queryset = self.model.objects.filter(id=post_id)
        return queryset

    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        if self.request.GET.get('offset'):
            offset = int(self.request.GET.get('offset'))
        else:
            offset = 0
        comments = 5
        if queryset:
            serializer = PostWithCommentsSerializer(
                queryset,
                many=True,
                context={'offset': offset,
                         'comments': comments})
            return Response(serializer.data[0])
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CreateUpdateDestroyComments(mixins.CreateModelMixin,
                                  mixins.UpdateModelMixin,
                                  mixins.DestroyModelMixin,
                                  views.APIView):
    permission_classes = (IsAuthenticated,)
    throttle_scope = 'comments'

    def post(self, request):
        serializer = CommentSerializer(data=request.data, context={
                                       'profile': request.user})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        comment = Comment.objects.filter(
            pk=request.data['id']).filter(
            profile=request.user.pk).first()
        if comment:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        comment = Comment.objects.filter(
            pk=request.data['id']).filter(
            profile=request.user.pk)
        if comment.exists():
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
