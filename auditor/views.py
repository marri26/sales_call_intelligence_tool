from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request):
    return HttpResponse("Auditor Page")


def call_auditor(request):
    if request.method == 'POST':
        url = request.POST.get('call_auditor')
        
        if not url:
            return render(request, 'call_auditor.html', {'error_message': 'Please enter a valid URL'})
        

        
        return HttpResponse(f'Call audit initiated for: {url}')
    
    return render(request, 'call_auditor.html')
