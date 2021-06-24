import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from ItHouse.celery import app


@app.task
def send_hello_email(user_id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        html_content = render_to_string(
            'email/send_hello.html',
            context={'username': user.username})
        msg = EmailMultiAlternatives(
            'Welcome to ITHouse',
            f'Hi, {user.username} xD',
            settings.EMAIL_HOST_USER,
            ['tretyakov.main@yandex.ru'])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
    except UserModel.DoesNotExist:
        logging.warning(
            'Tried to send verification email'
            f'to non-existing user \'{user_id}\'')


@app.task
def send_access_event_email(user_id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        html_content = render_to_string(
            'email/send_hello.html', context={'username': user.username})
        msg = EmailMultiAlternatives(
            'Access Event',
            f'Hi, {user.username} xD',
            settings.EMAIL_HOST_USER,
            ['tretyakov.main@yandex.ru'])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
    except UserModel.DoesNotExist:
        logging.warning(
            'Tried to send verification email'
            f'to non-existing user \'{user_id}\'')
