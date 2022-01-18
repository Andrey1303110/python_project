# Generated by Django 4.0 on 2022-01-18 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_myuser_account_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='account_type',
            field=models.CharField(choices=[('1', 'Base'), ('2', 'Expert'), ('3', 'Pro')], default='1', max_length=10, verbose_name='Тип аккаунта'),
        ),
    ]
