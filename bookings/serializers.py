from rest_framework import serializers
from .models import WaitingList, Booking


class WaitingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitingList
        fields = ['training', 'client', 'created_at']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['client', 'waiting_list', 'additional_task', 'free_seats']