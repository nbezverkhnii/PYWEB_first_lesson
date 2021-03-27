from datetime import datetime
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Article


class AuthorSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'date_joined')


class OneArticleViewSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = Article
        exclude = ('public',)  # Исключить эти поля

    def to_representation(self, instance):
        """ Переопределение вывода. Меняем формат даты в ответе """
        ret = super().to_representation(instance)
        # Конвертируем строку в дату по формату
        date_time = datetime.strptime(ret['date_time'], '%Y-%m-%dT%H:%M:%S.%f')
        # Конвертируем дату в строку в новом формате
        ret['date_time'] = date_time.strftime('%d %B %Y %H:%M:%S')
        return ret


class ArticlesViewSerializer(serializers.ModelSerializer):
    """

    """
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'massage', 'date_time', 'author']


class ArticleEditorSerializer(serializers.ModelSerializer):
    """

    """
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ['date_time', 'author', ]

