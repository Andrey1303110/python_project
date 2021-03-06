# Generated by Django 4.0 on 2022-01-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('fio', models.CharField(default='', max_length=100, verbose_name='ФИО')),
                ('telegram', models.CharField(default='', max_length=100, verbose_name='Telegram')),
                ('money', models.IntegerField(default=0, verbose_name='Баланс')),
                ('companys', models.IntegerField(default=0, verbose_name='Кампании')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
