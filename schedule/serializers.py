from rest_framework import serializers

from .models import Gym, ScheduledEvent, Training, TrainingSchedule, TrainingType


class TrainingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingType
        fields = "__all__"

    def validate_title(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Название не может быть пустым.")
        return value


class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = "__all__"

    def validate_training_content(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Описание тренировки не может быть пустым.")
        return value

    def validate_subscriptions_type(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Тип подписки не может быть пустым.")
        return value

    def validate(self, attrs):
        start_time = attrs.get("start_time") or getattr(self.instance, "start_time", None)
        end_time = attrs.get("end_time") or getattr(self.instance, "end_time", None)
        if start_time and end_time and end_time <= start_time:
            raise serializers.ValidationError({"end_time": "Время окончания должно быть позже времени начала."})
        return attrs


class TrainingScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingSchedule
        fields = "__all__"

    def validate_training_data(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Данные тренировки не могут быть пустыми.")
        return value

    def validate_workout_list(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Список упражнений не может быть пустым.")
        return value

    def validate(self, attrs):
        start_time = attrs.get("start_time") or getattr(self.instance, "start_time", None)
        end_time = attrs.get("end_time") or getattr(self.instance, "end_time", None)
        training = attrs.get("training") or getattr(self.instance, "training", None)
        free_seats = attrs.get("free_seats")
        if free_seats is None and self.instance is not None:
            free_seats = self.instance.free_seats
        if start_time and end_time and end_time <= start_time:
            raise serializers.ValidationError({"end_time": "Время окончания должно быть позже времени начала."})
        if training and free_seats is not None and free_seats > training.max_capacity:
            raise serializers.ValidationError({"free_seats": "Количество свободных мест не может превышать вместимость тренировки."})
        return attrs


class TrainingWorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingSchedule
        fields = ["workout_list"]


class TrainingWorkoutDetailUpdateDelete(serializers.ModelSerializer):
    class Meta:
        model = TrainingSchedule
        fields = ["workout_list"]


class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = "__all__"

    def validate_title(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Название не может быть пустым.")
        return value

    def validate_equipment(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Оборудование не может быть пустым.")
        return value


class ScheduledEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduledEvent
        fields = "__all__"

    def validate(self, attrs):
        training_schedule = attrs.get("training_schedule") or getattr(self.instance, "training_schedule", None)
        training = attrs.get("training") or getattr(self.instance, "training", None)
        gym = attrs.get("gym") or getattr(self.instance, "gym", None)
        free_seats = attrs.get("free_seats")
        if free_seats is None and self.instance is not None:
            free_seats = self.instance.free_seats
        if training_schedule and training and training_schedule.training_id != training.id:
            raise serializers.ValidationError(
                {"training": "Выбранная тренировка должна соответствовать расписанию тренировки."}
            )
        if gym and free_seats is not None and free_seats > gym.capacity:
            raise serializers.ValidationError({"free_seats": "Количество свободных мест не может превышать вместимость зала."})
        if training and free_seats is not None and free_seats > training.max_capacity:
            raise serializers.ValidationError({"free_seats": "Количество свободных мест не может превышать вместимость тренировки."})
        return attrs
