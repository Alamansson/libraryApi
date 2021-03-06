# Generated by Django 3.2.7 on 2022-02-21 23:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0007_delete_bookreviewrating'),
        ('app_review', '0002_auto_20220221_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookreview',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookreview',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='bookreview',
            unique_together={('user', 'book', 'rating', 'review')},
        ),
    ]
