from django import forms
from .models import CreateRecipe


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = CreateRecipe
        fields = ['title', 'ingredients', 'method']