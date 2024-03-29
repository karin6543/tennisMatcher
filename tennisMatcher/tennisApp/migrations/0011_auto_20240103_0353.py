# Generated by Django 3.2.23 on 2024-01-03 03:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tennisApp', '0010_auto_20231227_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_name',
            field=models.CharField(default='New Event', max_length=255),
        ),
        migrations.AddField(
            model_name='event',
            name='host_id',
            field=models.UUIDField(default=uuid.UUID('cab46477-941d-4877-97dc-79801dfcf598')),
        ),
    ]
