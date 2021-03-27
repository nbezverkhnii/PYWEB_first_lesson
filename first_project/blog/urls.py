from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('articles/', views.ArticlesView.as_view(), name='articles'),
    path('article/add/', views.ArticleEditorView.as_view(), name='add'),
    path('article/<int:article_id>/', views.OneArticleView.as_view(), name='one_article'),
    path('article/<int:article_id>/edit/', views.ArticleEditorView.as_view(), name='edit'),
    path('article/<int:article_id>/del/', views.ArticleEditorView.as_view(), name='del'),
]

