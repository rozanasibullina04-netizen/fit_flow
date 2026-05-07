from rest_framework import serializers
from .models import Subscriptions, SubscriptionsFreeze


class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = ['title', 'status', 'subscriptions_type', 'start_date', 'end_date', 'time_limit']


class SubscriptionsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        field = ['subscriptions_type', 'status', 'started_at', 'expires_at', 'remaining_visits']


class SubscriptionsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = ['title', 'price', 'validity_period', 'visits_limit', 'description']


class SubscriptionsTypeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        field = ['subscriptions_type']


class SubscriptionsFreezeSerializer(serializers.ModelSerializer):
    models = SubscriptionsFreeze
    field = ['start_date', 'end_date', 'is_active']