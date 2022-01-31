# Generated by Django 4.0 on 2022-01-28 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_useroffers_offer_profit_useroffers_offer_sells_and_more'),
        ('news', '0007_alter_articles_anons_alter_articles_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.myuser', verbose_name='Автор'),
        ),
    ]