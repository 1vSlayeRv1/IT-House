from django.db import models
import jwt
from django.contrib.auth.models import User
from events.models import Event
from django.conf import settings
from datetime import datetime, timedelta
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True,
                             blank=True, verbose_name='телефон')
    age = models.SmallIntegerField(
        null=True, blank=True, verbose_name='возраст')
    work_exp = models.SmallIntegerField(
        null=True, blank=True, verbose_name='опыт работы')
    knowledge = models.TextField(
        max_length=3000, null=True, blank=True, verbose_name='знания')
    event = models.ForeignKey(
        Event, null=True, blank=True, on_delete=models.CASCADE)
    role = models.ForeignKey('Role', null=True, blank=True, on_delete=models.CASCADE)

    @property
    def token(self):
        """
        Позволяет получить токен пользователя путем вызова user.token, вместо
        user._generate_jwt_token(). Декоратор @property выше делает это
        возможным. token называется "динамическим свойством".
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        Этот метод требуется Django для таких вещей, как обработка электронной
        почты. Обычно это имя фамилия пользователя, но поскольку мы не
        используем их, будем возвращать username.
        """
        return self.username

    def _generate_jwt_token(self):
        """
        Генерирует веб-токен JSON, в котором хранится идентификатор этого
        пользователя, срок действия токена составляет 1 день от создания
        """
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class FieldOfInterest(models.Model):
    field = models.CharField(max_length=100, null=False,
                             blank=False, verbose_name='сфера интереса')

    def __str__(self):
        return self.field

    class Meta:
        verbose_name = 'Сфера интереса'
        verbose_name_plural = 'Сферы интересов'


class Role(models.Model):
    role = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.role

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'
