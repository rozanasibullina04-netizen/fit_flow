from rest_framework import serializers
from .models import Notifications


class NotificationsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ['title', 'message', 'notifications_list', 'is_read', 'created_at']