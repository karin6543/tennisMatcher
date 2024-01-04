# Generated by Django 3.2.23 on 2023-12-27 20:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tennisApp', '0006_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='events_attending', to=settings.AUTH_USER_MODEL),
        ),
    ]