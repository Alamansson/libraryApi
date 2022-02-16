from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookView, BookLikeView, BookFavouriteView


router = DefaultRouter()
router.register('book', BookView)
router.register('book_like', BookLikeView)
router.register('book_favourite', BookFavouriteView)

urlpatterns = [
    path('', include(router.urls))
]





