from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from images.models import Image
from .serializers import SupportMessageSerializer


class CreateMessageAPI(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = SupportMessageSerializer
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        request.data._mutable = True
        request.data['profile'] = request.user.pk
        request.data._mutable = False
        serializer = SupportMessageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            for f in request.data.getlist('file'):
                image = Image.objects.create(file=f)
                image.support.add(serializer.data.get('id'))
                image.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
