from rest_framework import serializers

from .models import Booking, WaitingList


class WaitingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaitingList
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

    def validate_additional_task(self, value):
        value = value.strip()
        return value

    def validate(self, attrs):
        client = attrs.get("client") or getattr(self.instance, "client", None)
        subscription = attrs.get("active_subscription") or getattr(self.instance, "active_subscription", None)
        check_in = attrs.get("check_in") or getattr(self.instance, "check_in", None)
        if client and subscription and getattr(subscription, "client_id", None) not in (None, client.id):
            raise serializers.ValidationError(
                {"active_subscription": "Подписка должна принадлежать выбранному клиенту."}
            )
        if client and check_in and check_in.client_id != client.id:
            raise serializers.ValidationError(
                {"check_in": "Отметка посещения должна принадлежать выбранному клиенту."}
            )
        return attrs
