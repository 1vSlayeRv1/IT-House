# Generated by Django 3.1.11 on 2021-05-31 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('description', models.TextField(max_length=5000, verbose_name='описание')),
                ('date_start', models.DateTimeField(verbose_name='дата начала')),
                ('date_end', models.DateTimeField(verbose_name='дата окончания')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('address', models.CharField(max_length=150, verbose_name='адрес')),
                ('events', models.ManyToManyField(to='events.Event')),
            ],
            options={
                'verbose_name': 'Офис',
                'verbose_name_plural': 'Офисы',
            },
        ),
    ]
