from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from .api import SaleViewSet

router = DefaultRouter()
router.register(r'sales', SaleViewSet)

sales_urls = [
    url(r'^', include(router.urls)),
]
