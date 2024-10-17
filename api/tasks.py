from __future__ import absolute_import, unicode_literals
from django.core.cache import caches
from celery import shared_task
from django.conf import settings


@shared_task
def invalidate_book_cache(book_id):
    first_cache_layer = getattr(settings, 'FIRST_CACHING_LAYER', None)
    second_cache_layer = getattr(settings, 'SECOND_CACHING_LAYER', None)
    cache_timeout = getattr(settings, 'CACHE_TIMEOUT', {})

    if not first_cache_layer or not second_cache_layer:
        raise ValueError("Caching layers are not defined in the settings.")

    cache_key = f'book_{book_id}'
    first_cache = caches[first_cache_layer]
    second_cache = caches[second_cache_layer]

    first_cache.delete(cache_key)
    second_cache.delete(cache_key)