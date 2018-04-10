# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class restrict(models.Model):
    apduModelList = models.CharField(max_length=10000)
    apduResultList = models.CharField(max_length=10000)
    scriptsInstanceId = models.CharField(max_length=100)
    xmTransTime = models.CharField(max_length=40)
    xmTransNum = models.CharField(max_length=40)
    spTransTime = models.CharField(max_length=40)
    spTransNum = models.CharField(max_length=40)
