from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("call_auditor", views.call_auditor, name="call_auditor"),
    path('success/', views.success_view, name='success'),
    path('failure/', views.failure_view, name='failure'),
]
