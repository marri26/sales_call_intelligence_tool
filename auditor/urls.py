from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("call_auditor", views.call_auditor, name="call_auditor"),
]
