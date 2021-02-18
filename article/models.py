from django.db import models
from django.urls import reverse
from django.utils.text import slugify


def generate_url(string):
    url = slugify(string, allow_unicode=True)
    return url


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=40)
    poster = models.ImageField('Изображение', upload_to='articles_poster/')
    url = models.SlugField('URL', blank=True, max_length=30, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.url = generate_url(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('detail_article_url', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-title']


class ArticleText(models.Model):
    title = models.CharField('Заголовок Текста', max_length=40)
    text = models.TextField('Текст', blank=True, null=True, max_length=1000)
    image = models.ImageField('Изображение', upload_to='text_image/')
    article = models.ForeignKey(Article, verbose_name='Пост', on_delete=models.CASCADE)
    rotate = models.BooleanField('Обратное изображение', default=True)

    def __str__(self):
        return 'Текст для статьи "' + str(self.article) + '"'

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Текста'
