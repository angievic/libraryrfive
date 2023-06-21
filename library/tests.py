from django.test import TestCase
from library.services import extract_and_create_book_data, search_book_google_api


class BookAPITestCase(TestCase):
    def setUp(self):
        #no initial data needed for this test
        pass
    
    def test_extract_and_create_book_data(self):
        item = {
            'volumeInfo': {
                'title': 'Test Book',
                'authors': ['Test Author'],
                'categories': ['Test Category'],
                'subtitle': 'Test Subtitle',
                'publishedDate': '2022-01-01',
                'publisher': 'Test Publisher',
                'description': 'Test Description',
                'thumbnail': 'http://example.com/image.jpg'
            }
        }

        # Perform the function call
        book = extract_and_create_book_data(item)
        # Check if the book is created in the database
        self.assertEqual(book['title'], 'Test Book')
        self.assertEqual(book['publication_date'], '2022-01-01')

    def test_search_book_google_api(self):

        query = 'test query'
        # Perform the function call
        results = search_book_google_api(query)

        # Check if the results are as expected
        self.assertEqual(results[0]['source'], 'google')
        self.assertIsNotNone(results[0]['book'])
