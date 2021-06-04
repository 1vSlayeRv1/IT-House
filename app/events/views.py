from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Event
from .serializers import EventAddSerializer, EventSerializer


class ListEventsAPI(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class RetrieveUpdateDestroyEventsAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = EventAddSerializer
    queryset = Event.objects.all()

    def put(self, request):
        request.data['profile'] = request.user.pk
        event = Event.objects.filter(pk=request.data['event']).first()
        if event:
            serializer = EventAddSerializer(event, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'registration': 'success'}, status=status.HTTP_201_CREATED)
            else:
                raise ValidationError('Event Error')
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
