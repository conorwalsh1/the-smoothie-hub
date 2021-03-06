"""thesmoothiehub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('home.urls')),
    path('create_recipe_form/', include('create_recipe_form.urls')),
    path('', include('create_recipe_form.urls')),
    path('edit_recipe/<recipe_id>/', include('create_recipe_form.urls')),
    path('delete_recipe/<recipe_id>/', include('create_recipe_form.urls')),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('featured_recipe/', include(
        'featured_recipe.urls'), name='featured_recipe_urls'),
    path('accounts/', include('allauth.urls')),
]
