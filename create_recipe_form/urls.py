from . import views
from django.urls import path


urlpatterns = [
    path('create/', views.create_recipe_form, name='create_recipe_form'),
    path('view_your_recipes/', views.view_your_recipes, name='view_your_recipes'),
]
