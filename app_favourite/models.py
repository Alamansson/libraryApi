from django.conf import settings
from django.db import models

from book.models import Book


class Favourite(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='favourite',
    )
    book = models.ForeignKey(
        to=Book,
        on_delete=models.CASCADE,
        related_name='favourite',
    )

    class Meta:
        unique_together = ('user', 'book')

