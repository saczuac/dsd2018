# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Product, ProductType
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import ProductTypeSerializer, ProductSerializer, ProductEmployeeSerializer
from rest_framework import permissions

from rest_framework import status
from rest_framework.response import Response

from employees.models import Employee


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = (permissions.IsAuthenticated,)


class ProductDiscriminatedView(APIView):
    queryset = Product.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk=None, format=None):
        is_employee = Employee.objects.filter(user=request.user)
        serializer_class = ProductSerializer
        serializer = None

        if is_employee:
            serializer_class = ProductEmployeeSerializer

        if pk:
            product = Product.objects.filter(pk=pk)
            if not product:
                return Response({'error': 'Product not found'}, status=status.HTTP_400_BAD_REQUEST)

            serializer = serializer_class(product)
        else:
            serializer = serializer_class(self.queryset.all(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes = (permissions.IsAuthenticated,)
