from django.http import JsonResponse, HttpResponse
from .services import cache_book_data, fetch_book_data, get_book_cached

def bookDetail(request, id):
    if request.method == 'GET':
        # Check the memory cache for data

        cache_data = get_book_cached(id)


        if cache_data:
            print('at cache')
            return JsonResponse(cache_data, safe=False)


        book_data = fetch_book_data(id)
        print('at fetch')

        if book_data:
            cache_book_data(id, book_data)
            return JsonResponse(book_data, safe=False)


        return JsonResponse({'error': 'Book not found'}, status=404)

def test(request):
    return HttpResponse("result.id")
