# Generated by Django 3.2.7 on 2022-02-20 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_delete_bookfavourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
