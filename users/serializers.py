from rest_framework import serializers
from .models import Trainer, Admin, Client


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['full_name', 'photo', 'trainer_id', 'specialization', 'experience', 'rating']


class TrainerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['trainer_data', 'training']


class AdminSerializer(serializers.ModelSerializer):
    trainer = TrainerSerializer(many=True)


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
        field = ['updated_subscription']


class AdminVisitHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        field = ['client', 'training', 'check_in_time', 'subscriptions']


class ClientSerializer(serializers.ModelSerializer):
    trainer = TrainerSerializer(many=True)
    admin = AdminSerializer(many=True)


    class Meta:
        model = Client
        fields = ['name']