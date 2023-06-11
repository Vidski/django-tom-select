"""Django application configuration."""
from django.apps import AppConfig


class TomSelectAppConfig(AppConfig):
    """Django application configuration."""

    name = "django_tom_select"
    verbose_name = "tom-select"

    def ready(self):
        from . import conf  # noqa
