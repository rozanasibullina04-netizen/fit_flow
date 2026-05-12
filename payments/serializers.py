from rest_framework import serializers
from .models import Payment

class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['payment_id', 'status', 'subscription']


class PaymentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['payment_list']