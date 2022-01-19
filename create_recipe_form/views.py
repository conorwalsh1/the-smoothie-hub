from django.shortcuts import render, redirect
from .models import CreateRecipe

# Create your views here.

def create_recipe_form(request):

    queryset = CreateRecipe.objects.all()
    context = {
        'queryset': queryset
    }
    return render(request, "create_recipe_form.html", context)

def view_your_recipes(request):
    if request.method == 'POST':
        ingredients = request.POST.get('ingredients')
        method = request.POST.get('method')
        CreateRecipe.objects.create(ingredients=ingredients, method=method)

        return redirect('create_recipe_form.html')
    return render(request, "view_your_recipes.html")

