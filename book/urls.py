from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookView, BookReviewRatingViewSet


router = DefaultRouter()
router.register('book', BookView)
router.register('review', BookReviewRatingViewSet)

urlpatterns = [
    path('', include(router.urls))
]




