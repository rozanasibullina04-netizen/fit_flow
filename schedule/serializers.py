from rest_framework import serializers
from .models import Training, TrainingType, TrainingSchedule, Gym, ScheduledEvent


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = '__all__'


class TrainingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingType
        fields = ['title']


class TrainingScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingSchedule
        fields = '__all__'


class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = ['title']


class ScheduledEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledEvent
        fields = '__all__'