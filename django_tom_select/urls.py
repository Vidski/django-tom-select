"""
Django-Tom-Select URL configuration.

Add `django_tom_select` to your ``urlconf`` **if** you use any 'Model' fields::

    from django.urls import path


    path('tomselect/', include('django_tom_select.urls')),

"""
from django.urls import path

from .views import AutoResponseView

app_name = "django_tom_select"

urlpatterns = [
    path("fields/auto.json", AutoResponseView.as_view(), name="auto-json"),
]
