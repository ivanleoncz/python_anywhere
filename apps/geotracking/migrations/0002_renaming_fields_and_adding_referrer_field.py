# Generated by Django 2.2.25 on 2023-10-18 00:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('geotracking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitor',
            old_name='amount_of_requests',
            new_name='days_visited',
        ),
        migrations.RenameField(
            model_name='visitor',
            old_name='ip',
            new_name='ip_address',
        ),
        migrations.RenameField(
            model_name='visitor',
            old_name='last_request',
            new_name='updated',
        ),
        migrations.AddField(
            model_name='visitor',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visitor',
            name='device_id',
            field=models.CharField(default='dummy_id', help_text='Token generated upon request and stored as Persistent Cookie', max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visitor',
            name='referrer',
            field=models.CharField(blank=True, help_text='Page which served the link to the request.', max_length=256, null=True),
        ),
    ]
