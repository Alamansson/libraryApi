from django.db import models


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

    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=20, null=True, blank=True, choices=BOOK_CATEGORY)
    publisher = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='publisher')
    image = models.ImageField(upload_to='media')










