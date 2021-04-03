from datetime import datetime

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import Serializer, IntegerField

from .models import Article, Comment


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


class QuerySerializer(Serializer):
    limit = IntegerField(min_value=1, default=5, required=False)
    offset = IntegerField(min_value=0, default=0, required=False)


class CommentAddSerializer(serializers.ModelSerializer):
    """ Добавление комментария """
    author = AuthorSerializer(read_only=True)
    article = OneArticleViewSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ['date_add', 'author', 'note']


class CommentViewSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = Comment
        fields = '__all__'
