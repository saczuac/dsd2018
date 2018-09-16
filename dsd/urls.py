from django.contrib import admin
from django.urls import path, include

from products.urls import products_urls

from employees.urls import employees_urls

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='DSD API')

urlpatterns = [
    path('api/', schema_view),
    path('api/products/', include(products_urls)),
    path('api/employees/', include(employees_urls)),
    path('admin/', admin.site.urls),
]
