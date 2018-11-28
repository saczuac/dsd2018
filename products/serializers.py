from rest_framework import serializers
from .models import Product, ProductType


class ProductSerializer(serializers.ModelSerializer):
    product_type = serializers.SerializerMethodField()

    def get_product_type(self, obj):
        return obj.product_type.initials

    class Meta:
        model = Product
        fields = '__all__'


class ProductTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductType
        fields = '__all__'
