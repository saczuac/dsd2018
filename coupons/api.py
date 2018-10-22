# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Coupon
from rest_framework import viewsets
from .serializers import CouponSerializer
from rest_framework import permissions


class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = (permissions.IsAuthenticated,)
