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
class Pessoa(models.Model):
    user = models.OneToOneField(User, related_name='profile', null=True, blank=True)
    nome_completo = models.CharField(
        verbose_name=_('Nome Completo'),
        max_length=85,
        unique=True,
    )
    data_de_nascimento = models.DateField(
        verbose_name=_('Data de Nascimento'),
        null=True
    )
    naturalidade = models.CharField(max_length=255, null=True, blank=True)
    cadastro_concluido = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return self.nome_completo


class Estado(models.Model):
    nome = models.CharField(max_length=255)



# escola estadual
class SubEmpresa(models.Model):
    nome = models.CharField(max_length=255)

# seduc
class SecretariaEstado(models.Model):
    estado = models.OneToOneField('Estado', related_name='secretarias')
    nome = models.CharField(max_length=255)
    subempresas = models.ManyToManyField('SubEmpresa',  through='SubempresaEmpresa')


class SubempresaEmpresa(models.Model):
    empresa = models.ForeignKey('SecretariaEstado')
    subempresa = models.ForeignKey('SubEmpresa')
    data_vinculo = models.CharField(max_length=255, null=True, blank=True)
    data_desvinculo = models.CharField(max_length=255, null=True, blank=True)




class Trabalham(models.Model):
    nome = models.CharField(max_length=255)
    pessoa = models.ForeignKey('Pessoa', to_field='nome_completo')
    posto = models.ForeignKey('Posto')
    registro = models.TextField()




@python_2_unicode_compatible
class Posto(models.Model):
    nome = models.CharField(max_length=255)
    funcionarios = models.ManyToManyField(Pessoa,  through='Trabalham')

    def __str__(self):
        return "{}".format(self.nome)
