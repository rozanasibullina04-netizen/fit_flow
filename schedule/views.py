from django.shortcuts import render
from rest_framework import generics
from .models import ScheduledEvent, Gym, TrainingSchedule
from .serializers import ScheduledEventSerializer, RoomListSerializer, TrainingWorkoutSerializer, TrainingWorkoutDetailUpdateDelete

# Create your views here.

class ScheduleView(generics.ListAPIView):
    queryset = ScheduledEvent.objects.all()
    serializer_class = ScheduledEventSerializer


class WorkoutListCreateView(generics.ListCreateAPIView):
    queryset = TrainingSchedule.objects.all()
    serializer_class = TrainingWorkoutSerializer


class WorkoutDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrainingSchedule.objects.all()
    serializer_class = TrainingWorkoutDetailUpdateDelete


class RoomListView(generics.ListAPIView):
    queryset = Gym.objects.all()
    serializer_class = RoomListSerializer