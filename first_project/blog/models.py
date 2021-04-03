from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    """
    Класс, описывающий модель Статьи
    """
    title = models.CharField(max_length=250, null=False, verbose_name='Заголовок')
    massage = models.TextField(verbose_name='Текст')
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')
    public = models.BooleanField(verbose_name='Опубликовано')
    author = models.ForeignKey(User, related_name='authors', on_delete=models.PROTECT, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        # Add verbose name
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    """
    Комментарии и оценки к статьям
    """
    RATINGS = (
        (0, 'Без оценки'),
        (1, 'Ужасно'),
        (2, 'Плохо'),
        (3, 'Нормально'),
        (4, 'Хорошо'),
        (5, 'Отлично'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    message = models.TextField(default='', blank=True, verbose_name='Текст комментария')
    rating = models.IntegerField(default=0, choices=RATINGS, verbose_name='Оценка')

    def __str__(self):
        return f'{self.get_rating_display()}: {self.message or "Без комментариев"}'
