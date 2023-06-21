from library.views import BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'book', BookViewSet,basename='book')
urls_library= router.urls