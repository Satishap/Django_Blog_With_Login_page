# Generated by Django 2.2.5 on 2019-11-06 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='article_from',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_type', models.CharField(max_length=100)),
                ('First_Name', models.CharField(max_length=100)),
                ('Last_Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]