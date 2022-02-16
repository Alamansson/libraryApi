from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from .models import Book, BookLike, BookFavourite
from .serializers import BookSerializer, BookLikeSerializer, BookFavouriteSerializer
from account.permissions import IsAuthorPermission, IsActive
from rest_framework.permissions import AllowAny


class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsActive]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthorPermission]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]


class BookView(PermissionMixin, ModelViewSet):
    permission_classes = [IsAuthorPermission]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]

    filterset_fields = ['category']
    search_fields = ['title', 'author']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context


class BookLikeView(PermissionMixin, ModelViewSet):
    permission_classes = IsAuthorPermission
    queryset = BookLike.objects.all()
    serializer_class = BookLikeSerializer


class BookFavouriteView(PermissionMixin, ModelViewSet):
    permission_classes = IsAuthorPermission
    queryset = BookFavourite.objects.all()
    serializer_class = BookFavouriteSerializer








