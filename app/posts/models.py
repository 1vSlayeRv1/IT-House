from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from events.models import Event
from roles.models import Role

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, null=False, blank=False)
    lastname = models.CharField(max_length=100, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    age = models.SmallIntegerField(null=False, blank=False)
    work_exp = models.SmallIntegerField(null=False, blank=False)
    knowledge = models.TextField(max_length=3000, null=False, blank=False)
    date_reg = models.DateTimeField(auto_now_add=True)
    event_id = models.ForeignKey(Event, null=True, blank=True, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        verbose_name ='Профиль'
        verbose_name_plural = 'Профили'

class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=250, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True, null=False)
    profile_id = ForeignKey('Profile', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
