from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CreateRecipe(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submitted_recipes', default="Some String")
    ingredients = models.TextField(null=False, blank=False)
    method = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.title
