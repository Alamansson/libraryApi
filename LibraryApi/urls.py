
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('account.urls')),
    path('api/v1/', include('book.urls')),
    path('api/v1/', include('app_like.urls', namespace='likes')),
    path('api/v1/', include('app_favourite.urls', namespace='favourite')),

]
