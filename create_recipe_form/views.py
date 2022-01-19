from django.shortcuts import render
from .models import CreateRecipe

# Create your views here.

def create_recipe_form(request):

    queryset = CreateRecipe.objects.all()
    context = {
        'queryset': queryset
    }
    return render(request, "create_recipe_form.html", context)

def view_your_recipes(request):

    return render(request, "view_your_recipes.html")

