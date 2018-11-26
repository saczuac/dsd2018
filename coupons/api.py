# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Coupon

from rest_framework import viewsets, permissions

from .serializers import CouponSerializer

from django_filters import rest_framework


class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = (permissions.IsAuthenticated,)

    filter_backends = (rest_framework.DjangoFilterBackend,)
    filter_fields = (
        'number',
    )
