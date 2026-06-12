from rest_framework import serializers

from .models import Subscriptions, SubscriptionsFreeze


class SubscriptionsSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Название не может быть пустым")
        return value


    class Meta:
        model = Subscriptions
        fields = "__all__"

    def validate_title(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Название не может быть пустым.")
        return value

    def validate_subscriptions_type(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Тип подписки не может быть пустым.")
        return value

    def validate(self, attrs):
        start_date = attrs.get("start_date") or getattr(self.instance, "start_date", None)
        end_date = attrs.get("end_date") or getattr(self.instance, "end_date", None)
        activation_date = attrs.get("activation_date") if "activation_date" in attrs else getattr(self.instance, "activation_date", None)
        started_at = attrs.get("started_at") if "started_at" in attrs else getattr(self.instance, "started_at", None)
        expires_at = attrs.get("expires_at") if "expires_at" in attrs else getattr(self.instance, "expires_at", None)
        visits_limit = attrs.get("visits_limit") if "visits_limit" in attrs else getattr(self.instance, "visits_limit", None)
        remaining_visits = attrs.get("remaining_visits") if "remaining_visits" in attrs else getattr(self.instance, "remaining_visits", None)

        errors = {}
        if start_date and end_date and end_date < start_date:
            errors["end_date"] = "Дата окончания не может быть раньше даты начала."
        if activation_date and start_date and activation_date < start_date:
            errors["activation_date"] = "Дата активации не может быть раньше даты начала."
        if activation_date and end_date and activation_date > end_date:
            errors["activation_date"] = "Дата активации не может быть позже даты окончания."
        if started_at and expires_at and expires_at <= started_at:
            errors["expires_at"] = "Дата окончания действия должна быть позже даты начала."
        if visits_limit is not None and remaining_visits is not None and remaining_visits > visits_limit:
            errors["remaining_visits"] = "Количество оставшихся посещений не может превышать лимит."
        if errors:
            raise serializers.ValidationError(errors)
        return attrs


class SubscriptionsDetailSerializer(SubscriptionsSerializer):
    pass


class SubscriptionsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = ["id", "subscriptions_type"]


class SubscriptionsTypeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = ["id", "subscriptions_type"]


class SubscriptionsFreezeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionsFreeze
        fields = "__all__"

    def validate(self, attrs):
        subscription = attrs.get("subscriptions") or getattr(self.instance, "subscriptions", None)
        start_date = attrs.get("start_date") or getattr(self.instance, "start_date", None)
        end_date = attrs.get("end_date") or getattr(self.instance, "end_date", None)
        errors = {}
        if start_date and end_date and end_date < start_date:
            errors["end_date"] = "Дата окончания не может быть раньше даты начала."
        if subscription and start_date and start_date < subscription.start_date:
            errors["start_date"] = "Заморозка не может начаться раньше начала подписки."
        if subscription and end_date and end_date > subscription.end_date:
            errors["end_date"] = "Заморозка не может закончиться позже окончания подписки."
        if errors:
            raise serializers.ValidationError(errors)
        return attrs
