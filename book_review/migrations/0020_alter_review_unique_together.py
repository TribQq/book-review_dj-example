# Generated by Django 3.2.5 on 2021-07-23 17:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_review', '0019_remove_book_reviewed_by'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('book', 'owner')},
        ),
    ]
