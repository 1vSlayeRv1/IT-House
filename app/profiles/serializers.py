from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import (CharField, EmailField, ModelSerializer,
                                        ValidationError)
from rest_framework.validators import UniqueValidator

from events.models import EventGroup
from images.models import Image

Profile = get_user_model()


class ImageFileSerializer(ModelSerializer):
    file = serializers.StringRelatedField(source='file.url')

    class Meta:
        model = Image
        fields = ('file',)


class UserSerializer(ModelSerializer):
    User = get_user_model()
    email = EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())])

    password = CharField(write_only=True, required=True,
                         validators=[validate_password])
    password_repeat = CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = [
            'id', 'username',
            'password', 'password_repeat',
            'email'
        ]

    def validate(self, attrs):
        if attrs['password'] != attrs['password_repeat']:
            raise ValidationError(
                {'password': 'Пароли не совпадают!'})
        return attrs

    def create(self, validated_data):
        User = get_user_model()
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class EventProfileSerializer(ModelSerializer):
    id = serializers.StringRelatedField(source='event.id')
    event = serializers.StringRelatedField(source='event.name')
    
    class Meta:
        model = EventGroup
        fields = ('id','event', 'status')


class ListProfileSerializer(ModelSerializer):
    eventsgroups = SerializerMethodField()
    profile_image = ImageFileSerializer(read_only=True, many=True)

    def get_eventsgroups(self, obj):
        qset = EventGroup.objects.filter(profile=obj.id)
        return [EventProfileSerializer(m).data for m in qset]

    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username',
            'email', 'firstname',
            'lastname', 'phone',
            'age', 'work_exp',
            'knowledge', 'role',
            'profile_image', 'eventsgroups'
        )


class UpdateProfileSerializer(ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'id', 'firstname',
            'lastname', 'phone',
            'age', 'work_exp',
            'knowledge', 'role')

    def update(self, instance, validated_data):
        instance.firstname = validated_data['firstname']
        instance.lastname = validated_data['lastname']
        instance.phone = validated_data['phone']
        instance.age = validated_data['age']
        instance.work_exp = validated_data['work_exp']
        instance.knowledge = validated_data['knowledge']
        instance.role = validated_data['role']
        instance.save(
            update_fields=[
                'firstname', 'lastname',
                'phone', 'age',
                'work_exp', 'knowledge',
                'role'])
        return instance


class ImageProfileSerializer(ModelSerializer):

    class Meta:
        model = Profile
        fields = ('avatar', )

    def create(self, instance, validated_data):
        instance.avatar = validated_data['avatar']
        instance.save(
            update_fields=[
                'avatar'
            ]
        )
        return instance
