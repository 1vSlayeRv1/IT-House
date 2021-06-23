from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Event
from .serializers import EventAddSerializer, EventSerializer


class ListEventsAPI(ListAPIView):
    permission_classes = (AllowAny, )
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    throttle_scope = 'checkevents'


class RetrieveUpdateDestroyEventsAPI(APIView):
    permission_classes = (IsAuthenticated, )
    throttle_scope = 'addevents'

    def put(self, request):
        request.data['profile'] = request.user.pk
        event = Event.objects.filter(pk=request.data['event']).first()
        if event:
            serializer = EventAddSerializer(event, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            else:
                raise ValidationError('Event validation error')
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request):
        event = Event.objects.filter(pk=request.data['event']).first()
        if event:
            user = get_user_model()
            user = user.objects.get(pk=request.user.pk)
            user.eventsgroups.remove(event)
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
