from rest_framework import serializers
from .models import Image
from django.contrib.auth import get_user_model
from posts.models import Post
from django.db.models import OuterRef
from support.models import MessageToSupport

class ImageProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('file', 'profile')
    def create(self, validated_data):
        Image.objects.filter(profile=validated_data['profile'][0]).delete()
        image = Image.objects.create(file = validated_data['file'])
        image.profile.set(validated_data['profile'])
        image.save()
        return image