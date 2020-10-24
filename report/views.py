from django.contrib import messages
from django.shortcuts import render, redirect

from events.models import Event
from .forms import ReportForm
from .models import Report


# Create your views here.


def report(request):
    all_reports = Report.objects.all().order_by('-reported_at')
    return render(request, 'report/all_report.html', {
        'reports': all_reports,
        'all_reports_active': True
    })


def report_by_category(request, type_of_report):
    reports_in_type = Report.objects.filter(report_type=type_of_report).order_by('-reported_at')
    return render(request, 'report/reports_by_category.html', {
        'reports': reports_in_type,
        'type': type_of_report,
        'type_title': type_of_report.replace('-', ' '),
    })


def new_report(request):
    if request.method == 'POST':
        report_form = ReportForm(request.POST)
        if report_form.is_valid():
            report_form.save()
            messages.success(request, f'Report of {Event.objects.get(pk=request.POST["event"]).title} is created.')
            return redirect('report:feed')
    else:
        report_form = ReportForm()
    return render(request, 'report/new_report.html', {'report_form': report_form})


def delete_report(request, type_of_report, report_id):
    Report.objects.get(report_type=type_of_report, pk=report_id).delete()
    return redirect('report:feed')
