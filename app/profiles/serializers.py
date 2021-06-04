from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from posts.serializers import ImageFileSerializer
from events.models import Event


class UserSerializer(serializers.ModelSerializer):
    User = get_user_model()
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(write_only=True, required=True,
                                     validators=[validate_password])
    password_repeat = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'password', 'password_repeat', 'email']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_repeat']:
            raise serializers.ValidationError(
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


class EventProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event.profile.through
        fields = ('id', )


class ListProfileSerializer(serializers.ModelSerializer):
    profile_event = EventProfileSerializer(read_only=True, many=True)
    profile_image = ImageFileSerializer(read_only=True, many=True)

    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username', 'email', 'firstname', 'lastname', 'phone', 'age',
            'work_exp', 'knowledge', 'role', 'profile_image', 'profile_event')


class UpdateProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'firstname', 'lastname',
                  'phone', 'age', 'work_exp', 'knowledge', 'role')

    def update(self, instance, validated_data):
        instance.firstname = validated_data['firstname']
        instance.lastname = validated_data['lastname']
        instance.phone = validated_data['phone']
        instance.age = validated_data['age']
        instance.work_exp = validated_data['work_exp']
        instance.knowledge = validated_data['knowledge']
        instance.role = validated_data['role']
        instance.save(
            update_fields=['firstname', 'lastname', 'phone', 'age', 'work_exp',
                           'knowledge', 'role'])
        return instance
