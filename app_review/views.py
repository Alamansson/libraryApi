# from app_review.models import BookReviewRating
# from app_review.serializers import BookReviewRatingSerializer
from book.views import PermissionMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from .serializers import ReviewSerializer
from .models import BookReview
from rest_framework.response import Response
from rest_framework import status


class BookReviewView(GenericAPIView):

    serializer_class = ReviewSerializer

    def post(self, request):

        srz_data = self.serializer_class(data=request.data)
        if srz_data.is_valid(raise_exception=True):
            book_id = srz_data.validated_data['book_id']

            if bool(BookReview.objects.filter(book_id=book_id, user=request.user)):
                return Response({"Вы уже оставляли отзыв"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                try:
                    instance = BookReview.objects.last().rating
                    rating = (instance + int(request.data.get('rating'))) / 2

                except ValueError:
                    rating = request.data.get('rating')
                BookReview.objects.create(book_id=book_id, user=request.user,
                                       rating=rating,
                                       review=request.data.get('review'))
                return Response({"Вы оставили отзыв"}, status=status.HTTP_400_BAD_REQUEST)
