from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Article, ArticleText


class ListArticleText(admin.StackedInline):
    model = ArticleText
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image', 'url')
    readonly_fields = ('get_image',)
    inlines = [ListArticleText]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="50" height=""60 >')

    get_image.short_description = 'Изображение'


@admin.register(ArticleText)
class ArticleTextAdmin(admin.ModelAdmin):
    list_display = ('title', 'article', 'get_image')
    readonly_fields = ('get_image',)


    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height=""60 >')

    get_image.short_description = 'Изображение'