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
    image = models.ImageField(upload_to='media')
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









