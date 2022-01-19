from django.db import models

# Create your models here.

class CreateRecipe(models.Model):

    title = title = models.CharField(max_length=200, unique=True, default=False)
    ingredients = models.TextField(null=False, blank=False)
    method = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.title
