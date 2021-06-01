from datetime import datetime
from django.contrib.auth import get_user_model
from django.core.exceptions import ViewDoesNotExist
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CurrentUserDefault
from .models import Post, Comment
from images.models import Image
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
    def validate(self, attrs):
        if attrs['comment'] == '':
            raise ValidationError('Invalid Comment')
        return attrs
    def create(self, validated_data):
        comment = Comment.objects.create(
            comment = validated_data['comment'],
            profile = validated_data['profile'],
            post = validated_data['post']
        )
        comment.save()
        return comment
    def update(self, instance, validate_data):
        if not instance:
            raise ValidationError('Comment not found!')
        instance.comment = validate_data['comment']
        instance.save()
        return instance

class CommentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'date', 'profile', 'post')

 
class PostWithCommentsSerializer(serializers.ModelSerializer):

    comments = CommentImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'content', 'date', 'comments')

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'