from rest_framework import serializers

from .models import Notifications


class NotificationsListSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Название не должно быть пустым")
        return value
    def validate_message(self, value):
        if not value.strip():
            raise serializers.ValidationError("Поле massage не должно быть пустым")
        return value


    class Meta:
        model = Notifications
        fields = "__all__"

    def validate_title(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Заголовок не может быть пустым.")
        return value

    def validate_message(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Сообщение не может быть пустым.")
        return value
