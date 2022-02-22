from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer
from account.permissions import IsAuthorPermission, IsActive
from rest_framework.permissions import AllowAny


class PermissionMixin:
    def get_permissions(self):
        # print(self.action)
        if self.action == 'create':
            permissions = [IsActive]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthorPermission]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]


class BookView(PermissionMixin, ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]

    filterset_fields = ['category']
    search_fields = ['title', 'author']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, *args, **kwargs):
        instance = self.queryset.get(pk=kwargs.get('pk'))
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context






