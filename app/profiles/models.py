from django.db import models
from django.contrib.auth.models import User
from events.models import Event

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
