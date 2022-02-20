from django.conf import settings
from django.db import models

from book.models import Book


class Like(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='likes',
    )
    book = models.ForeignKey(
        to=Book,
        on_delete=models.CASCADE,
        related_name='likes',
    )
    # register_date = models.DateTimeField()

    class Meta:
        unique_together = ('user', 'book')

    # def __str__(self):
    #     return str(self.register_date)
