from rest_framework import serializers
from .models import VisitHistory, CheckIn


class VisitHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitHistory
        fields = ['date_and_time', 'check_in_time', 'trainer', 'training', 'gym']


class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = '__all__'