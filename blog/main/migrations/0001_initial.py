# Generated by Django 4.0 on 2022-01-08 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=250, verbose_name='Фамилия')),
                ('avatar', models.ImageField(default=None, upload_to='images', verbose_name='Изображение')),
                ('money', models.TextField(verbose_name='Деньги')),
                ('date_reg', models.DateTimeField(verbose_name='Дата регистрации')),
            ],
        ),
    ]