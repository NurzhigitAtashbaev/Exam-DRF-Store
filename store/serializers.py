from rest_framework.exceptions import NotFound
from rest_framework import serializers
from .models import Store, Product, Buy, Supply


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class BuySerializer(serializers.ModelSerializer):
    class Meta:
        model = Buy
        fields = '__all__'

    def examination(self, validate_data):
        product = Product.objects.get(id=id)
        if product == NotFound:
            raise Exception('Product is not exists')
        product.save()
