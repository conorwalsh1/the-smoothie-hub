from django.contrib import admin
from .models import CreateRecipe
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(CreateRecipe)
class CreateRecipeAdmin(SummernoteModelAdmin):

    search_fields = ['ingredients', 'method']
    summernote_fields = ('ingredients', 'method')
