from django.db import models


class News(models.Model):
    title = models.CharField('Название статьи', max_length=50)
    data = models.DateTimeField('Дата публикации')
    short_text = models.CharField('Краткое описание', max_length=250)
    full_text = models.TextField('Полный текст новости')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
