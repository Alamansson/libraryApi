from django.urls import path

from app_favourite import views

app_name = 'favourites'

urlpatterns = [
    path('favourite/', views.FavouriteView.as_view(), name='like_product'),
    path('favourite_delete/', views.FavouriteDeleteView.as_view(), name='dislike_product'),
]
