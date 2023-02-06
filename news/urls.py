"""
URL mappings for the news app
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from news import views

router = DefaultRouter()
router.register('authors', views.AuthorViewset)
router.register('categories', views.NewsCategoryViewset)
router.register('articles', views.NewsArticleViewset)

app_name = 'news'

"""URL patterns new news app."""
urlpatterns = [
    path('', include(router.urls)),
]
