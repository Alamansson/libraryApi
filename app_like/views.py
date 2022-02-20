from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from app_like.models import Like
from app_like.serializers import LikeSerializer
from account.permissions import IsAuthorPermission


class LikeView(GenericAPIView):

    serializer_class = LikeSerializer
    permission_classes = [IsAuthorPermission]

    def post(self, request):
        srz_data = self.serializer_class(data=request.data)
        if srz_data.is_valid(raise_exception=True):
            book_id = srz_data.validated_data['book_id']
            try:
                Like.objects.get_or_create(book_id=book_id, user=request.user)
                return Response({"Вы поставили ЛАЙК"}, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({'Произошла ошибка'}, status=status.HTTP_200_OK)


class DislikeView(GenericAPIView):

    serializer_class = LikeSerializer
    permission_classes = [IsAuthorPermission]

    def post(self, request):
        srz_data = self.serializer_class(data=request.data)
        if srz_data.is_valid(raise_exception=True):
            book_id = srz_data.validated_data['book_id']
            try:
                Like.objects.get(book_id=book_id, user=request.user).delete()
                return Response({"Вы удалили ЛАЙК"}, status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({'Произошла ошибка'}, status=status.HTTP_200_OK)