from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Report
from .forms import ReportForm


# Create your views here.
def report(request):
    all_reports = Report.objects.all().order_by('-reported_at')
    return render(request, 'report/all_report.html', {
        'all_reports': all_reports,
        'all_reports_active': True
    })


def report_by_category(request, type_of_report):
    reports_in_type = Report.objects.filter(report_type=type_of_report).order_by('-reported_at')
    return render(request, 'report/reports_by_category.html', {
        'reports_in_type': reports_in_type,
        'type': type_of_report,
    })


def new_report(request):
    if request.method == 'POST':
        report_form = ReportForm(request.POST)
        if report_form.is_valid():
            report_title = report_form.cleaned_data['title']
            report_form.save()
            messages.success(request, f'{report_title} is created.')
            return redirect('report:feed')
    else:
        report_form = ReportForm()
    return render(request, 'report/new_report.html', {'report_form': report_form})


def report_detail(request, type_of_report, report_slug):
    detail = Report.objects.get(slug=report_slug, report_type=type_of_report)
    return render(request, 'report/report_detail.html', {'report': detail})
