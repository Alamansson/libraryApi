# Generated by Django 3.2.7 on 2022-02-21 22:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0007_delete_bookreviewrating'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookReviewRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='book.book', verbose_name='Книги')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Имя пользователя')),
            ],
        ),
    ]
