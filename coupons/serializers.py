from rest_framework import serializers
from .models import Coupon


class CouponSerializer(serializers.Serializer):

    class Meta:
        model = Coupon
        fields = '__all__'
