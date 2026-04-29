from rest_framework import serializers
from .models import WaitingList, Booking


class WaitingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitingList
        fields = ['creation_time']


class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['active_subscription', 'free_seats']