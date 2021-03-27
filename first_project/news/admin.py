from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """
    Настройка вида панели администратора для работы с моделью Статья
    """
    # Отображение в режимепросмотра
    list_display = ('title', 'public', 'massage')
    # Отображение полей в режиме редактирования
    fields = ('title', 'massage', 'date_time', 'public')
    # Поля только для чтения в режиме редактирования
    readonly_fields = ('date_time',)
    # Поля для поиска
    search_fields = ('title', 'massage')
    # Поля фильтрации
    list_filter = ['public', 'date_time']