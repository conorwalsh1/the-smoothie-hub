# Generated by Django 3.2 on 2022-01-18 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_post_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='method',
            field=models.TextField(blank=True),
        ),
    ]
