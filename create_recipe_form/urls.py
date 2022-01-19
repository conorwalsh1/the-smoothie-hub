from . import views
from django.urls import path


urlpatterns = [
    path('', views.create_recipe_form, name='create-recipe-form'),
]
