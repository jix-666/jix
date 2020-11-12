from django.contrib import messages
from django.shortcuts import render, redirect

from .models import Report


# Create your views here.
def report(request):
    """Display all report in the system according to reported date.

    Returns:
    HttpResponseObject -- all report page

    """
    if not request.user.is_authenticated:
        return redirect('events:feed')
    elif request.user.is_superuser:
        all_reports = Report.objects.all().order_by('-reported_at')
        return render(request, 'report/all_report.html', {
            'reports': all_reports,
            'all_reports_active': True
        })
    else:
        messages.warning(request, 'Permission denied.')
        return redirect('events:feed')


def report_by_category(request, type_of_report):
    """Display all report in the system by category according to reported date.

    Returns:
    HttpResponseObject -- report by category page

    """
    if not request.user.is_authenticated:
        return redirect('events:feed')
    elif request.user.is_superuser:
        reports_in_type = Report.objects.filter(report_type=type_of_report).order_by('-reported_at')
        return render(request, 'report/reports_by_category.html', {
            'reports': reports_in_type,
            'type': type_of_report,
            'type_title': type_of_report.replace('-', ' '),
        })
    else:
        messages.warning(request, 'Permission denied.')
        return redirect('events:feed')


def delete_report(request, type_of_report, report_id):
    """Delete specific report.

    Redirect:
    redirect to report index page

    """
    if not request.user.is_authenticated:
        return redirect('events:feed')
    elif request.user.is_superuser:
        Report.objects.get(report_type=type_of_report, pk=report_id).delete()
        return redirect('report:feed')
    else:
        messages.warning(request, 'Permission denied.')
        return redirect('events:feed')
