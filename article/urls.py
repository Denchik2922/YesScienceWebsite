from django.urls import path
from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('',  ArticleListView.as_view(), name='list_article_url'),
    path('<str:slug>/', ArticleDetailView.as_view(), name='detail_article_url'),
]
