from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class News(models.Model):
    """
    Класс, описывающий модель
    """
    title = models.CharField(max_length=250, null=False, verbose_name='Заголовок')
    massage = models.TextField(verbose_name='Текст')
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')
    public = models.BooleanField(verbose_name='Опубликовано')
    author = models.ForeignKey(User, related_name='news_authors', on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        # Add verbose name
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
