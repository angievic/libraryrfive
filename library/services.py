
from library.models import Book,Author, Category
from library.serializers import BookSerializer
import requests

def extract_and_create_book_data(item):
    volume_info = item.get('volumeInfo', {})
    title = volume_info.get('title')
    if title:
        author_google = volume_info.get('authors', [])
        categories_google = volume_info.get('categories', [])
        existing_book = Book.objects.filter(title=title).first()
        if not existing_book:
            authors = []
            categories = []
            for a in author_google:
                author,_ = Author.objects.get_or_create(name=a)
                authors.append(author.id)
            for c in categories_google:
                category,_ = Category.objects.get_or_create(name=c)
                categories.append(category.id)
            existing_book = Book(
                title=volume_info.get('title'),
                subtitle=volume_info.get('subtitle'),
                publication_date=volume_info.get('publishedDate'),
                editor = volume_info.get('publisher'),
                description = volume_info.get('description'),
                image = volume_info.get('thumbnail'),
                source = "google"
            )
            existing_book.save()
            if categories:
                existing_book.categories.set(categories)
            if authors:
                existing_book.authors.set(authors)
        return BookSerializer(existing_book,many=False).data
    return {}

def search_book_google_api(query):
    # API Books in google
    url = 'https://www.googleapis.com/books/v1/volumes'
    params = {'q': query}
    response = requests.get(url, params=params)
    results = []
    if response.status_code == 200:
        data = response.json()
        items = data.get('items', [])
        for item in items:
            results.append({'source': 'google', 'book': extract_and_create_book_data(item)})
    return results



def extract_and_create_book_data_open_library(item):
    volume_info = item
    title = volume_info.get('title')
    if title:
        author_openapi = volume_info.get('author_name', [])
        existing_book = Book.objects.filter(title=title).first()
        if not existing_book:
            authors = []
            for a in author_openapi:
                author,_ = Author.objects.get_or_create(name=a)
                authors.append(author.id)
            existing_book = Book(
                title=volume_info.get('title'),
                publication_date=volume_info.get('first_publish_year'),
                image = get_cover_url(item),
                source = "open-library"
            )
            existing_book.save()
            existing_book.authors.set(authors)
        return BookSerializer(existing_book,many=False).data
    return {}


def search_books_open_library(query):
    url = 'https://openlibrary.org/search.json'
    params = {'q': query}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        items = data.get('docs', [])
        results = []
        results = [{'source': 'open-library', 'book': extract_and_create_book_data_open_library(item)} for item in items]
        return results

    return []


def get_cover_url(doc):
    cover_data = doc.get('cover_i')
    if cover_data:
        return f"https://covers.openlibrary.org/b/id/{cover_data}-L.jpg"

    return ''