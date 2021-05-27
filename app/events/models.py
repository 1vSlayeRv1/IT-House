from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='название')
    description = models.TextField(max_length=5000, null=False, blank=False, verbose_name='описание')
    date_start = models.DateTimeField(null=False, blank=False, verbose_name='дата начала')
    date_end = models.DateTimeField(null=False, blank=False, verbose_name='дата окончания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

class Office(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='название')
    address = models.CharField(max_length=150, null=False, blank=False, verbose_name='адрес')
    events = models.ManyToManyField('Event')
    class Meta:
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы'