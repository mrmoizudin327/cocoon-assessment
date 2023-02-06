from django.db import models
from tinymce import models as tinymce_models


class Author(models.Model):
    """Author model"""
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    job_description = models.TextField()

    def __str__(self):
        return "%s %s" % (self.name, self.surname)


class NewsCategory(models.Model):
    """News Category Model"""
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class NewsArticle(models.Model):
    """News Model"""
    title = models.CharField(max_length=255, unique=True)
    summary = models.TextField()
    content = tinymce_models.HTMLField()
    published = models.BooleanField(default=True)
    published_date = models.DateTimeField(auto_now_add=True)
    news_category = models.ForeignKey(NewsCategory, null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

