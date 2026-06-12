from datetime import date

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from notifications.models import Notifications
from subscriptions.models import Subscriptions


class ApiSmokeTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="test-password")
        self.client.force_authenticate(self.user)

    def test_api_requires_authentication(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse("contacts"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_collection_endpoints_are_available(self):
        route_names = [
            "trainer",
            "admin",
            "admin-users",
            "admin-subscriptions",
            "client",
            "admin-stats",
            "subscriptions",
            "subscription-type",
            "schedule",
            "workout",
            "gym",
            "training",
            "scheduled-event",
            "training-type",
            "waiting-list",
            "booking",
            "visit-history",
            "admin-visit-history",
            "check-ins",
            "notifications",
            "payments",
            "contacts",
        ]

        for route_name in route_names:
            with self.subTest(route_name=route_name):
                response = self.client.get(reverse(route_name))
                self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_notification_can_be_created_and_marked_read(self):
        create_response = self.client.post(
            reverse("notifications"),
            {"title": "Reminder", "message": "Training starts soon."},
        )
        self.assertEqual(create_response.status_code, status.HTTP_201_CREATED)

        notification = Notifications.objects.get()
        self.assertFalse(notification.is_read)

        read_response = self.client.patch(
            reverse("notifications-read", kwargs={"id": notification.id}),
            {},
        )
        self.assertEqual(read_response.status_code, status.HTTP_200_OK)
        notification.refresh_from_db()
        self.assertTrue(notification.is_read)

    def test_contact_validation_rejects_blank_client_list(self):
        response = self.client.post(
            reverse("contacts"),
            {
                "client_list": " ",
                "email": "client@example.com",
                "phone": "+7 999 123-45-67",
                "registration_date": "2026-06-12",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_subscription_can_be_frozen_and_unfrozen(self):
        subscription = Subscriptions.objects.create(
            title="Unlimited",
            status=Subscriptions.STATUS_ACTIVE,
            subscriptions_type="standard",
            price="100.00",
            validity_period=30,
            visits_limit=10,
            remaining_visits=10,
            start_date=date(2099, 1, 1),
            end_date=date(2099, 12, 31),
        )

        freeze_response = self.client.post(
            reverse("subscriptions-freeze", kwargs={"id": subscription.id}),
            {"start_date": "2099-02-01", "end_date": "2099-02-10"},
        )
        self.assertEqual(
            freeze_response.status_code,
            status.HTTP_201_CREATED,
            freeze_response.data,
        )
        subscription.refresh_from_db()
        self.assertEqual(subscription.status, Subscriptions.STATUS_FROZEN)
        self.assertFalse(subscription.is_active_on(subscription.start_date))

        unfreeze_response = self.client.post(
            reverse("subscriptions-unfreeze", kwargs={"id": subscription.id}),
        )
        self.assertEqual(unfreeze_response.status_code, status.HTTP_200_OK)
        subscription.refresh_from_db()
        self.assertEqual(subscription.status, Subscriptions.STATUS_ACTIVE)
