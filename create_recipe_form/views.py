from django.shortcuts import render

# Create your views here.

def create_recipe_form(request):

    return render(request, "create_recipe_form.html")
