from rest_framework import serializers
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import SupportImageSerializer, SupportMessageSerializer
from rest_framework.response import Response
from rest_framework import status
from images.models import Image
from profiles.models import Profile
class CreateMessageAPI(APIView):
    permission_classes = (AllowAny, )
    serializer_class = SupportMessageSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        request.data['profile'] = request.user.pk
        serializer = SupportMessageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        request.data['support'] = serializer.data.get('id')
        serializer = SupportImageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    