# Generated by Django 4.1.6 on 2023-02-03 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsarticle',
            old_name='new_category',
            new_name='news_category',
        ),
    ]
