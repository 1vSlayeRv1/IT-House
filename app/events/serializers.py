from rest_framework.exceptions import ValidationError
from events.models import Event
from rest_framework.serializers import ModelSerializer, StringRelatedField
from images.models import Image


class ImageEventSerializer(ModelSerializer):
    file = StringRelatedField(source='file.url', read_only=True)

    class Meta:
        model = Image
        fields = ('file', )


class EventSerializer(ModelSerializer):
    file = ImageEventSerializer(read_only=True)
    office = StringRelatedField(source='office.address', read_only=True)
    class Meta:
        model = Event
        fields = (
            'id',
            'name',
            'description',
            'date_start',
            'date_end',
            'file',
            'office'
        )


class EventAddSerializer(ModelSerializer):

    class Meta:
        model = Event.profile.through
        fields = ('profile', )

    def update(self, instance, validated_data):
        if not instance:
            raise ValidationError('Event not found!')
        instance.profile.add(self.initial_data['profile'])
        instance.save()
        return instance
