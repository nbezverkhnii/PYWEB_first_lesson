# Generated by Django 3.1.7 on 2021-03-26 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('massage', models.TextField(verbose_name='Текст')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')),
                ('public', models.BooleanField(verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новости',
            },
        ),
    ]