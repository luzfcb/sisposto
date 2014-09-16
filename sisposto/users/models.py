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
    pessoa = models.ForeignKey('Pessoa', related_name='trabalhos')
    posto = models.ForeignKey('Posto', related_name='trabalhadores')
    registro = models.TextField()




@python_2_unicode_compatible
class Posto(models.Model):
    nome = models.CharField(max_length=255)
    funcionarios = models.ManyToManyField(Pessoa,  through='Trabalham')

    def __str__(self):
        return "{}".format(self.nome)


class Teste(models.Model):
    id = models.AutoField(auto_created=True, unique=True, db_column='ID_PESSOA', primary_key=True)
    #matricula_ergon_vinculo =

#
# ID_PESSOA
# MATRICULA_ERGON_VINC;
# Matricula;
# DIGITO_ERGON;
# MATRICULA_SIGESP;
# CPF;
# NOME;
# DTNASCIMENTO;
# SEXO;
# NOMEMAE;
# NOME_PAI;
# LOGRADOURO;
# BAIIRO;
# MUNICIPIO;
# CEP;
# TELEFONE;
# DTADMISSAO;
# DT_INGRESSO;
# TIPO_EXCLUSAO;
# DATA_EXCLUSAO;
# TIPOAFASTAMENTO;
# DATA_DESATIVACAO;
# SITUACAOFUNCIONAL;
# LOTACAO;
# DESCRICAO_LOTACAO;
# ESTADOCIVIL;
# RG;
# ORGAO_EXP;
# GRAUINSTRUCAO;
# EMAIL;
# ORGAOATUAL;
# LICENCAMEDICA;
# ID_TIPO_REGISTRO;
# ORGAOORIGEM;
# DTOBITO;
# DTEXONERACAO;
# TABELA_HORARIO
