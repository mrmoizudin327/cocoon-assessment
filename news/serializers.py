"""
Serializers for News API view
"""
from rest_framework import serializers

from news.models import NewsArticle, NewsCategory, Author


class AuthorSerializer(serializers.ModelSerializer):
    """Serializer for Author"""

    class Meta:
        model = Author
        fields = ['id', 'name', 'surname', 'job_description']
        read_only_fields = ['id']


class NewsCategorySerializer(serializers.ModelSerializer):
    """Serializer for News Category"""

    class Meta:
        model = NewsCategory
        fields = ['id', 'name']
        read_only_fields = ['id']


class NewsArticlesSerializer(serializers.ModelSerializer):
    """Serializer for News Articles"""

    class Meta:
        model = NewsArticle
        fields = ['id', 'title', 'summary', 'content', 'published', 'published_date', 'author', 'news_category']
        read_only_fields = ['id']

