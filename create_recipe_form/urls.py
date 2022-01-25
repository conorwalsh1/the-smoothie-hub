from . import views
from django.urls import path


urlpatterns = [
    path('create/', views.create_recipe_form, name='create_recipe_form'),
    path(
        'view_your_recipes/',
        views.view_your_recipes,
        name='view_your_recipes'
        ),
    path('edit_recipe/', views.edit_recipe, name='edit_recipe'),
    path('delete_recipe/', views.delete_recipe, name='delete_recipe'),
]
