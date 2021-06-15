from images.models import Image
from profiles.models import Profile
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, StringRelatedField

from .models import Comment, Post


class CommentSerializer(ModelSerializer):

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


class PostImageSerializer(ModelSerializer):
    file = StringRelatedField(source='file.url', read_only=True)

    class Meta:
        model = Image
        fields = ('file', )
        read_only_fields = fields


class ProfileImageSerializer(ModelSerializer):
    avatar = StringRelatedField(
        source='avatar.url', read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'avatar')
        read_only_fields = fields


class CommentImageSerializer(ModelSerializer):
    profile = ProfileImageSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'comment', 'date', 'profile', 'post')
        read_only_fields = fields


class PostWithCommentsSerializer(ModelSerializer):
    comments = CommentImageSerializer(many=True, read_only=True)
    post_image = PostImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'content',
                  'post_image', 'date', 'comments')
        read_only_fields = fields


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
