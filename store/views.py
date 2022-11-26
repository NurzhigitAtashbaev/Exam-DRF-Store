from rest_framework import generics

from .models import Store, Product, Buy, Supply
from .serializers import StoreSerializer, BuySerializer, SupplySerializer


class StoreListAPIView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class StoreRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class BuyAPIView(generics.ListCreateAPIView):
    queryset = Buy.objects.all()
    serializer_class = BuySerializer


class StoreSupplyAPIView(generics.UpdateAPIView):
    queryset = Store.objects.all()
    serializer_class = SupplySerializer
