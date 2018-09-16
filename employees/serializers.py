from rest_framework import serializers
from .models import Employee, EmployeeType


class EmployeeSerializer(serializers.Serializer):

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeTypeSerializer(serializers.Serializer):

    class Meta:
        model = EmployeeType
        fields = '__all__'
