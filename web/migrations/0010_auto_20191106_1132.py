# Generated by Django 2.2.5 on 2019-11-06 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_article_from'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='article_from',
            new_name='article',
        ),
    ]