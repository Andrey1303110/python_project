from datetime import datetime
from django.db import models
from users.models import MyUser


class Articles(models.Model):
    title = models.CharField('Название', max_length=50, blank=False, default=None)
    anons = models.CharField('Анонс', max_length=250, blank=False, default=None)
    image = models.ImageField(upload_to='images', verbose_name='Изображение', blank=False, default=None)
    full_text = models.TextField('Статья', blank=False, default=None)
    date = models.DateTimeField('Дата публикации', default=datetime.now, blank=True)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, blank=False, default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
