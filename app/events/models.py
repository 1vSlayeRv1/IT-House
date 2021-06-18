from django.db import models

from images.models import Image
from profiles.models import Profile
from profiles.tasks import send_hello_email


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

    registration = models.ManyToManyField(
        Profile,
        blank=True,
        through='EventGroup',
        related_name='eventsgroups')

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

    def __str__(self):
        return self.name


class EventGroup(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('Wait', 'Wait'),
        ('Access', 'Access')
    ]
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default=STATUS_CHOICES[0][0])

    def __str__(self):
        return self.event.name

    def save(self):
        if self.status == 'Access':
            send_hello_email(self.profile.pk)
        super().save()

    class Meta:
        verbose_name = 'Событие с набором участников'
        verbose_name_plural = 'События с подтвержденными участниками'
