from django.contrib import auth
from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(write_only=True, required=True,
                                     validators=[validate_password])
    password_repeat = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'password_repeat', 'email']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_repeat']:
            raise serializers.ValidationError(
                {'password': 'Пароли не совпадают!'})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'token')

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if username is None:
            raise ValidationError(
                'A user with this username and password not found.')

        if not user.is_active:
            raise ValidationError('This user has been deactivated.')

        return {
            'username': user.username,
            'token': user.token,
        }
