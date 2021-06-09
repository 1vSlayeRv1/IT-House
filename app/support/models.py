from django.db import models

from profiles.models import Profile


class MessageToSupport(models.Model):
    title = models.CharField(
        max_length=100, 
        null=False,
        blank=False, 
        verbose_name='заголовок')

    content = models.TextField(
        max_length=3000, 
        null=False, 
        blank=False, 
        verbose_name='текст')

    date = models.DateTimeField(
        auto_now_add=True, 
        null=False, 
        blank=False,
        verbose_name='дата создания')

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    section = models.ForeignKey('SupportSection', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сообщение в поддержку'
        verbose_name_plural = 'Сообщения в поддержку'

class SupportSection(models.Model):
    section = models.CharField(
        max_length=150, 
        null=False, 
        blank=False,
        verbose_name='название раздела')

    def __str__(self):
        return self.section

    class Meta:
        verbose_name = 'Раздел поддержки'
        verbose_name_plural = 'Разделы поддержки'
