"""
Shared memory across multiple machines to the heavy AJAX lookups.

Tom-Select uses django.core.cache_ to share fields across
multiple threads and even machines.

Tom-Select uses the cache backend defined in the setting
``TOM_SELECT_CACHE_BACKEND`` [default=``default``].

It is advised to always setup a separate cache server for Tom-Select.

.. _django.core.cache: https://docs.djangoproject.com/en/dev/topics/cache/
"""
from django.core.cache import caches

from .conf import settings

__all__ = ("cache",)

cache = caches[settings.TOM_SELECT_CACHE_BACKEND]
