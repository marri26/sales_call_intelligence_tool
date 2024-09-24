from django.db import models


class Call(models.Model):
    def __str__(self):
        return self.call_id

    call_url = models.CharField(max_length=200)
    call_id = models.CharField(max_length=200)
    audit_datetime = models.DateTimeField("date published")


class Analysis(models.Model):
    def __str__(self):
        return self.prompt_response
    call_id = models.ForeignKey(Call, on_delete=models.CASCADE)
    prompt_response = models.CharField(max_length=200)
   
