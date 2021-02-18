# Generated by Django 3.1.6 on 2021-02-18 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Заголовок')),
                ('poster', models.ImageField(upload_to='articles_poster/', verbose_name='Изображение')),
                ('url', models.SlugField(blank=True, max_length=30, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='ArticleText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Заголовок Текста')),
                ('text', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Текст')),
                ('image', models.ImageField(upload_to='text_image/', verbose_name='Изображение')),
                ('rotate', models.BooleanField(default=True, verbose_name='Обратное изображение')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='article.article', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Текст',
                'verbose_name_plural': 'Текста',
            },
        ),
    ]
