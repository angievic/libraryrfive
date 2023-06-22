from library.services import search_book_google_api, search_books_open_library
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from library.models import Book
from library.serializers import BookSerializer
from rest_framework import viewsets, permissions
from django.db.models import Q

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.
    """
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.AllowAny]



@csrf_exempt
def search_book(request):
    if request.method == 'GET':
        results = []
        query = request.GET.get('query')
        type = request.GET.get('type')

        # Search intern db
        if type == "title":
            books = Book.objects.filter(Q(title__icontains=query))
        if type == "subtitle":
            books = Book.objects.filter(Q(subtitle__icontains=query))
        if type == "authors":
            books = Book.objects.filter(Q(authors__name=query))
        if type == "description":
            books = Book.objects.filter(Q(description__icontains=query))
        if type == "editor":
            books = Book.objects.filter(Q(editor__icontains=query))
        if len(books)>0:
            # Return book data
            results = {'source': 'db interna', 'book': BookSerializer(books,many=True).data if books else {}}
        else:
            # try in google api
            results = search_book_google_api(query)
            #try in another source
            if len(results) == 0:
                results = search_books_open_library(query)

        return JsonResponse({'results': results}, safe=False)

    return JsonResponse({'error': 'Invalid request method'})
           

