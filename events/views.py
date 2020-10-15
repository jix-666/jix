from django.shortcuts import render
from django.http import HttpResponse
from .models import Event
from .forms import EventForm


# Create your views here.


def events(request):
    all_events = Event.objects.all()
    return render(request, 'events/all_events.html', {'all_events': all_events})


def events_by_category(request, category):
    events_in_category = Event.objects.filter(category=category)
    return render(
        request,
        'events/events_by_category.html',
        {
            'events_in_category': events_in_category,
            'category': category,
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
    else:
        event_form = EventForm()
    return render(request, 'events/new_event.html', {'event_form': event_form})
