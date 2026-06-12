from rest_framework import generics
from .models import Training, ScheduledEvent, TrainingType, Gym, TrainingSchedule
from .serializers import TrainingSerializer, ScheduledEventSerializer, TrainingTypeSerializer, TrainingScheduleSerializer, \
    GymSerializer, TrainingWorkoutSerializer, TrainingWorkoutDetailUpdateDelete


class TrainingView(generics.ListCreateAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer


class ScheduledEventView(generics.ListCreateAPIView):
    queryset = ScheduledEvent.objects.all()
    serializer_class = ScheduledEventSerializer


class TrainingTypeView(generics.ListCreateAPIView):
    queryset = TrainingType.objects.all()
    serializer_class = TrainingTypeSerializer


class ScheduleView(generics.ListCreateAPIView):
    queryset = TrainingSchedule.objects.all()
    serializer_class = TrainingScheduleSerializer


class WorkoutListCreateView(generics.ListCreateAPIView):
    queryset = TrainingSchedule.objects.all()
    serializer_class = TrainingWorkoutSerializer


class WorkoutDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrainingSchedule.objects.all()
    serializer_class = TrainingWorkoutDetailUpdateDelete
    lookup_field = "id"


class RoomListView(generics.ListCreateAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer


class TrainingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    lookup_field = "id"


class ScheduledEventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScheduledEvent.objects.all()
    serializer_class = ScheduledEventSerializer
    lookup_field = "id"


class TrainingTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrainingType.objects.all()
    serializer_class = TrainingTypeSerializer
    lookup_field = "id"


class ScheduleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrainingSchedule.objects.all()
    serializer_class = TrainingScheduleSerializer
    lookup_field = "id"


class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer
    lookup_field = "id"
