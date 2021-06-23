import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from profiles.models import Role
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.utils import jwt_payload_handler

from .serializers import (ImageProfileSerializer, ListProfileSerializer,
                          RoleSerializer, UpdateProfileSerializer,
                          UserSerializer)
from .tasks import send_hello_email

User = get_user_model()


class RegisterView(APIView):
    permission_classes = (AllowAny, )
    throttle_scope = 'signup'

    def create_token(self, user):
        payload = jwt_payload_handler(user)
        token = jwt.encode(payload, settings.SECRET_KEY)
        return token.decode('unicode_escape')

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = User.objects.get(email=request.data['email'])
            if user.check_password(request.data['password']):
                send_hello_email.delay(user.pk)
                return Response(
                    {'token': self.create_token(user)},
                    status=status.HTTP_201_CREATED)
            else:
                raise ValidationError('User validate error')
        else:
            raise ValidationError('User validate error')


class ListCreateProfileAPI(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ListProfileSerializer
    model = serializer_class.Meta.model
    throttle_scope = 'profile'

    def get_queryset(self):
        profile_id = self.request.user.pk
        queryset = self.model.objects.get(id=profile_id)
        return queryset

    def list(self, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ListProfileSerializer(queryset)
        return Response(serializer.data)

    def put(self, request):
        user = User.objects.get(pk=request.user.pk)
        serializer = UpdateProfileSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class ProfileAvatarUploadView(CreateModelMixin, APIView):
    permission_classes = (IsAuthenticated, )
    parser_classes = [MultiPartParser, FormParser]
    throttle_scope = 'imageupload'

    def post(self, request):
        profile = User.objects.get(pk=request.user.pk)
        serializer = ImageProfileSerializer(profile,
                                            data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class ProfileRoleAPI(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
    model = serializer_class.Meta.model
    throttle_scope = 'profile'
