# Generated by Django 3.2.23 on 2023-12-27 20:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tennisApp', '0007_event_attendees'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
