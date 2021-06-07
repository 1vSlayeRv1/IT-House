from django.core.exceptions import ValidationError
import jwt
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework_jwt.utils import jwt_payload_handler


class UploadImage(TestCase):
    def setUp(self):
        user = get_user_model()
        self.user = user.objects.create(
            email='slayer@kek.lol', username='slayer', password='keklol123123')

    def test_upload_image(self):
        payload = jwt_payload_handler(self.user)
        token = jwt.encode(payload, settings.SECRET_KEY).decode(
            'unicode_escape')

        with open('tests/101563.jpg', 'rb') as file:
            resp = self.client.post(
                '/api/images/upload/', {'file': file},
                **{'HTTP_AUTHORIZATION': f'Bearer {token}'})
        self.assertEqual(resp.status_code, 201)
