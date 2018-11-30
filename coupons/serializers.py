from datetime import date

from rest_framework import serializers
from .models import Coupon


class CouponSerializer(serializers.ModelSerializer):
    is_valid = serializers.SerializerMethodField()
    product_type = serializers.SerializerMethodField()

    def get_product_type(self, obj):
        return obj.product_type.initials if obj.product_type else ''

    def get_is_valid(self, obj):
        return (not obj.used and obj.end_date > date.today())

    class Meta:
        model = Coupon
        fields = ['id', 'is_valid', 'discount_percentage', 'product_type', 'used']
