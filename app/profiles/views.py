import datetime
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


from .serializers import UserSerializer

from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            raise ValidationError('User validate error')
