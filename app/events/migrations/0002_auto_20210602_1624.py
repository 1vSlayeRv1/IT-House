# Generated by Django 3.1.11 on 2021-06-02 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0009_remove_image_event'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='images.image', verbose_name='изображение'),
        ),
        migrations.AddField(
            model_name='event',
            name='profile',
            field=models.ManyToManyField(blank=True, related_name='profile_event', to=settings.AUTH_USER_MODEL),
        ),
    ]
