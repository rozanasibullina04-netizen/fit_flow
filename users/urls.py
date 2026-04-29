from django.urls import path, include
from django.contrib import admin
from .views import TrainerListView, TrainerDetailView, AdminListView, AdminUserListView, AdminSubscriptionListView, \
    AdminSubscriptionUpdateView, ClientListView, AdminVisitHistoryView
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('api/v1/trainers/', TrainerListView.as_view(), name='trainer'),
    path('api/v1/trainers/<int:id>/', TrainerDetailView.as_view(), name='trainer-detail'),
    path('api/v1/admin/', AdminListView.as_view(), name='admin'),
    path('api/v1/admin/users/', AdminUserListView.as_view(), name='admin-users'),
    path('api/v1/admin/subscriptions/', AdminSubscriptionListView.as_view(), name='admin-subscriptions'),
    path('api/v1/admin/subscriptions/<int:id>/', AdminSubscriptionUpdateView.as_view(), name='admin-subscriptions-update'),
    path('api/v1/admin/visit-history/', AdminVisitHistoryView.as_view(), name='admin-visit-history'),
    path('api/v1/client/', ClientListView.as_view(), name='client'),
]