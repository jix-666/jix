from django.urls import path

from . import views

app_name = 'events'
urlpatterns = [
    path('', views.events, name='feed'),
    path('new/', views.new_event, name='new'),
    path('<str:event_category>/', views.events_by_category, name='events_by_category'),
    path('<str:event_category>/<str:event_slug>/', views.event_detail, name='event_detail'),
    path('<str:event_category>/<str:event_slug>/edit/', views.edit_event, name='edit_event'),
    path('<str:event_category>/<str:event_slug>/delete/', views.delete_event, name='delete_event'),
    path('<str:event_category>/<str:event_slug>/report/', views.report_event, name='report_event'),
    path('<str:event_category>/<str:event_slug>/join/', views.joining_event, name='joining_event'),
]
