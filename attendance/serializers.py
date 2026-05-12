from rest_framework import serializers
from .models import VisitHistory, CheckIn


class VisitHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitHistory
        fields = ['date_and_time', 'check_in_time', 'trainer', 'training', 'gym']


class AdminVisitHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitHistory
        field = ['client', 'training', 'check_in_time', 'subscriptions']


class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = ['client', 'checked_in_at', 'active_subscription', 'time_limit']