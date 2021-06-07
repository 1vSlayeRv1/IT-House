from django.test import TestCase
from posts.models import Post
import jwt
from django.contrib.auth import get_user_model
from rest_framework_jwt.utils import jwt_payload_handler
from django.conf import settings


class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(
            title='Топовый пост1', description='Краткое описание топ поста1',
            content='1Ну тут очень много контента xD')

    def test_list_load_posts(self):
        resp = self.client.get('/api/posts/')
        self.assertEqual(resp.status_code, 200)

    def test_detail_load_posts(self):
        resp = self.client.get('/api/posts/2')
        self.assertEqual(resp.status_code, 200)


class CommentTest(TestCase):
    def setUp(self):
        user = get_user_model()
        user = user.objects.create(
            email='slayer@kek.lol', username='slayer', password='keklol123123')
        payload = jwt_payload_handler(user)
        self.token = jwt.encode(payload, settings.SECRET_KEY).decode(
            'unicode_escape')
        Post.objects.create(
            title='Топовый пост', description='Краткое описание топ поста',
            content='Ну тут очень много контента xD')

    def test_create_comment_to_post(self):

        resp = self.client.post(
            '/api/posts/comment/',
            {'comment': 'The Best Comment', 'post': 1},
            **{'HTTP_AUTHORIZATION': f'Bearer {self.token}'})
        self.assertEqual(resp.status_code, 201)
