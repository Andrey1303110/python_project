# Generated by Django 4.0 on 2022-01-14 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_myuser_companys_myuser_money_myuser_telegram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='companys',
            field=models.IntegerField(default=0, verbose_name='Кампаний'),
        ),
    ]
