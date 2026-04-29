from django.urls import path, include
from .views import SubscriptionsListView, SubscriptionsFreezeView, SubscriptionsTypeListView, \
    SubscriptionsTypeDetailView, SubscriptionsDetailView

urlpatterns = [
    path('api/v1/subscriptions/', SubscriptionsListView.as_view(),
         name='subscriptions'),
    path('api/v1/subscriptions/<int:id>/freeze/', SubscriptionsFreezeView.as_view(),
         name='subscriptions-freeze'),
    path('api/v1/subscription-types/', SubscriptionsTypeListView.as_view(),
         name='subscription-type'),
    path('api/v1/subscription-types/<int:id>/', SubscriptionsTypeDetailView.as_view(),
         name='subscriptions-type-detail'),
    path('api/v1/subscriptions/<int:id>/', SubscriptionsDetailView.as_view(),
         name='subscriptions-detail')
]