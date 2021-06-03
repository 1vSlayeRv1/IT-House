from rest_framework import serializers

from .models import MessageToSupport


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
