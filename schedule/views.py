from django.shortcuts import render
from rest_framework import generics
from .models import Training, ScheduledEvent, TrainingType, Gym, TrainingSchedule
from .serializers import TrainingSerializer, ScheduledEventSerializer, TrainingTypeSerializer, TrainingScheduleSerializer, \
    GymSerializer, TrainingWorkoutSerializer, TrainingWorkoutDetailUpdateDelete


class TrainingView(generics.ListAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer


class ScheduledEventView(generics.ListAPIView):
    queryset = ScheduledEvent.objects.all()
    serializer_class = ScheduledEventSerializer


class TrainingTypeView(generics.ListAPIView):
    queryset = TrainingType.objects.all()
    serializer_class = TrainingTypeSerializer


class ScheduleView(generics.ListAPIView):
    queryset = TrainingSchedule.objects.all()
    serializer_class = TrainingScheduleSerializer


class WorkoutListCreateView(generics.ListCreateAPIView):
    queryset = TrainingSchedule.objects.all()
    serializer_class = TrainingWorkoutSerializer


class WorkoutDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrainingSchedule.objects.all()
    serializer_class = TrainingWorkoutDetailUpdateDelete


class RoomListView(generics.ListAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer