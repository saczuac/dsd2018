# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Employee, EmployeeType
from rest_framework import viewsets
from .serializers import EmployeeTypeSerializer, EmployeeSerializer
from rest_framework import permissions


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)


class EmployeeTypesViewSet(viewsets.ModelViewSet):
    queryset = EmployeeType.objects.all()
    serializer_class = EmployeeTypeSerializer
    permission_classes = (permissions.IsAuthenticated,)
