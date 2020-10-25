from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import EventForm
from .models import Event


# Create your views here.


def events(request):
    all_events = Event.objects.all().order_by('-created_at')
    return render(request, 'events/all_events.html', {
        'all_events': all_events,
        'all_events_active': True
    })


def events_by_category(request, event_category):
    events_in_category = Event.objects.filter(category=event_category).order_by('-created_at')
    return render(request, 'events/events_by_category.html', {
        'events_in_category': events_in_category,
        'category': event_category,
    })


def new_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_title = event_form.cleaned_data['title']
            event_form.save()
            messages.success(request, f'{event_title} is created.')
            return redirect('events:feed')
    else:
        event_form = EventForm()
    return render(request, 'events/new_event.html', {'event_form': event_form})


def event_detail(request, event_category, event_slug):
    event = Event.objects.get(slug=event_slug, category=event_category)
    return render(request, 'events/event_detail.html', {'event': event})


def edit_event(request, event_category, event_slug):
    event = Event.objects.get(slug=event_slug, category=event_category)
    event_form = EventForm(initial={
        'title': event.title,
        'description': event.description,
        'category': event.category,
        'appointment_date': event.appointment_date,
        'image_url': event.image_url
    })
    if request.method == 'POST':
        event_form = EventForm(request.POST, instance=event)
        if event_form.is_valid():
            event_title = event_form.cleaned_data['title']
            event_form.save()
            messages.info(request, f'{event_title} was updated.')
            return redirect('events:feed')
    return render(request, 'events/edit_event.html', {
        'event_form': event_form,
        'event': event,
        'is_edit_mode': True
    })


def delete_event(request, event_category, event_slug):
    event = Event.objects.get(slug=event_slug, category=event_category)
    event.delete()
    messages.warning(request, f'{event.title} is deleted.')
    return redirect('events:feed')
