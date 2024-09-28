from django import forms
from .models import Call

class AuditForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = ['call_url']
        widgets = {
            'call_url': forms.URLInput(attrs={'placeholder': 'https://example.com/call'}),
            'call_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'audit_status': forms.HiddenInput()
        }
        