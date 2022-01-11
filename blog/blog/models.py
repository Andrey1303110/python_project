from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    name = models.CharField('Имя', max_length=50)
    avatar = models.ImageField(upload_to='images/users', verbose_name='Изображение')

    def __str__(self):
        return self.user

