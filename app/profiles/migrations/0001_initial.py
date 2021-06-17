# Generated by Django 3.1.11 on 2021-06-15 11:36

import uuid

import django.db.models.deletion
import images.utilities
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldOfInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=100, verbose_name='сфера интереса')),
            ],
            options={
                'verbose_name': 'Сфера интереса',
                'verbose_name_plural': 'Сферы интересов',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Роль',
                'verbose_name_plural': 'Роли',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, max_length=255, unique=True)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('avatar', models.ImageField(blank=True, default='test.jpg', null=True, upload_to=images.utilities.get_timestamp_path, verbose_name='аватар')),
                ('firstname', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя')),
                ('lastname', models.CharField(blank=True, max_length=100, null=True, verbose_name='Фамилия')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='телефон')),
                ('age', models.SmallIntegerField(blank=True, null=True, verbose_name='возраст')),
                ('work_exp', models.SmallIntegerField(blank=True, null=True, verbose_name='опыт работы')),
                ('knowledge', models.TextField(blank=True, max_length=3000, null=True, verbose_name='знания')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.role')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
