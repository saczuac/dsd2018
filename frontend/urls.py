from django.urls import path
from django.contrib.auth import views as auth_views

from .views import ProductListView, ProductBuyView

frontend_urls = [
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'
    ),

    path(
        'logout/',
        auth_views.logout,
        {'next_page': '/'},
        name='logout'
    ),

    path('buy/<int:product_id>', ProductBuyView.as_view(), name='product-buy'),
    path('', ProductListView.as_view(), name='product-list'),
]
