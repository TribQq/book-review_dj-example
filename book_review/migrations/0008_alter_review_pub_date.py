# Generated by Django 3.2.5 on 2021-07-21 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_review', '0007_rename_pub_time_review_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateField(auto_now=True, default='2021-06-01'),
            preserve_default=False,
        ),
    ]
