from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import EventForm
from .models import Event


# Create your views here.


def events(request):
    all_events = Event.objects.all()
    return render(request, 'events/all_events.html', {'all_events': all_events, 'all_events_active': True})


def events_by_category(request, event_category):
    events_in_category = Event.objects.filter(category=event_category)
    return render(
        request,
        'events/events_by_category.html',
        {
            'events_in_category': events_in_category,
            'category': event_category,
        }
    )


def new_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event = Event(title=request.POST['title'], description=request.POST['description'],
                          appointment_date=request.POST['appointment_date'],
                          image_url=request.POST['image_url'])
            event.save()
            messages.success(request, f'{event.title} is created.')
            return redirect('events:feed')
    else:
        event_form = EventForm()
    return render(request, 'events/new_event.html', {'event_form': event_form})


def event_detail(request, event_category, event_slug):
    event = Event.objects.get(slug=event_slug)
    return render(request, 'events/event_detail.html', {'event': event})
