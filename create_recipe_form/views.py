from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import CreateRecipe
from .forms import CreateRecipeForm

# This function renders the view_your_recipes.html page


def view_your_recipes(request):

    queryset = CreateRecipe.objects.all()
    context = {
        'queryset': queryset
    }
    return render(request, "view_your_recipes.html", context)


# This function handles the create recipe form


def create_recipe_form(request):
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('/view_your_recipes/')
    form = CreateRecipeForm()
    context = {
        'form': form
    }
    return render(request, "create_recipe_form.html", context)


# This function handles the edit recipe form


def edit_recipe(request, recipe_id):
    set = get_object_or_404(CreateRecipe, id=recipe_id)
    if request.method == 'POST':
        form = CreateRecipeForm(request.POST, instance=set)
        if form.is_valid():
            messages.success(request, 'Recipe edited successfully.')
            form.save()
            return redirect('/view_your_recipes/')
    form = CreateRecipeForm(instance=set)
    context = {
        'form': form
    }
    return render(request, 'edit_recipe.html', context)


# This function allows recipes to be deleted


def delete_recipe(request, recipe_id):
    set = get_object_or_404(CreateRecipe, id=recipe_id)
    set.delete()
    return redirect('/view_your_recipes/')
