from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from .models import Event, User
from .serializers import EventSerializer, UserSerializer, CreateRoomSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class EventView(generics.CreateAPIView):
    def get(self, request, format = None):
        querySet = Event.objects.all()
        serializer_class = EventSerializer
        if querySet.exists():
            room = querySet[0]
            return Response(EventSerializer(room).data, status = status.HTTP_200_OK)
        return Response(status = status.HTTP_200_OK)

class UserView(generics.CreateAPIView):
    querySet = User.objects.all()
    serializer_class = UserSerializer

class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer
    def post(self, request, format = None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()

        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            host = self.request.session.session_key
            event_id = serializer.data.get('event_id')
            status = serializer.data.get('status')
            eventDateTime = serializer.data.get('eventDateTime')
            user_rating = serializer.data.get('user_rating')
            createdAt = serializer.data.get('createdAt')
            querySet = Event.objects.filter(event_id = event_id)
            if querySet.exists():
                room = querySet[0]
                room.status = status
                room.eventDateTime = eventDateTime
                room.user_rating = user_rating
                room.createdAt = createdAt
                room.save(update_fields=['event_id', 'status', 'eventDateTime', 'user_rating', 'createdAt'])
            else:
                room = Event(event_id = event_id, status = status, eventDateTime = eventDateTime, user_rating = user_rating, createdAt = createdAt, host_id = host)
                room.save()
            return Response(EventSerializer(room).data, status = status.HTTP_200)