from django.urls import path
from . import views


app_name = 'events'
urlpatterns = [
    path('', views.events, name='feed'),
    path('new/', views.new_event, name='new'),
    path('<str:category>/', views.events_by_category, name='events_by_category'),
]