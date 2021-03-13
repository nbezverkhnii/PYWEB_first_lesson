from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=250, null=False, verbose_name='Заголовок')
    massage = models.TextField(verbose_name='Текст')
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')
    public = models.BooleanField(verbose_name='Опубликовано')

    def __str__(self):
        return self.title

    class Meta:
        # Add verbose name
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'
