import jwt
from datetime import datetime
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework_jwt.utils import jwt_payload_handler
from django.conf import settings
from .models import Event
from images.models import Image
import pytz

class EventsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = get_user_model()
        user = user.objects.create(
            email='slayer@kek.lol', username='slayer', password='keklol123123')
        image = Image.objects.create(file='test.jpg')
        Event.objects.create(
            name='Название события', description='Описание евента',
            date_start=datetime(
                2013, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC),
            date_end=datetime(
                2013, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC),
            file=image)
        payload = jwt_payload_handler(user)
        cls.token = jwt.encode(payload, settings.SECRET_KEY).decode(
            'unicode_escape')

    def test_add_profile_to_event(self):

        resp = self.client.put(
            '/api/events/add/',
            data={'event': 1},
            content_type='application/json',
            **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'}
        )
        self.assertEqual(resp.status_code, 201)

    def test_add_profile_to_invalid_event(self):

        resp = self.client.put(
            '/api/events/add/',
            data={'event': 999},
            content_type='application/json',
            **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'}
        )
        self.assertEqual(resp.status_code, 400)

    def test_events_list(self):
        resp = self.client.get('/api/events/',)
        self.assertEqual(resp.status_code, 200)

    def test_delete_event_from_profile(self):
        resp = self.client.delete(
            '/api/events/add/',
            data={'event': '1'},
            content_type='application/json',
            **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'}
        )
        self.assertEqual(resp.status_code, 200)

    def test_delete_invalud_event_from_profile(self):
        resp = self.client.delete(
            '/api/events/add/',
            data={'event': '999'},
            content_type='application/json',
            **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'}
        )
        self.assertEqual(resp.status_code, 400)
