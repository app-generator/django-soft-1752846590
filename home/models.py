# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    nome = models.TextField(max_length=255, null=True, blank=True)
    password = models.TextField(max_length=255, null=True, blank=True)
    bi = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Produto(models.Model):

    #__Produto_FIELDS__
    codigo = models.IntegerField(null=True, blank=True)
    nome = models.TextField(max_length=255, null=True, blank=True)
    preco = models.IntegerField(null=True, blank=True)
    quantidade = models.IntegerField(null=True, blank=True)
    categoria = models.TextField(max_length=255, null=True, blank=True)
    estado = models.BooleanField()
    acoes = models.CharField(max_length=255, null=True, blank=True)

    #__Produto_FIELDS__END

    class Meta:
        verbose_name        = _("Produto")
        verbose_name_plural = _("Produto")



#__MODELS__END
