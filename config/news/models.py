from django.db import models
from PIL import Image


class News(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    image = models.ImageField('Изображение', upload_to='news_images/', null=True, blank=True)
    def __str__(self):
        return f'Новость {self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'