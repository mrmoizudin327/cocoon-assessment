from django.contrib import admin
from .models import Author, NewsCategory, NewsArticle

"""Registering Author model to admin site."""
admin.site.register(Author)

"""Registering News Category model to admin site."""
admin.site.register(NewsCategory)

"""Registering News Articles model to admin site."""
admin.site.register(NewsArticle)
