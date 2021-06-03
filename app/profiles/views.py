import datetime
import jwt   
from django.core.exceptions import ValidationError
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.utils import jwt_payload_handler

from .serializers import UserSerializer

from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterView(APIView):
    permission_classes = (AllowAny, )

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
                return Response({'token': self.create_token(user)})
            else:
                raise ValidationError('User validate error')
        else:
            raise ValidationError('User validate error')
