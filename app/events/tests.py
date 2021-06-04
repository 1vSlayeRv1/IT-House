import jwt
from datetime import datetime
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework_jwt.utils import jwt_payload_handler
from django.conf import settings
from .models import Event
from images.models import Image
import pytz
from django.test.client import MULTIPART_CONTENT, BOUNDARY, encode_multipart
class EventsTest(TestCase):
    def setUp(self):
        user = get_user_model()
        self.user = user.objects.create(email='slayer@kek.lol', username='slayer', password='keklol123123')
        image = Image.objects.create(file='test.jpg')
        Event.objects.create(
            name='Название события',
            description='Описание евента',
            date_start=datetime(2013, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC),
            date_end=datetime(2013, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC),
            file=image
        )

    def test_add_profile_to_event(self):
        payload = jwt_payload_handler(self.user)
        token = jwt.encode(payload, settings.SECRET_KEY).decode(
            'unicode_escape')

        resp = self.client.put(
                '/api/events/add/',
                data={'event': 1},
                content_type='application/json',
                **{'HTTP_AUTHORIZATION': f'Bearer {token}'}
            )
        self.assertEqual(resp.status_code, 201)

    def test_events_list(self):
        resp = self.client.get('/api/events/',)
        self.assertEqual(resp.status_code, 200)