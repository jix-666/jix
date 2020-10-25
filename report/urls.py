from django.urls import path
from . import views

app_name = 'report'
urlpatterns = [
    path('', views.report, name='feed'),
    path('<str:type_of_report>/', views.report_by_category, name='report_by_category'),
    path('<str:type_of_report>/<int:report_id>/', views.delete_report, name='delete_report'),
]
