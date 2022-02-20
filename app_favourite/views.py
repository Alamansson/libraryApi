
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from app_favourite.models import Favourite
from app_favourite.serializers import FavouriteSerializer
from account.permissions import IsAuthorPermission


class FavouriteView(GenericAPIView):

    serializer_class = FavouriteSerializer
    permission_classes = [IsAuthorPermission]

    def post(self, request):
        srz_data = self.serializer_class(data=request.data)
        if srz_data.is_valid(raise_exception=True):
            book_id = srz_data.validated_data['book_id']
            try:
                Favourite.objects.get_or_create(book_id=book_id, user=request.user)
                return Response({"Вы включили в Избранное"}, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({'Произошла ошибка'}, status=status.HTTP_200_OK)


class FavouriteDeleteView(GenericAPIView):

    serializer_class = FavouriteSerializer
    permission_classes = [IsAuthorPermission]

    def post(self, request):
        srz_data = self.serializer_class(data=request.data)
        if srz_data.is_valid(raise_exception=True):
            book_id = srz_data.validated_data['book_id']
            try:
                Favourite.objects.get(book_id=book_id, user=request.user).delete()
                return Response({"Вы убрали с Избранное"}, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({'Произошла ошибка'}, status=status.HTTP_200_OK)
