# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Sale
from rest_framework import viewsets
from .serializers import SaleSerializer
from rest_framework import permissions


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = (permissions.IsAuthenticated,)
