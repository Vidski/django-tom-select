"""
This is a Django_ integration of Tom-Select_.

The application includes Tom-Select driven Django Widgets and Form Fields.

.. _Django: https://www.djangoproject.com/
.. _Tom-Select: https://tom-select.js.org/

"""
from django import get_version

from . import _version

__version__ = _version.version
VERSION = _version.version_tuple

if get_version() < "3.2":
    default_app_config = "django_tom_select.apps.TomSelectAppConfig"
