# Generated by Django 4.0 on 2022-01-19 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_myuser_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_message', models.CharField(default='', max_length=500, verbose_name='Текст')),
                ('from_message', models.EmailField(default='', max_length=254, verbose_name='Отпарвитель')),
                ('to_message', models.EmailField(default='', max_length=254, verbose_name='Получатель')),
                ('time', models.DateTimeField(verbose_name='Время отправки')),
            ],
        ),
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.ImageField(default='static/main/img/stock_avatar.png', null=True, upload_to='images/', verbose_name='Аватар'),
        ),
    ]