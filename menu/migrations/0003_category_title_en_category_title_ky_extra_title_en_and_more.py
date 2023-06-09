# Generated by Django 4.1.7 on 2023-03-12 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_remove_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='title_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_ky',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='extra',
            name='title_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='extra',
            name='title_ky',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='title_en',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='food',
            name='title_ky',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
