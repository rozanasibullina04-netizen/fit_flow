from rest_framework import serializers

from .models import Payment


class PaymentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

    def validate_payment_list(self, value):
        return value.strip()

    def validate(self, attrs):
        subscription = attrs.get("subscription")
        if subscription is None and self.instance is not None:
            subscription = self.instance.subscription
        amount = attrs.get("amount")
        if amount is None and self.instance is not None:
            amount = self.instance.amount
        if subscription and amount is not None and amount <= 0:
            raise serializers.ValidationError(
                {"amount": "Payment amount for a subscription must be greater than zero."}
            )
        return attrs
