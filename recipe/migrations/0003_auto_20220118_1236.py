# Generated by Django 3.2 on 2022-01-18 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_post_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AddField(
            model_name='post',
            name='ingredients',
            field=models.TextField(default='Ingredients', null=True, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='method',
            field=models.TextField(default='Method'),
        ),
    ]
