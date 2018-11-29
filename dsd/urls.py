from django.contrib import admin
from django.urls import path, include

from products.urls import products_urls

from employees.urls import employees_urls

from frontend.urls import frontend_urls

from bonita.urls import bonita_urls

from sales.urls import sales_urls

from coupons.urls import coupons_urls

from rest_framework_swagger.views import get_swagger_view

from rest_framework_jwt.views import obtain_jwt_token

schema_view = get_swagger_view(title='DSD API')

urlpatterns = [
    path('', include(frontend_urls)),
    path('api/', schema_view),
    path('api/products/', include(products_urls)),
    path('api/bonita/', include(bonita_urls)),
    path('api/employees/', include(employees_urls)),
    path('api/coupons/', include(coupons_urls)),
    path('api/sales/', include(sales_urls)),
    path('auth', obtain_jwt_token),
    path('admin/', admin.site.urls),
]
