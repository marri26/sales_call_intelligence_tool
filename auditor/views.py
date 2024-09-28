from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AuditForm
from django.utils import timezone

def index(request):
    return HttpResponse("Auditor Page")

def call_auditor(request):
    if request.method == 'POST':
        form = AuditForm(request.POST)

        if form.is_valid():
            call = form.save(commit=False)
            call.audit_status = "SUCCESS"  # Set to SUCCESS if the form is valid
            call.call_datetime = timezone.now()
            call.save()
            return redirect('success')
        else:
            call = form.save(commit=False)
            call.audit_status = "FAILURE"  # Set to FAILURE if the form is invalid
            call.call_datetime = timezone.now()
            call.save()  # Optionally save it even if invalid (if it is appropriate for your use case)
            return render(request, 'failure.html', {'message': 'Call audit failed!', 'form': form})

    else:
        form = AuditForm()

    return render(request, 'call_auditor.html', {'form': form})

def success_view(request):
    return render(request, 'success.html', {'message': 'Call audit saved successfully!'})

def failure_view(request):
    return render(request, 'failure.html', {'message': 'Call audit failed!'})
