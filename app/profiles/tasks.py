import logging

from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from ItHouse.celery import app
from django.conf import settings

@app.task
def send_hello_email(user_id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        send_mail('Welcome to ITHouse', f'Hi, {user.username} xD', settings.EMAIL_HOST_USER, ['tretyakov.main@yandex.ru'])
    except UserModel.DoesNotExist:
        logging.warning(f"Tried to send verification email to non-existing user '{user_id}'")
