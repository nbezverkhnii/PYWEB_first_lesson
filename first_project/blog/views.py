from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from .models import Article
from .serializers import OneArticleViewSerializer, ArticlesViewSerializer, ArticleEditorSerializer


class OneArticleView(APIView):
    """

    """
    def get(self, request, article_id):
        """

        """
        article = Article.objects.filter(pk=article_id, public=True).first()

        if not article:
            raise NotFound(f'Опубликованная статья с id={article_id} не найдена')

        serializer = OneArticleViewSerializer(article)
        return Response(serializer.data)

class ArticlesView(APIView):
    """

    """
    def get(self, request):
        """
        Получение всех статей блога
        """
        articles = Article.objects.filter(public=True).order_by('date_time')
        serializer = ArticlesViewSerializer(articles, many=True)

        return Response(serializer.data)

class ArticleEditorView(APIView):
    """

    """
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def check_valid(new_article, request):
        if new_article.is_valid():
            new_article.save(author=request.user)
            return Response(new_article.data, status=status.HTTP_201_CREATED)
        else:
            return Response(new_article.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """

        """
        new_article = ArticleEditorSerializer(data=request.data)
        return self.check_valid(new_article, request)

    def patch(self, request, article_id):
        """

        """
        article = Article.objects.filter(pk=article_id, author=request.user).first()
        if not article:
            raise NotFound(f'Статья с id={article_id} у пользователя {request.user.username} не найдена')

        new_article = ArticleEditorSerializer(article, data=request.data, partial=True)
        return self.check_valid(new_article, request)

    def delete(self, request, article_id):
        """

        """
        article = Article.objects.filter(pk=article_id, author=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
