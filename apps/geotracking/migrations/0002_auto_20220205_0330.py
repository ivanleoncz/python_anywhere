# Generated by Django 2.2.25 on 2022-02-05 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geotracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visitors',
            options={'verbose_name': 'Visitors', 'verbose_name_plural': 'Visitors'},
        ),
        migrations.AlterField(
            model_name='visitors',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]