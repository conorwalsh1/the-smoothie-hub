from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import CreateRecipe

# Register your models here.


@admin.register(CreateRecipe)
class CreateRecipeAdmin(SummernoteModelAdmin):

    search_fields = ['ingredients', 'method']
    summernote_fields = ('ingredients', 'method')
