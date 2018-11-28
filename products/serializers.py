from rest_framework import serializers
from .models import Product, ProductType


class ProductSerializer(serializers.ModelSerializer):
    product_type = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    def get_product_type(self, obj):
        return obj.product_type.initials

    def get_price(self, obj):
        return obj.calculate_price()

    class Meta:
        model = Product
        fields = ['id', 'price', 'product_type', 'name']


class ProductEmployeeSerializer(serializers.ModelSerializer):
    product_type = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    def get_product_type(self, obj):
        return obj.product_type.initials

    def get_price(self, obj):
        return obj.cost_price

    class Meta:
        model = Product
        fields = ['id', 'price', 'product_type', 'name']


class ProductTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductType
        fields = '__all__'
