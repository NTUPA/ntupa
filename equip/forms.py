from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms.utils import flatatt
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape, format_html, html_safe
from django.utils.encoding import force_text
from django.utils.datastructures import MultiValueDict
from django.contrib.auth.models import User

import json

from .models import Event, Equipment, Category

class EquipmentSelect(forms.Widget):
    def __init__(self, attrs=None):
        super(EquipmentSelect, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''

        final_attrs = self.build_attrs(attrs, name=name, multiple='multiple', size='10')

        output = [format_html('<select{}>', flatatt(final_attrs))]
        output.append('</select>')

        ct_qs = Category.objects.all()
        ct_list = []
        for ct in ct_qs:
            ct_list.append(str(ct))

        eq_qs = Equipment.objects.all()
        eq_list = []
        for eq in eq_qs:
            eq_list.append({'id': eq.id, 'name': str(eq), 'belongs_to': eq.belongs_to, 'category': str(eq.category)})

        output.append('<script type="text/javascript">$(function(){ initEquipmentSelect(\'%s\', %s, %s, %s); });</script>' % (attrs['id'], json.dumps(ct_list), json.dumps(eq_list), json.dumps(value)))

        return mark_safe('\n'.join(output))

    def value_from_datadict(self, data, files, name):
        if isinstance(data, MultiValueDict):
            return data.getlist(name)
        return data.get(name)

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'location', 'client', 'start_date', 'end_date', 'manager', 'assistant', 'stages', 'equipments', 'note',)

    class Media:
        css = { 'all': ('https://code.jquery.com/ui/1.11.4/themes/dark-hive/jquery-ui.css', '/static/m2m_widget.css',) }
        js = ('https://code.jquery.com/jquery-3.0.0.min.js', 'https://code.jquery.com/ui/1.11.4/jquery-ui.min.js', '/static/m2m_widget.js' )

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['equipments'].widget = EquipmentSelect()
        self.fields['manager'].label_from_instance = lambda obj: '%s%s' % (obj.last_name, obj.first_name)
        self.fields['assistant'].label_from_instance = lambda obj: '%s%s' % (obj.last_name, obj.first_name)
        self.fields['stages'].label_from_instance = lambda obj: '%s%s' % (obj.last_name, obj.first_name)
