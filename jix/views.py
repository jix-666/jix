from django.shortcuts import render


def index(request):
    """Render index page of Jix."""
    return render(request, 'jix/index.html', {'is_event_index': True})
