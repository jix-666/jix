from django.urls import path
from . import views


app_name = 'events'
urlpatterns = [
    path('', views.events, name='feed'),
    path('new/', views.new_event, name='new'),
    path('<str:event_category>/', views.events_by_category, name='events_by_category'),
    path('<str:event_category>/<slug:event_slug>/', views.event_detail, name='event_detail'),
    path('<str:event_category>/<slug:event_slug>/delete/', views.delete_event, name='delete_event'),
]