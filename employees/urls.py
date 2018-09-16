from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from .api import EmployeeViewSet, EmployeeTypesViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'employeestypes', EmployeeTypesViewSet)


employees_urls = [
    url(r'^', include(router.urls)),
]
