from django.db import models
from images.models import Image
from profiles.models import Profile


class Event(models.Model):
    name = models.CharField(
        max_length=100, null=False,
        blank=False,
        verbose_name='название')

    description = models.TextField(
        max_length=5000, 
        null=False, 
        blank=False, 
        verbose_name='описание')

    date_start = models.DateTimeField(
        null=False, 
        blank=False, 
        verbose_name='дата начала')

    date_end = models.DateTimeField(
        null=False, 
        blank=False, 
        verbose_name='дата окончания')

    office = models.ForeignKey(
        'Office', 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE, 
        verbose_name='офис')

    file = models.ForeignKey(
        Image, 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        verbose_name='изображение')

    profile = models.ManyToManyField(
        Profile, 
        blank=True, 
        related_name='profile_event')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ['-id']


class Office(models.Model):
    name = models.CharField(
        max_length=100, 
        null=False,
        blank=False, 
        verbose_name='название')

    address = models.CharField(
        max_length=150, 
        null=False, 
        blank=False, 
        verbose_name='адрес')

    class Meta:
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы'
