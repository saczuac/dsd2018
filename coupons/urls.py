from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from .api import CouponViewSet

router = DefaultRouter()
router.register(r'coupon', CouponViewSet)


coupons_urls = [
    url(r'^', include(router.urls)),
]
