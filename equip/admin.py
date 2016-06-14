from django.contrib import admin

from .models import Category, Location, Equipment

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Equipment)