# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Event

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['status', 'event_name', 'host_id', 'datetime', 'user_rating']

class CreateRoomSerializer(serializers.ModelSerializer):
       class Meta:
        model = Event
        fields = ['status', 'event_name', 'hostId', 'datetime', 'user_rating']
