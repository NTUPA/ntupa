from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Equipment, Event
from .forms import EventForm

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'equip/index.html'
    context_object_name = 'equipments'

    def get_queryset(self):
        return Equipment.objects.all()

class EventListView(LoginRequiredMixin, generic.ListView):
    template_name = 'equip/event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.all().order_by('start_date')

class EventPrintView(LoginRequiredMixin, generic.DetailView):
    template_name = 'equip/event_print.html'
    model = Event

class PrintView(LoginRequiredMixin, generic.ListView):
    template_name = 'equip/print.html'
    context_object_name = 'equipments'

    def get_queryset(self):
        return Equipment.objects.all()

@login_required()
def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return redirect('event')
    else:
        form = EventForm()
    return render(request, 'equip/event_create.html', {'form': form})

@login_required()
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save()
            return redirect('event')
    else:
        form = EventForm(instance=event)
    return render(request, 'equip/event_create.html', {'form': form})
