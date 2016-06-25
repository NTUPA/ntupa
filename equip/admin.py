from django.contrib import admin

from .models import Category, Location, Equipment, Event

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Event)

class EquipmentTableAdmin(admin.ModelAdmin):
    list_display = ('model', 'category', 'manufacturer', 'number', 'condition', 'belongs_to', 'location', 'description')
    list_editable = ('number', 'condition', 'belongs_to', 'location')
    ordering = ('category', 'manufacturer', 'model', 'number', )

admin.site.register(Equipment, EquipmentTableAdmin)