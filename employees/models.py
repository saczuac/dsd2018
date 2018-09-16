# -*- coding: utf-8 -*-
from django.db import models

from django.utils.translation import ugettext as _

from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    employee_type = models.ForeignKey(
        'employees.EmployeeType',
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def __str__(self):
        return self.user.first_name


class EmployeeType(models.Model):
    initials = models.CharField(_('Iniciales'), max_length=50)
    description = models.TextField(_('Descripción'))

    class Meta:
        verbose_name = "Tipo de Empleado"
        verbose_name_plural = "Tipo de Empleados"

    def __str__(self):
        return self.initials
