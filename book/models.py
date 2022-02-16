from django.db import models
# from .account import User

class Created(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Book(Created):
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
    status = models.CharField(max_length=10, choices=BOOK_INTENTION, default='sell')


class BookLike(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='like')
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='like', null=True)

    def __str__(self):
         return f"Author {self.user}, book {self.book}"


class BookFavourite(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='favourite')
    user = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='favourite', null=True)









