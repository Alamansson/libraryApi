from django.db import models
from book.managers import ConfirmedProductManager


class Created(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Book(models.Model):
    BOOK_CATEGORY = [
        ('coding', 'Программирование'),
        ('medical', 'Медицина'),
        ('literature', 'Литература'),
    ]
    BOOK_INTENTION = [
        ('sell', 'Продажа'),
        ('exchange', 'Обмен'),
        ('seeking', 'Ищу'),
    ]

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=20, null=True, blank=True, choices=BOOK_CATEGORY)
    publisher = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='publisher')
    image = models.ImageField(upload_to='book')
    description = models.TextField(blank=True, null=True)
    stock = models.PositiveSmallIntegerField(default=0)
    status = models.CharField(max_length=10, choices=BOOK_INTENTION, default='sell')
    is_confirm = models.BooleanField(default=False)

    objects = models.Manager()

    confirmed = ConfirmedProductManager()


RATE_CHOICES = [
    (1, '1 - Trash'),
    (2, '2 - Horrible'),
    (3, '3 - Terrible'),
    (4, '4 - Bad'),
    (5, '5 - OK'),
    (6, '6 - Watchable'),
    (7, '7 - Good'),
    (8, '8 - Very Good'),
    (9, '9 - Perfect'),
    (10, '10 - Master Piece'),
]


class BookReviewRating(models.Model):
    user = models.ForeignKey(
        'account.User', verbose_name="Имя пользователя", on_delete=models.DO_NOTHING, blank=True)
    rating = models.PositiveSmallIntegerField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name="Книги",
        related_name="ratings"
    )

    def __str__(self):
        return f"{self.rating} - {self.book}"








