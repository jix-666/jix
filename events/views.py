from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def events(request):
    return HttpResponse('Events page')
