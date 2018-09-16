from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from .api import ProductViewSet, ProductTypeViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'producttypes', ProductTypeViewSet)


products_urls = [
    url(r'^', include(router.urls)),
]
