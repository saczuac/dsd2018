from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from .api import ProductViewSet, ProductTypeViewSet, ProductDiscriminatedView

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'producttypes', ProductTypeViewSet)


products_urls = [
    url(
        r'^list/(?P<pk>\d+)$',
        ProductDiscriminatedView.as_view(),
        name='product-list-detail'
    ),

    url(
        r'^list$',
        ProductDiscriminatedView.as_view(),
        name='product-list'
    ),

    url(r'^', include(router.urls)),
]
