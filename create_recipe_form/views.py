from django.shortcuts import render, redirect
from .models import CreateRecipe

# Create your views here.

def view_your_recipes(request):

    queryset = CreateRecipe.objects.all()
    context = {
        'queryset': queryset
    }
    return render(request, "view_your_recipes.html", context)

def create_recipe_form(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        ingredients = request.POST.get('ingredients')
        method = request.POST.get('method')
        CreateRecipe.objects.create(ingredients=ingredients, method=method, title=title)

        return redirect('/view_your_recipes/') 
        
    return render(request, "create_recipe_form.html")

