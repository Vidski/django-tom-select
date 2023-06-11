"""Settings for Django-Tom-Select."""
from appconf import AppConf
from django.conf import settings  # NOQA

__all__ = ("settings", "TomSelectConf")


class TomSelectConf(AppConf):
    """Settings for django-tom-select."""

    CACHE_BACKEND = "default"
    """
    Django-Tom-Select uses Django's cache to sure a consistent state across multiple machines.

    Example of settings.py::

        CACHES = {
            "default": {
                "BACKEND": "django_redis.cache.RedisCache",
                "LOCATION": "redis://127.0.0.1:6379/1",
                "OPTIONS": {
                    "CLIENT_CLASS": "django_redis.client.DefaultClient",
                }
            },
            'tom-select': {
                "BACKEND": "django_redis.cache.RedisCache",
                "LOCATION": "redis://127.0.0.1:6379/2",
                "OPTIONS": {
                    "CLIENT_CLASS": "django_redis.client.DefaultClient",
                }
            }
        }

        # Set the cache backend to tom-select
        TOM_SELECT_CACHE_BACKEND = 'tom-select'

    .. tip:: To ensure a consistent state across all you machines you need to user
        a consistent external cache backend like Memcached, Redis or a database.

    .. note::
        Should you have copied the example configuration please make sure you
        have Redis setup. It's recommended to run a separate Redis server in a
        production environment.

    .. note:: The timeout of tom-select's caching backend determines
        how long a browser session can last.
        Once widget is dropped from the cache the json response view will return a 404.
    """
    CACHE_PREFIX = "tomselect_"
    """
    If you caching backend does not support multiple databases
    you can isolate tom-select using the cache prefix setting.
    It has set `tom-select_` as a default value, which you can change if needed.
    """
    JS = ["django_tom_select/tom-select.complete.min.js"]
    """
    The URI for the Tom-Select JS file. By default this points to version shipped with Django.

    If you want to select the version of the JS library used, or want to serve it from
    the local 'static' resources, add a line to your settings.py like so::

        TOM_SELECT_JS = ['assets/js/tom-select.min.js']

    If you provide your own JS and would not like Django-Tom-Select to load any, change
    this setting to a blank string like so::

        TOM_SELECT_JS = []

    .. tip:: Change this setting to a local asset in your development environment to
        develop without an Internet connection.
    """

    CSS = ["django_tom_select/tom-select.min.css"]
    """
    The URI for the Tom-Select CSS file. By default this points to version shipped with Django.

    If you want to select the version of the library used, or want to serve it from
    the local 'static' resources, add a line to your settings.py like so::

        TOM_SELECT_CSS = ['assets/css/tom-select.css']

    If you want to add more css (usually used in tom-select themes), add a line
    in settings.py like this::

        TOM_SELECT_CSS = [
            'assets/css/tom-select.css',
            'assets/css/tom-select-theme.css',
        ]

    If you provide your own CSS and would not like Django-Tom-Select to load any, change
    this setting to a blank string like so::

        TOM_SELECT_CSS = []

    .. tip:: Change this setting to a local asset in your development environment to
        develop without an Internet connection.
    """

    THEME = "default"
    """
    Tom-Select supports custom themes using the theme option so you can style Tom-Select
    to match the rest of your application.

    .. tip:: When using other themes, you may need use tom-select css and theme css.
    """

    JSON_ENCODER = "django.core.serializers.json.DjangoJSONEncoder"
    """
    A :class:`JSONEncoder<json.JSONEncoder>` used to generate the API response for the model widgets.

    A custom JSON encoder might be useful when your models uses
    a special primary key, that isn't serializable by the default encoder.
    """

    class Meta:
        """Prefix for all Django-Tom-Select settings."""

        prefix = "TOM_SELECT"
