# Generated by Django 3.1.11 on 2021-06-18 13:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=150, verbose_name='название раздела')),
            ],
            options={
                'verbose_name': 'Раздел поддержки',
                'verbose_name_plural': 'Разделы поддержки',
            },
        ),
        migrations.CreateModel(
            name='MessageToSupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('content', models.TextField(max_length=3000, verbose_name='текст')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.supportsection')),
            ],
            options={
                'verbose_name': 'Сообщение в поддержку',
                'verbose_name_plural': 'Сообщения в поддержку',
            },
        ),
    ]
