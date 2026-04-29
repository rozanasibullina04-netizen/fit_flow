from rest_framework import serializers
from .models import Subscriptions, SubscriptionsFreeze


class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = ['title', 'subscriptions_type', 'start_date', 'end_date', 'time_limit']


class SubscriptionsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        field = ['subscriptions_type', 'status', 'started_at', 'expires_at', 'remaining_visits']


# class SubscriptionsFreezeSerializer(serializers.ModelSerializer):
#     subscriptions = SubscriptionsFreeze(many=True)
#
#
#     class Meta:
#         model = SubscriptionsFreeze
#         fields = ['is_active']


class SubscriptionsTypeSerializer(serializers.ModelSerializers):
    class Meta:
        model = Subscriptions
        fields = ['title', 'price', 'validity_period', 'visits_limit', 'description']


class SubscriptionsTypeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        field = '__all__'