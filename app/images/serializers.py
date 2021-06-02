from rest_framework import serializers
from .models import Image


class ImageProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('file', 'profile')

    def create(self, validated_data):
        if Image.objects.filter(profile=validated_data['profile'][0]).exists():
            Image.objects.filter(profile=validated_data['profile'][0]).delete()
        image = Image.objects.create(file=validated_data['file'])
        image.profile.set(validated_data['profile'])
        image.save()
        return image
