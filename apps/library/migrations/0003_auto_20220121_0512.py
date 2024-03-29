# Generated by Django 2.2.25 on 2022-01-21 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20220119_0329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='isbn',
        ),
        migrations.AddField(
            model_name='book',
            name='isbn_10',
            field=models.CharField(blank=True, help_text='<a href="https://www.isbn-international.org/content/what-isbn">ISBN</a>', max_length=13, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='book',
            name='isbn_13',
            field=models.CharField(blank=True, help_text='<a href="https://www.isbn-international.org/content/what-isbn">ISBN</a>', max_length=13, null=True, unique=True),
        ),
    ]
