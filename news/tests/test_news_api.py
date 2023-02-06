"""
Tests for news api.
"""
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status


class NewsApiTests(TestCase):
    """Tests for the news api."""

    def setUp(self):
        self.client = APIClient()

    def test_get_authors(self):
        """Test getting authors successfully."""
        res = self.client.get('/api/news/authors/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_categories(self):
        """Test getting news categories successfully."""
        res = self.client.get('/api/news/categories/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_articles(self):
        """Test getting news articles successfully."""
        res = self.client.get('/api/news/articles/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
