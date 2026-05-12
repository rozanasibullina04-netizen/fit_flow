from rest_framework import serializers
from .models import WaitingList, Booking


class WaitingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitingList
        fields = ['training', 'client', 'created_at']


class BookingSerializer(serializers.ModelSerializer):
    def validate_additional_task(self, value):
        if not value.strip():
            raise serializers.ValidationError("additional task должно быть заполнено")
        return value
    def validate_free_seats(self, value):
        if value < 0:
            raise serializers.ValidationError("free seats не должен быть отрицательным")
        return value


    class Meta:
        model = Booking
        fields = ['client', 'waiting_list', 'additional_task', 'active_subscription', 'free_seats']