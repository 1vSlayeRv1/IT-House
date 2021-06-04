from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class AuthTest(TestCase):
    def setUp(self):
        resp = self.client.post(reverse('signup'), {
            "username": "slayer",
            "email": "slayer@kek.lol",
            "password": "keklol123123",
            "password_repeat": "keklol123123"
        })
        self.assertEqual(resp.status_code, 201)

    def test_signin_user_valid_data(self):
        resp = self.client.post(reverse('signin'), {
            'email': 'slayer@kek.lol',
            'password': 'keklol123123'
        })
        self.assertEqual(resp.status_code, 200)

    