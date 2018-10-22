# -*- coding: utf-8 -*-
from django.db import models

from django.utils.translation import ugettext as _


class Coupon(models.Model):
    number = models.IntegerField(_('Número'))
    used = models.BooleanField(_('Usado ?'))

    class Meta:
        verbose_name = "Cupon"
        verbose_name_plural = "Cupones"

    def __str__(self):
        return str(self.number) + " " + str(self.used)
