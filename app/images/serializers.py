from rest_framework.serializers import ModelSerializer

from .models import Image


class ImageProfileSerializer(ModelSerializer):

    class Meta:
        model = Image
        fields = ('file', )

    def create(self, validated_data):
        if Image.objects.filter(profile=self.context['profile']).exists():
            Image.objects.filter(profile=self.context['profile']).delete()
        image = Image.objects.create(file=validated_data['file'])
        image.profile.set([self.context['profile']])
        image.save()
        return image
