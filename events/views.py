from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from report.forms import ReportForm
from report.models import Report
from .forms import EventForm
from .models import Event, Attendee


# Create your views here.


def events(request):
    """Display all event in the system according to created date.

    Returns:
    HttpResponseObject -- all events page

    """
    all_events = Event.objects.all().order_by('-created_at')
    return render(request, 'events/all_events.html', {
        'all_events': all_events,
        'all_events_active': True
    })


def events_by_category(request, event_category):
    """Display all event in the system by category according to created date.

    Returns:
    HttpResponseObject -- event by category page

    """
    events_in_category = Event.objects.filter(category=event_category).order_by('-created_at')
    return render(request, 'events/events_by_category.html', {
        'events_in_category': events_in_category,
        'category': event_category,
    })


@login_required(login_url='/accounts/login')
def new_event(request):
    """Create a new event.

    Returns:
    HttpResponseObject -- new event page

    """
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            event_title = event_form.cleaned_data['title']
            event = event_form.save()
            event.user = request.user
            event.save()
            messages.success(request, f'{event_title} is created.')
            return redirect('events:feed')
    else:
        event_form = EventForm()
    return render(request, 'events/new_event.html', {'event_form': event_form})


def event_detail(request, event_category, event_slug):
    """Display all detail of specific events.

    Returns:
    HttpResponseObject -- event detail page

    """
    event = Event.objects.get(slug=event_slug, category=event_category)
    if request.user.is_authenticated:
        try:
            joined = event.attendee_set.get(user=request.user)
        except (KeyError, Attendee.DoesNotExist):
            return render(request, 'events/event_detail.html', {'event': event})
        return render(request, 'events/event_detail.html', {'event': event, 'joined': joined})
    else:
        return render(request, 'events/event_detail.html', {'event': event})


@login_required(login_url='/accounts/login')
def edit_event(request, event_category, event_slug):
    """Edit specific event.

    Returns:
    HttpResponseObject -- edit event page

    """
    event = Event.objects.get(slug=event_slug, category=event_category)
    if event.user == request.user and request.user.is_authenticated:
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
                if event.user == request.user and request.user.is_authenticated:
                    event_title = event_form.cleaned_data['title']
                    event_form.save()
                    messages.info(request, f'{event_title} was updated.')
                else:
                    messages.warning(request, f'You can not edit {event.title}.')
                return redirect('events:feed')
    else:
        messages.warning(request, f'You can not edit {event.title}.')
        return redirect('events:feed')
    return render(request, 'events/edit_event.html', {
        'event_form': event_form,
        'event': event,
        'is_edit_mode': True
    })


@login_required(login_url='/accounts/login')
def delete_event(request, event_category, event_slug):
    """Delete specific event.

    Redirect:
    redirect to event feed page

    """
    event = Event.objects.get(slug=event_slug, category=event_category)
    if event.user == request.user and request.user.is_authenticated:
        event.delete()
        messages.warning(request, f'{event.title} is deleted.')
    else:
        messages.warning(request, f'You can not delete {event.title}.')
    return redirect('events:feed')


@login_required(login_url='/accounts/login')
def report_event(request, event_category, event_slug):
    """Report specific event.

    Returns:
    HttpResponseObject -- report event page

    """
    event = Event.objects.get(slug=event_slug, category=event_category)
    if request.method == 'POST':
        report_form = ReportForm(request.POST)
        if report_form.is_valid():
            report = Report(
                event=event,
                report_type=request.POST['report_type'],
                detail=request.POST['detail']
            )
            report.save()
            messages.warning(request, f'{event.title} is reported.')
            return redirect('events:feed')
    else:
        report_form = ReportForm()
    return render(request, 'events/report_event.html', {'report_form': report_form, 'event': event})


@login_required(login_url='/accounts/login')
def joining_event(request, event_category, event_slug):
    """

    Returns:
    HttpResponseObject -- event detail page that has join
    """
    event = get_object_or_404(Event, category=event_category, slug=event_slug)
    if event.attendee_set.filter(user=request.user).exists():
        messages.warning(request, f'You have already joined {event.title}.')
        return redirect('events:feed')
    event.attendee_set.create(user=request.user)
    messages.success(request, f'You have join {event.title}.')
    return redirect('events:feed')
