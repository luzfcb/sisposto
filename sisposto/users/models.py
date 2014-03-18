# -*- coding: utf-8 -*-
# Import the AbstractUser model
from django.contrib.auth.models import AbstractUser

# Import the basic Django ORM models library
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django.utils.translation import ugettext_lazy as _


# Subclass AbstractUser
@python_2_unicode_compatible
class User(AbstractUser):

    def __str__(self):
        return self.username


@python_2_unicode_compatible
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', null=True, blank=True)
    nome_completo = models.CharField(
        verbose_name=_('Nome Completo'),
        max_length=85,

    )
    data_de_nascimento = models.DateField(
        verbose_name=_('Data de Nascimento'),
        null=True
    )
    naturalidade = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome_completo
