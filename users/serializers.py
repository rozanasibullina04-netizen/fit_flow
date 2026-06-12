from rest_framework import serializers

from .models import Admin, Client, Trainer


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"

    def validate_full_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("ФИО не может быть пустым.")
        if value.isdigit():
            raise serializers.ValidationError("ФИО не может состоять только из цифр.")
        return value

    def validate_specialization(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Специализация не может быть пустой.")
        return value


class TrainerDetailSerializer(TrainerSerializer):
    pass


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"

    def validate_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Имя не может быть пустым.")
        if value.isdigit():
            raise serializers.ValidationError("Имя не может состоять только из цифр.")
        return value


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ["user_list"]


class AdminSubscriptionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ["subscriptions"]


class AdminSubscriptionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ["subscriptions"]


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

    def validate_name(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Имя не может быть пустым.")
        if value.isdigit():
            raise serializers.ValidationError("Имя не может состоять только из цифр.")
        return value
