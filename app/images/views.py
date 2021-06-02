from rest_framework import views
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from rest_framework import status
from .serializers import ImageProfileSerializer


class ProfileFileUploadView(views.APIView):
    permission_classes = (AllowAny, )
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        request.data['profile'] = request.user.pk
        serializer = ImageProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
