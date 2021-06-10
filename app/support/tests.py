import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework_jwt.utils import jwt_payload_handler

from .models import SupportSection


class CreateSupportTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = get_user_model()
        user.objects.create(email='slayer@kek.lol',
                            username='slayer', password='keklol123123')
        SupportSection.objects.create(section='Тестовая секция')
        user = user.objects.get(email='slayer@kek.lol')
        payload = jwt_payload_handler(user)
        cls.token = jwt.encode(payload, settings.SECRET_KEY).decode(
            'unicode_escape')

    def test_create_support_valid_message(self):

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

    def test_create_support_invalid_message(self):

        with open('tests/101563.jpg', 'rb') as file:
            resp = self.client.post(
                '/api/support/',
                {'title': 'kek', 'content': 'lol',
                    'section': 999, 'file': file},
                **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        self.assertEqual(resp.status_code, 400)

        resp = self.client.post(
            '/api/support/',
            {'title': '', 'content': 'lol', 'section': 1},
            **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        self.assertEqual(resp.status_code, 400)

        with open('tests/101563.jpg', 'rb') as file, \
                open('tests/101563.jpg', 'rb') as file2:
            file = [file, file2]
            resp = self.client.post(
                '/api/support/',
                {'title': 'kek', '': 'lol', 'section': 1, 'file': file},
                **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        self.assertEqual(resp.status_code, 400)
