import uuid
from django.db import models


class Call(models.Model):
    def __str__(self):
        return self.call_id

    def is_recent(self):
        return self.audit_datetime >= timezone.now() - datetime.timedelta(days=1)
    is_recent.admin_order_field = 'is_recent'
    is_recent.boolean = True
    is_recent.short_description = 'Is recent?'
    call_url = models.CharField(max_length=200)
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    audit_datetime = models.DateTimeField("Date Audited")


class Analysis(models.Model):
    def __str__(self):
        return self.prompt_response
    call_id = models.ForeignKey(Call, on_delete=models.CASCADE)
    prompt_response = models.CharField(max_length=200)
   
class PromptConfig(models.Model):
    prompt_id = models.UUIDField( 
         default = uuid.uuid1, 
         editable = False) 
    prompt_name = models.CharField(max_length = 100)
    prompt = models.CharField(max_length = 2000)

class CallTypeConfig(models.Model):
    call_config_id = models.UUIDField(  
         default = uuid.uuid1, 
         editable = False)
    call_type = models.CharField(max_length = 100)