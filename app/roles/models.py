from django.db import models

class Role(models.Model):
    role = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.role
    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'
