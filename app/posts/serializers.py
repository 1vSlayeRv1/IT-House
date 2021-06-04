from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Post, Comment
from images.models import Image
from profiles.models import Profile


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('comment', 'post')

    def validate(self, attrs):
        if attrs['comment'] == '':
            raise ValidationError('Invalid Comment')
        return attrs

    def create(self, validated_data):
        comment = Comment.objects.create(
            comment=validated_data['comment'],
            profile=self.context['profile'],
            post=validated_data['post']
        )
        comment.save()
        return comment

    def update(self, instance, validate_data):
        if not instance:
            raise ValidationError('Comment not found!')
        instance.comment = validate_data['comment']
        instance.save()
        return instance


class ImageFileSerializer(serializers.ModelSerializer):
    file = serializers.StringRelatedField(source='file.url', read_only=True)

    class Meta:
        model = Image
        fields = ('file', )


class ProfileImageSerializer(serializers.ModelSerializer):
    profile_image = ImageFileSerializer(read_only=True, many=True)

    class Meta:
        model = Profile
        fields = ('id', 'profile_image')


class CommentImageSerializer(serializers.ModelSerializer):
    profile = ProfileImageSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'comment', 'date', 'profile', 'post')


class PostWithCommentsSerializer(serializers.ModelSerializer):

    comments = CommentImageSerializer(many=True, read_only=True)
    post_image = ImageFileSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'content',
                  'post_image', 'date', 'comments')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
