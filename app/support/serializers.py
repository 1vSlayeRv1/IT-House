from re import L, VERBOSE
from django.db.models import fields
from rest_framework import serializers
from .models import MessageToSupport
from images.models import Image
from profiles.models import Profile


class SupportImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('file', 'support')
    def create(self, validated_data):
        image = Image.objects.create(file=validated_data['file'])
        image.support.add(validated_data['support'][0])
        image.save()
        return image
class SupportMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageToSupport
        fields = ('id', 'title', 'content', 'profile', 'section')

    def create(self, validated_data):
        message = MessageToSupport.objects.create(
            title=validated_data['title'],
            content=validated_data['content'],
            profile=validated_data['profile'],
            section=validated_data['section'],
        )
        message.save()
        return message
