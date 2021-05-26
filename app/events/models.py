from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=5000, null=False, blank=False)
    date_start = models.DateTimeField(auto_now_add=True, null=False)
    date_end = models.DateTimeField(null=False, blank=False)

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'