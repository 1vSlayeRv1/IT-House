import jwt
from django.test import TestCase
from django.conf import settings
from rest_framework_jwt.utils import jwt_payload_handler
from django.contrib.auth import get_user_model
from .models import SupportSection


class CreateSupportTest(TestCase):
    def setUp(self):
        self.user = get_user_model()
        self.user.objects.create(email='slayer@kek.lol',
                                 username='slayer', password='keklol123123')
        SupportSection.objects.create(section='Тестовая секция')
        self.user = self.user.objects.get(email='slayer@kek.lol')
        payload = jwt_payload_handler(self.user)
        self.token = jwt.encode(payload, settings.SECRET_KEY).decode(
            'unicode_escape')

    def test_create_support_message(self):

        with open('tests/101563.jpg', 'rb') as file:
            resp = self.client.post(
                '/api/support/',
                {'title': 'kek', 'content': 'lol', 'section': 1, 'file': file},
                **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        self.assertEqual(resp.status_code, 201)
        resp = self.client.post(
            '/api/support/',
            {'title': 'kek', 'content': 'lol', 'section': 1},
            **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        self.assertEqual(resp.status_code, 201)
        with open('tests/101563.jpg', 'rb') as file, \
                open('tests/101563.jpg', 'rb') as file2:
            file = [file, file2]
            resp = self.client.post(
                '/api/support/',
                {'title': 'kek', 'content': 'lol', 'section': 1, 'file': file},
                **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        self.assertEqual(resp.status_code, 201)
