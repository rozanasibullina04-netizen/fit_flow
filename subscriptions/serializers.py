from rest_framework import serializers
from .models import Subscriptions, SubscriptionsFreeze


class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = ['title']


class SubscriptionsFreezeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionsFreeze
        fields = '__all__'