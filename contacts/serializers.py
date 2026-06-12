from rest_framework import serializers

from .models import ContactList


class ContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactList
        fields = "__all__"

    def validate_client_list(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Список клиентов не может быть пустым.")
        return value

    def validate_phone(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Телефон не может быть пустым.")
        return value
