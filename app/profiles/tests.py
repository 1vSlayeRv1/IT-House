from django.test import TestCase
from django.urls import reverse


class AuthTest(TestCase):
    def setUp(self):
        resp = self.client.post(reverse('signup'), {
            "username": "slayer",
            "email": "slayer@kek.lol",
            "password": "keklol123123",
            "password_repeat": "keklol123123"
        })
        self.assertEqual(resp.status_code, 201)

    def test_signin_user_valid(self):
        resp = self.client.post(reverse('signin'), {
            'email': 'slayer@kek.lol',
            'password': 'keklol123123'
        })
        self.assertEqual(resp.status_code, 200)

    def test_create_user_invalid(self):
        usernames = ['askdlasklda@sadas', '!sasad12421sad$!@$',
                     'sal!$!@<sda', '010141240212041', 'slayer']
        emails = ['slayer@kek.', 'slayer@k', 'slayer.kek', 'sl@k']
        passwords = ['132', 'slayer', 'kek', '1',
                     '', '12941294821921', 'asasasasasasas']
        for u in usernames:
            for e in emails:
                for p in passwords:
                    resp = self.client.post(reverse('signup'), {
                        "username": f"{u}",
                        "email": f"{e}",
                        "password": f"{p}",
                        "password_repeat": f"{p}"
                    })
        self.assertEqual(resp.status_code, 400)

    def test_signin_user_invalid(self):
        emails = ['slayer@kek.lo', 'slayer@ke', 'slayer', 'lol', '']
        passwords = ['keklol12312', 'Keklol', '123', '1',
                     '1221412412521521521521125kl25112!!!%#', '']
        for e in emails:
            for p in passwords:
                resp = self.client.post(reverse('signin'), {
                    'email': f'{e}',
                    'password': f'{p}'
                })
        self.assertEqual(resp.status_code, 400)
