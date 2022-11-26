from django.urls import path
from .views import (StoreListAPIView, StoreRetrieveAPIView, BuyAPIView, SupplyAPIView)

urlpatterns = [
    path('stores/', StoreListAPIView.as_view()),
    path('stores/<int:id>/', StoreRetrieveAPIView.as_view()),
    path('stores/<int:id>/buy/', BuyAPIView.as_view()),
    path('stores/<int:id>/supply/', SupplyAPIView.as_view())
]
