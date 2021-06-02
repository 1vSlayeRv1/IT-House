from profiles.models import Profile
from django.contrib.auth import get_user_model
from rest_framework.relations import SlugRelatedField
from rest_framework.exceptions import ValidationError
from events.models import Event
from rest_framework import serializers
from images.models import Image


class ImageEventSerializer(serializers.ModelSerializer):
    file = serializers.StringRelatedField(source='file.url', read_only=True)

    class Meta:
        model = Image
        fields = ('file', )


class EventSerializer(serializers.ModelSerializer):
    file = ImageEventSerializer(read_only=True)

    class Meta:
        model = Event
        fields = ('id', 'name', 'description',
                  'date_start', 'date_end', 'file')


class EventAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event.profile.through
        fields = ('profile', )

    def update(self, instance, validated_data):
        if not instance:
            raise ValidationError('Event not found!')
        instance.profile.add(self.initial_data['profile'])
        instance.save()
        return instance
