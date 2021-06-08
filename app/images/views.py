from rest_framework import views
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import ImageProfileSerializer


class ProfileFileUploadView(views.APIView):
    permission_classes = (IsAuthenticated, )
    parser_classes = [MultiPartParser, FormParser]
    throttle_scope = 'imageupload'

    def post(self, request):
        serializer = ImageProfileSerializer(
            data=request.data, context={'profile': request.user})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
