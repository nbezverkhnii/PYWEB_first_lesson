from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """

    """
    # Отображение в режимепросмотра
    list_display = ('title', 'public', 'massage', 'author')
    # Отображение полей в режиме редактирования
    fields = (('title', 'author'), 'massage', 'date_time', 'public')
    # Поля только для чтения в режиме редактирования
    readonly_fields = ('date_time',)
    # Поля для поиска
    search_fields = ('title', 'massage')
    # Поля фильтрации
    list_filter = ['public', 'author', 'date_time']


    def save_model(self, request, obj, form, change):
        """
        Переопределяем метод для сохранения статьи без указания автора
        Теперь автор будет подставляться прямо из запроса request.user
        """
        if not hasattr(obj, 'author') or not obj.author:
            obj.author = request.user
        super().save_model(request, obj, form, change)
