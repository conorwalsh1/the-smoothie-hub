from django.shortcuts import render, redirect, get_object_or_404
from .models import CreateRecipe
from .forms import CreateRecipeForm

# Create your views here.

def view_your_recipes(request):

    queryset = CreateRecipe.objects.all()
    context = {
        'queryset': queryset
    }
    return render(request, "view_your_recipes.html", context)

def create_recipe_form(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/view_your_recipes/') 
    form = CreateRecipeForm()
    context = {
        'form' : form
    }
    return render(request, "create_recipe_form.html", context)

def edit_recipe(request, recipe_id):
    set = get_object_or_404(CreateRecipe, id=recipe_id)
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST, instance=set)
        if form.is_valid():
            form.save()
            return redirect('/view_your_recipes/') 
    form = CreateRecipeForm(instance=set)
    context = {
        'form' : form
    }
    return render(request, 'edit_recipe.html', context)

