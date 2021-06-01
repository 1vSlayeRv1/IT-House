# Generated by Django 3.1.11 on 2021-06-01 10:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_comment_profile'),
        ('images', '0002_auto_20210601_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='post',
            field=models.ManyToManyField(blank=True, null=True, to='posts.Post'),
        ),
        migrations.AlterField(
            model_name='image',
            name='profile',
            field=models.ManyToManyField(blank=True, null=True, related_name='profile_image', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='image',
            name='support',
            field=models.ManyToManyField(blank=True, null=True, to='support.MessageToSupport'),
        ),
    ]
