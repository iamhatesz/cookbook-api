from django.contrib import admin

# Register your models here.
from heroku_rest_api.api.models import Item

admin.site.register(Item)
