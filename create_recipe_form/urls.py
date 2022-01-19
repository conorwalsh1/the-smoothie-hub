from . import views
from django.urls import path


urlpatterns = [
    path('', views.create_recipe_form, name='create_recipe_form'),
    path('', views.view_your_recipes, name='view_your_recipes'),
]
