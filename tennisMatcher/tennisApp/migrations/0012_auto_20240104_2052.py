# Generated by Django 3.2.23 on 2024-01-04 20:52

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tennisApp', '0011_auto_20240103_0353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='datetime',
            new_name='createdAt',
        ),
        migrations.AddField(
            model_name='event',
            name='eventDatetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_id',
            field=models.AutoField(default=uuid.UUID('ef208a03-7c3e-456b-934a-015437b42dd1'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='host_id',
            field=models.UUIDField(unique=True),
        ),
    ]
