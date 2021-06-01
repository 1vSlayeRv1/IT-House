from re import M
from rest_framework import views, generics
from rest_framework import parsers
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import ImageProfileSerializer
from .utilities import get_timestamp_path
import json


class ProfileFileUploadView(views.APIView):
    permission_classes = (AllowAny, )
    parser_classes = [FileUploadParser]
    def post(self, request):
        request.data['profile'] = [request.user.pk]
        serializer = ImageProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    