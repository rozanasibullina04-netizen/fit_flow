from rest_framework import serializers
from .models import Training, TrainingType, TrainingSchedule, Gym, ScheduledEvent


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'


class TrainingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingType
        fields = '__all__'


class TrainingScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingSchedule
        fields = ['training_date', 'start_time', 'end_time', 'trainer', 'workout_list', 'training', 'gym', 'free_seats']


class TrainingWorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingSchedule
        field = ['workout_list']


class TrainingWorkoutDetailUpdateDelete(serializers.ModelSerializer):
    class Meta:
        model = TrainingSchedule
        field = ['training_data']


class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = ['title', 'capacity', 'description']


class ScheduledEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledEvent
        fields = ['duration', 'free_seats']