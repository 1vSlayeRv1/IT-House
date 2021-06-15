# Generated by Django 3.1.11 on 2021-06-15 11:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_auto_20210615_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='profile',
            field=models.ManyToManyField(blank=True, related_name='profile_event', to=settings.AUTH_USER_MODEL),
        ),
    ]
