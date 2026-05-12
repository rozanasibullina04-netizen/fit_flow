from rest_framework import serializers
from .models import Trainer, Admin, Client


class TrainerSerializer(serializers.ModelSerializer):
    def validate_full_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Имя не может быть пустым")
        return value
    def validate_specialization(self, value):
        if not value.strip():
            raise serializers.ValidationError("Поле specialization не может быть пустым")
        return value
    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Оценка должна быть от 1 до 5")
        return value
    def validate_experience(self, value):
        if value < 1:
            raise serializers.ValidationError("Опыт должен быть больше 1 года")
        return value


    class Meta:
        model = Trainer
        fields = ['full_name', 'photo', 'trainer_id', 'specialization', 'experience', 'rating']


class TrainerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['trainer_data', 'training']


class AdminSerializer(serializers.ModelSerializer):
    trainer = TrainerSerializer(many=True)
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Имя не может быть пустым")
        return value


    class Meta:
        model = Admin
        fields = ['name']


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        field = ['user_list']


class AdminSubscriptionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        field = ['subscriptions']


class AdminSubscriptionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        field = ['subscription']


class ClientSerializer(serializers.ModelSerializer):
    trainer = TrainerSerializer(many=True)
    admin = AdminSerializer(many=True)
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Имя не может быть пустым")
        return value


    class Meta:
        model = Client
        fields = ['name']