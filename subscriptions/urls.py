from django.urls import path

from .views import (
    SubscriptionsDetailView,
    SubscriptionsListView,
    SubscriptionsTypeDetailView,
    SubscriptionsTypeListView,
    SubscriptionFreezeView,
    SubscriptionUnfreezeView,
)

urlpatterns = [
    path('api/v1/subscriptions/', SubscriptionsListView.as_view(),
         name='subscriptions'),
    # path('api/v1/subscriptions/<int:id>/freeze/', SubscriptionsFreezeView.as_view(),
    #      name='subscriptions-freeze'),
    path('api/v1/subscription-types/', SubscriptionsTypeListView.as_view(),
         name='subscription-type'),
    path('api/v1/subscription-types/<int:id>/', SubscriptionsTypeDetailView.as_view(),
         name='subscriptions-type-detail'),
    path('api/v1/subscriptions/<int:id>/', SubscriptionsDetailView.as_view(),
         name='subscriptions-detail'),
    path('api/v1/subscriptions/<int:id>/freeze/', SubscriptionFreezeView.as_view(),
         name='subscriptions-freeze'),
    path('api/v1/subscriptions/<int:id>/unfreeze/', SubscriptionUnfreezeView.as_view(),
         name='subscriptions-unfreeze'),
]
