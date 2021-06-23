from images.models import Image
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SupportSection
from .serializers import SupportMessageSerializer, SupportSectionSerializer


class CreateMessageAPI(APIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = SupportMessageSerializer
    parser_classes = [MultiPartParser, FormParser]
    throttle_scope = 'support'

    def get(self, request):
        queryset = SupportSection.objects.all()
        serializer = SupportSectionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SupportMessageSerializer(
            data=request.data, context={'profile': request.user})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            for f in request.data.getlist('file'):
                image = Image.objects.create(file=f)
                image.support.add(serializer.data.get('id'))
                image.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
