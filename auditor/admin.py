from django.contrib import admin
from .models import Call, Analysis, PromptConfig, CallTypeConfig

class CallAdmin(admin.ModelAdmin):
    list_display = ('call_url', 'id','audit_datetime')
    list_filter = ['audit_datetime']
    search_fields = ['call_url']

admin.site.register(Call, CallAdmin)
admin.site.register(Analysis)
admin.site.register(PromptConfig)
admin.site.register(CallTypeConfig)