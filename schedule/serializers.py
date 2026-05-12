from rest_framework import serializers
from .models import Training, TrainingType, TrainingSchedule, Gym, ScheduledEvent


class TrainingTypeSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Название не может быть пустым")
        return value
    def validate_duration(self, value):
        if value < 0:
            raise serializers.ValidationError("duration не должен быть отрицательным")
        return value


    class Meta:
        model = TrainingType
        fields = ['title', 'duration']


class TrainingSerializer(serializers.ModelSerializer):
    def validate_training_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("training content не должен быть пустым")
        return value
    def validate_subscriptions_type(self, value):
        if not value.strip():
            raise serializers.ValidationError("subscriptions type не должно быть пустым")
        return value
    def validate_max_capacity(self, value):
        if value < 0:
            raise serializers.ValidationError("max_capacity не должен быть отрицательным")
        return value


    class Meta:
        model = Training
        fields = ['training_content', 'subscriptions_type', 'start_time', 'end_time', 'max_capacity']


class TrainingScheduleSerializer(serializers.ModelSerializer):
    def validate_training_data(self, value):
        if not value.strip():
            raise serializers.ValidationError("training data не должен быть пустым")
        return value
    def validate_workout_list(self, value):
        if not value.strip():
            raise serializers.ValidationError("workout list не должен быть пустым")
        return value


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
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Название не может быть пустым")
        return value
    def validate_equipment(self, value):
        if not value.strip():
            raise serializers.ValidationError("equipment не должно быть пустым")
        return value
    def validate_capacity(self, value):
        if value < 0:
            raise serializers.ValidationError("capacity не должен быть отрицательным")
        return value


    class Meta:
        model = Gym
        fields = ['title', 'capacity', 'description']


class ScheduledEventSerializer(serializers.ModelSerializer):
    def validate_duration(self, value):
        if value < 0:
            raise serializers.ValidationError("duration не должен быть отрицательным")
        return value

    def validate_free_seats(self, value):
        if value < 1 or value > 20:
            raise serializers.ValidationError("количество мест должно быть от 1 до 20")
        return value


    class Meta:
        model = ScheduledEvent
        fields = ['duration', 'free_seats']