# Generated by Django 3.2.5 on 2021-08-04 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_review', '0040_book_small_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.PositiveIntegerField(default=500),
        ),
    ]
