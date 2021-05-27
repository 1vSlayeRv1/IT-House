from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from events.models import Event
from roles.models import Role

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, null=False, blank=False, verbose_name='имя')
    lastname = models.CharField(max_length=100, null=False, blank=False, verbose_name='фамилия')
    email = models.EmailField(unique=True, null=False, blank=False, verbose_name='почта')
    phone = models.CharField(max_length=15, null=False, blank=False, verbose_name='телефон')
    age = models.SmallIntegerField(null=False, blank=False, verbose_name='возраст')
    work_exp = models.SmallIntegerField(null=False, blank=False, verbose_name='опыт работы')
    knowledge = models.TextField(max_length=3000, null=False, blank=False, verbose_name='знания')
    date_reg = models.DateTimeField(auto_now_add=True, verbose_name='дата регистрации')
    event_id = models.ForeignKey(Event, null=True, blank=True, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        verbose_name ='Профиль'
        verbose_name_plural = 'Профили'

class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='заголовок поста')
    description = models.CharField(max_length=250, null=False, blank=False, verbose_name='краткое описание')
    content = models.TextField(null=False, blank=False, verbose_name='контент')
    date = models.DateTimeField(auto_now_add=True, null=False, db_index=True, verbose_name='дата создания')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
