from django.db import models
from django.conf import settings
from book.models import Book


class BookReview(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='review',
    )
    book = models.ForeignKey(
        to=Book,
        on_delete=models.CASCADE,
        related_name='review',
    )

    rating = models.PositiveSmallIntegerField(blank=True, null=True)

    review = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('user', 'book', 'rating', 'review')
