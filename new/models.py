# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class New(models.Model):
    ide = models.DecimalField(max_digits=6, decimal_places=0)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
