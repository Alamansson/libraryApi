from django.urls import path

from app_review import views

app_name = 'reviews'

urlpatterns = [
    path('review/', views.BookReviewView.as_view(), name='review_product'),
]


