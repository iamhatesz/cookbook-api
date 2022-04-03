from django.contrib import admin

from cookbook_api.api.models import Recipe, Tag


@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class AdminRecipe(admin.ModelAdmin):
    pass
