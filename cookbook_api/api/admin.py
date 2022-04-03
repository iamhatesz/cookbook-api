from django.contrib import admin

# Register your models here.
from cookbook_api.api.models import Item

admin.site.register(Item)
