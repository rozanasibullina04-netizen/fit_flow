from rest_framework import serializers

from .models import CheckIn, VisitHistory


class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = "__all__"

    def validate(self, attrs):
        client = attrs.get("client") or getattr(self.instance, "client", None)
        subscription = attrs.get("active_subscription") or getattr(self.instance, "active_subscription", None)
        if client and subscription and getattr(subscription, "client_id", None) not in (None, client.id):
            raise serializers.ValidationError(
                {"active_subscription": "Подписка должна принадлежать выбранному клиенту."}
            )
        checked_in_at = attrs.get("checked_in_at") or getattr(self.instance, "checked_in_at", None)
        if self.instance is None and subscription and checked_in_at:
            if not subscription.is_active_on(checked_in_at.date()):
                raise serializers.ValidationError(
                    {"active_subscription": "Subscription is not available for check-in."}
                )
        return attrs


class VisitHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitHistory
        fields = "__all__"

    def validate(self, attrs):
        client = attrs.get("client") or getattr(self.instance, "client", None)
        subscription = attrs.get("subscription") or getattr(self.instance, "subscription", None)
        if client and subscription and getattr(subscription, "client_id", None) not in (None, client.id):
            raise serializers.ValidationError(
                {"subscription": "Подписка должна принадлежать выбранному клиенту."}
            )
        return attrs


class AdminVisitHistorySerializer(VisitHistorySerializer):
    pass
