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
