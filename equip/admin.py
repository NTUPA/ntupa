from django.contrib import admin

from .models import Category, Location, Equipment, Event

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Event)

class EquipmentTableAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'model', 'number', 'condition', 'belongs_to')
    list_editable = ('number', 'condition', 'belongs_to')

admin.site.register(Equipment, EquipmentTableAdmin)