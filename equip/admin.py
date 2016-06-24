from django.contrib import admin

from .models import Category, Location, Equipment, Event

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Event)

class EquipmentTableAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'number', 'condition', 'belongs_to', 'location')
    list_editable = ('number', 'condition', 'belongs_to', 'location')

admin.site.register(Equipment, EquipmentTableAdmin)