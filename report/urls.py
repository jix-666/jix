from django.urls import path
from . import views

app_name = 'report'
urlpatterns = [
    path('', views.report, name='feed'),
    path('new/', views.new_report, name='new'),
    path('<str:type_of_report>/', views.report_by_category, name='report_by_category'),
    path('<str:report_type>/<slug:report_slug>/', views.report_detail, name='report_detail'), ]
