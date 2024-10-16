import requests
from django.core.cache import  caches
from django.conf import settings

cache_timeout = getattr(settings, 'CACHE_TIMEOUT')

def get_book_cached(book_id):
    first_cache = caches[settings.FIRST_CACHING_LAYER]
    cache_key = f'book_{book_id}'
    cached_data = first_cache.get(cache_key)

    if cached_data:
        return cached_data


    seccond_cache = caches[settings.SECOND_CACHING_LAYER]
    cached_data = seccond_cache.get(cache_key)

    if cached_data:
        first_cache.set(cache_key, cached_data, timeout=cache_timeout.get(settings.FIRST_CACHING_LAYER))
    return None

def fetch_book_data(book_id):
        url = f'https://get.taaghche.com/v2/book/{book_id}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }


        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            return None

def cache_book_data(book_id, data):

    cache_key = f'book_{book_id}'

    first_cache = caches[settings.FIRST_CACHING_LAYER]
    seccond_cache = caches[settings.SECOND_CACHING_LAYER]

    first_cache.set(cache_key, data, timeout=cache_timeout.get(settings.FIRST_CACHING_LAYER))

    seccond_cache.set(cache_key, data, timeout=cache_timeout.get(settings.SECOND_CACHING_LAYER))
