from django.urls import path
from .views import EventView, UserView, CreateRoomView

# Create your tests here.
urlPatterns = [
    path('event', EventView.as_view()),
    path('users', UserView.as_view()),
    path('create-room', CreateRoomView.as_view())
]