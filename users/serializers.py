from rest_framework import serializers
from .models import Trainer, Admin, Client


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['name']


class AdminSerializer(serializers.ModelSerializer):
    trainer = TrainerSerializer(many=True)


    class Meta:
        model = Admin
        fields = ['name']


class ClientSerializer(serializers.ModelSerializer):
    trainer = TrainerSerializer(many=True)
    admin = AdminSerializer(many=True)


    class Meta:
        model = Client
        fields = ['name']