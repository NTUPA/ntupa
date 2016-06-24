from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Equipment

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'equip/index.html'
    context_object_name = 'equipments'

    def get_queryset(self):
        return Equipment.objects.all()

class PrintView(LoginRequiredMixin, generic.ListView):
    template_name = 'equip/print.html'
    context_object_name = 'equipments'

    def get_queryset(self):
        return Equipment.objects.all()