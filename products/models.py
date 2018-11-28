# -*- coding: utf-8 -*-
from django.db import models

from django.utils.translation import ugettext as _


class Product(models.Model):
    name = models.CharField(_('Nombre'), max_length=50)
    cost_price = models.FloatField(_('Precio de compra'))
    sale_price = models.FloatField(_('Precio de venta'))

    product_type = models.ForeignKey(
        'products.ProductType',
        on_delete=models.PROTECT
    )

    def calculate_price(self):
        discount = 0
        price = self.sale_price
        diff = self.sale_price - self.cost_price

        if self.product_type.initials.lower() == 'electro':
            discount = (diff * 50) / 100
        else:
            ten_percentage = (self.cost_price * 10) / 100

            if diff > ten_percentage:
                excedent = diff - ten_percentage
                discount = (excedent * 80) / 100
                excedent = excedent - discount

                return self.cost_price + ten_percentage + excedent

        price = price - discount
        return price

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.name


class ProductType(models.Model):
    initials = models.CharField(_('Iniciales'), max_length=50)
    description = models.TextField(_('Descripción'))

    class Meta:
        verbose_name = "Tipo de Producto"
        verbose_name_plural = "Tipos de Producto"

    def __str__(self):
        return self.initials
