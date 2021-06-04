from django.test import TestCase
from posts.models import Post
import jwt
from datetime import datetime
from django.contrib.auth import get_user_model
from rest_framework_jwt.utils import jwt_payload_handler
from django.conf import settings
from django.test.client import MULTIPART_CONTENT, BOUNDARY, encode_multipart


class PostTest(TestCase):
    def setUp(self):
        Post.objects.create(
            title='Топовый пост', description='Краткое описание топ поста',
            content='Ну тут очень много контента xD')

    def test_list_load_posts(self):
        resp = self.client.get('/api/posts/')
        self.assertEqual(resp.status_code, 200)

    def test_detail_load_posts(self):
        resp = self.client.get('/api/posts/1')
        self.assertEqual(resp.status_code, 200)


class CommentTest(TestCase):
    def setUp(self):
        user = get_user_model()
        self.user = user.objects.create(
            email='slayer@kek.lol', username='slayer', password='keklol123123')
    def test_create_comment_to_post(self):
        payload = jwt_payload_handler(self.user)
        token = jwt.encode(payload, settings.SECRET_KEY).decode(
            'unicode_escape')

        resp = self.client.post(
                '/api/posts/comment/',
                {'comment': 'Топовый коммент', 'post': 1},
                **{'HTTP_AUTHORIZATION': f'Bearer {token}'}
            )
        self.assertEqual(resp.status_code, 201)