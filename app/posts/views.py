from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.db.models import Prefetch
from django.db.models import query
from django.db.models.query import QuerySet
from rest_framework.generics import ListAPIView
from rest_framework import mixins, views, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from images.models import Image
from .models import Post, Comment
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

    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostWithCommentsSerializer(queryset, many=True)
        return Response(serializer.data[0])


class CreateUpdateDestroyComments(mixins.CreateModelMixin,
                                  mixins.UpdateModelMixin,
                                  mixins.DestroyModelMixin,
                                  views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = CommentSerializer(data=request.data, context={
                                       'profile': request.user})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        comment = Comment.objects.filter(
            pk=request.data['id']).filter(
            profile=request.user.pk).first()
        if comment:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                raise ValidationError('Comment Error')
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        comment = Comment.objects.filter(
            pk=request.data['id']).filter(
            profile=request.user.pk)
        if comment.exists():
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
