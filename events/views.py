from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

# Create your views here.


def events(request):
    all_events = Event.objects.all()
    return HttpResponse('Events page')


def events_by_category(request, category):
    events_by_category = Event.objects.filter(category=category)
    return HttpResponse('Event ' + category)
