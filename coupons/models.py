# -*- coding: utf-8 -*-
from django.db import models

from django.utils.translation import ugettext as _


class Coupon(models.Model):
    number = models.IntegerField(_('Número'))
    used = models.BooleanField(_('Usado ?'))

    release_date = models.DateField(
        _('Fecha de lanzamiento'),
        auto_now_add=True,
        null=True,
        blank=True
    )

    end_date = models.DateField(
        _('Fecha de fin'),
        null=True,
        blank=True
    )

    discount_percentage = models.FloatField(
        _('Porcentaje de descuento'),
        default=0.0,
    )

    product_type = models.ForeignKey(
        'products.ProductType',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name=_('TIpo de producto relacionado')
    )

    class Meta:
        verbose_name = "Cupon"
        verbose_name_plural = "Cupones"

    def __str__(self):
        return str(self.number) + " " + str(self.used)
