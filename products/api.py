# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Product, ProductType
from rest_framework import viewsets
from .serializers import ProductTypeSerializer, ProductSerializer
from rest_framework import permissions


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = (permissions.IsAuthenticated,)
