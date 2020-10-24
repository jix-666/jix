from django.shortcuts import render


def index(request):
    return render(request, 'jix/index.html', {'is_event_index': True})
