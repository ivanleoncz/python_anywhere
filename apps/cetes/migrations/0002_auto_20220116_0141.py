# Generated by Django 2.2.25 on 2022-01-16 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cetes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionmonth',
            name='date',
            field=models.DateField(unique=True),
        ),
        migrations.AlterField(
            model_name='auctionmonth',
            name='days',
            field=models.PositiveIntegerField(default=28),
        ),
        migrations.AlterField(
            model_name='auctionsemester',
            name='date',
            field=models.DateField(unique=True),
        ),
        migrations.AlterField(
            model_name='auctionsemester',
            name='days',
            field=models.PositiveIntegerField(default=182),
        ),
        migrations.AlterField(
            model_name='auctiontrimester',
            name='date',
            field=models.DateField(unique=True),
        ),
        migrations.AlterField(
            model_name='auctiontrimester',
            name='days',
            field=models.PositiveIntegerField(default=91),
        ),
        migrations.AlterField(
            model_name='auctionyear',
            name='date',
            field=models.DateField(unique=True),
        ),
        migrations.AlterField(
            model_name='auctionyear',
            name='days',
            field=models.PositiveIntegerField(default=364),
        ),
    ]
