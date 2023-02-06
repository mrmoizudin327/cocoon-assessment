"""
Views for news
"""
from rest_framework import viewsets

from news.serializers import (AuthorSerializer, NewsArticlesSerializer, NewsCategorySerializer)
from news.models import (Author, NewsCategory, NewsArticle)


class AuthorViewset(viewsets.ModelViewSet):
    """Views for manage author APIs."""
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class NewsCategoryViewset(viewsets.ModelViewSet):
    """Views for manage news categories APIs."""
    serializer_class = NewsCategorySerializer
    queryset = NewsCategory.objects.all()


class NewsArticleViewset(viewsets.ModelViewSet):
    """Views for manage news categories APIs."""
    serializer_class = NewsArticlesSerializer
    queryset = NewsArticle.objects.all()
