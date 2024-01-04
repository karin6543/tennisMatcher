from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import uuid

class Event(models.Model):
    # Your event fields
    event_id = models.AutoField(primary_key=True, default = uuid.uuid4())
    host_id = models.UUIDField(unique = True, max_length = 50)
    event_name = models.CharField(max_length=255, default='New Event')
    status = models.CharField(max_length=255)
    user_rating = models.IntegerField()
    eventDatetime = models.DateTimeField(default = timezone.now)
    createdAt = models.DateTimeField()
  

    # Many-to-Many relationship with User
    attendees = models.ManyToManyField(User, related_name='events_attending')

    def __str__(self):
        return f"{self.event_id} - {self.status}"

# If you want to extend the User model
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Additional fields for user profile if needed

    def __str__(self):
        return self.user.username
    

