from django.db import models
from django.db.models.fields.related import ForeignKey
from profiles.models import Profile


class Post(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        verbose_name='заголовок поста')

    description = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        verbose_name='краткое описание')

    content = models.TextField(
        null=False,
        blank=False,
        verbose_name='контент')

    date = models.DateTimeField(
        auto_now=True,
        null=False,
        db_index=True,
        verbose_name='дата создания')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-date']


class Comment(models.Model):
    comment = models.CharField(
        max_length=500,
        null=False,
        blank=False,
        verbose_name='комментарий')

    date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name='дата создания')

    profile = ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=False,
        blank=False)

    post = ForeignKey(
        'Post',
        related_name='comments',
        on_delete=models.CASCADE,
        null=False,
        blank=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-date']
