# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from django.conf import settings
from django.core.validators import MinValueValidator

from django.db import models

# Create your models here.
from django.utils.translation import ugettext as _
from sitetree.models import TreeItemBase


class SmartTreeItem(TreeItemBase):
    icon_css_class = models.CharField(_('CSS class of icon'), max_length=50, null=True, blank=True)
    show_icon = models.BooleanField(_('Show icon of this item'), default=False)


# classes abstratas
class ModeloBasico(models.Model):
    """
    Modelo padrao abstrato para controle de data e hora de criacao e modificacao
    """
    criado_em = models.DateTimeField(_('Criando em'), auto_now_add=True, editable=False,
                                     help_text=_('Data e Hora em que este registro foi criado'))
    modificado_em = models.DateTimeField(_('Modificado em'), auto_now=True,
                                         help_text=_('Data e Hora em que este registro foi modificado'))

    criado_por = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   related_name="%(app_label)s_%(class)s_criado_por",
                                   null=True, editable=False)
    modificado_por = models.ForeignKey(settings.AUTH_USER_MODEL,
                                       related_name="%(app_label)s_%(class)s_modificado_por",
                                       null=True,
                                       editable=False)

    esta_ativo = models.BooleanField(_(u'Esta ativo?'), default=True, help_text='')

    class Meta:
        abstract = True


class ModeloTemporal(ModeloBasico):
    """
    Modelo padrao abstrato para controle de data e hora de criacao e modificacao e periodo de validade
    """
    dtvalido_de = models.DateField(_('Data inicial de utilizacao'), auto_now_add=True, editable=False)
    dtvalido_ate = models.DateField(_('Data final de utilizacao'), blank=True, null=True)

    class Meta:
        abstract = True


# class Colaborador(ModeloBasico):
# """
# Ver apresentacao de um dos criadores do Django:
#     https://speakerdeck.com/freakboy3742/red-user-blue-user-myuser-auth-dot-user
#
#     Verificar necessidade de utilização de models proxy
#     http://www.marinhobrandao.com/blog/proxy-models-quase-uma-bala-de-prata/
#     """
#     nome = models.CharField(_('Nome'), max_length=40)
#     sobrenome = models.CharField(_('Sobrenome'), max_length=255)
#     identificador_unico = models.CharField(_('CPF'), max_length=255, unique=True)
#     data_nasc = models.DateField(_('Data de Nascimento'))
#     #usuario = models.OneToOneField('users.User', null=True, related_name='colaborador_user')
#
#
#     class Meta:
#         verbose_name = _('UserProfile')
#         verbose_name_plural = _('Colaboradores')
#         ordering = ['-nome', '-sobrenome']


class CNH(ModeloBasico):
    """
    Categoria A – habilita a condução de veículo motorizado de duas ou três rodas, com ou sem carro lateral
    (motos, triciclos etc);

    Categoria B – habilita a condução de veículo motorizado, não abrangido pela categoria A, cujo peso bruto
    total não exceda a três mil e quinhentos quilogramas e cuja lotação não exceda a oito lugares, excluído o do
    motorista (carros de passeio);

    Categoria C – habilita a condução de veículo motorizado utilizado em transporte de carga, cujo peso bruto
    total exceda a três mil e quinhentos quilogramas (caminhões) e utilizado para transporte de até 8 pessoas.
    Para habilitar-se na categoria C, o condutor deve estar habilitado há, pelo menos, um ano na categoria B e
    não ter cometido nenhuma infração grave ou gravíssima, nem ser reincidente em infrações médias, durante os
    últimos doze meses.

    Categoria D – condutor de veículo motorizado utilizado no transporte de passageiros, cuja lotação exceda a
    oito lugares, excluído o do motorista (ônibus). Para habilitar-se na categoria D, o condutor deve estar habilitado
    há, pelo menos, um ano na categoria C ou há dois anos na categoria B e não ter cometido nenhuma infração grave ou
    gravíssima, nem ser reincidente em infrações médias nos últimos doze meses.

    Categoria E – condutor de combinação de veículos em que a unidade tratora se enquadre nas categorias B, C ou D e
    cuja unidade acoplada, reboque, semi-reboque ou articulada, tenha seis mil quilogramas ou mais de peso bruto total,
    ou cuja lotação exceda a oito lugares, ou, ainda, seja enquadrado na categoria trailer. Para habilitar-se na
    categoria E, o condutor deve estar habilitado na categoria D ou há, pelo menos, um ano na categoria C e não ter
    cometido nenhuma infração grave ou gravíssima, nem ser reincidente em infrações médias nos últimos doze meses.9
    """
    # Choices
    CNHTipo = (
        ('A', 'Categoria A'),
        ('B', 'Categoria B'),
        ('C', 'Categoria C'),
        ('D', 'Categoria D'),
        ('E', 'Categoria E'),
        ('AB', 'Categoria AB'),
        ('AC', 'Categoria AC'),
        ('AD', 'Categoria AD'),
        ('AE', 'Categoria AE'),
    )

    numero_cnh = models.CharField(_('Número CNH'), max_length=12, )
    categoria = models.CharField(_('Categoria'), max_length=12, choices=CNHTipo)
    validade = models.DateField(null=True)


    class Meta:
        verbose_name = _('CNH')
        verbose_name_plural = _('CNHs')
        ordering = ['-numero_cnh', '-categoria', '-validade']

    def __unicode__(self):
        return 'CNH Nº: {0} - Categoria: {1} - Validade: {2}'.format(self.numero_cnh, self.categoria, self.validade)


# class Condutora(Pessoa, CNH):
#     """
#     Condutor teste
#     """
#
#     class Meta:
#         verbose_name = _('Condutor')
#         verbose_name_plural = _('Condutores')




class Produto(ModeloBasico):
    pass

    def __unicode__(self):
        return self.nome


class Fornecedor(ModeloBasico):
    nome = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.nome_fantasia)


class Combustivel(models.Model):
    nome = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = _('Combustivel')
        verbose_name_plural = _('Combustiveis')
        ordering = ['nome']


class Cor(models.Model):
    nome = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = _('Cor')
        verbose_name_plural = _('Cores')
        ordering = ['nome']


class Orgao(ModeloTemporal):
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=20)

    def __unicode__(self):
        return self.nome

#
# class Acessorio(ModeloBasico):
#     descricao = models.CharField(max_length=255)
#     eh_obrigatorio = models.BooleanField(default=False, verbose_name=u'É obrigatório')
#
#     def __unicode__(self):
#         return u'{0}'.format(self.descricao)
#
#     class Meta:
#         verbose_name = u'Acessório'
#         verbose_name_plural = u'Acessórios'
#
#
#
#
# COR_PLACA = (
#
# )
#
#
# class TipoPlaca(models.Model):
#     """
#        CBT:
#        Art. 115.
#        § 7o  Excepcionalmente, mediante autorização específica e fundamentada das respectivas corregedorias e com a
#        devida comunicação aos órgãos de trânsito competentes, os veículos utilizados por membros do Poder Judiciário e
#        do Ministério Público que exerçam competência ou atribuição criminal poderão temporariamente ter placas
#        especiais, de forma a impedir a identificação de seus usuários específicos, na forma de regulamento a ser
#        emitido, conjuntamente, pelo Conselho Nacional de Justiça - CNJ, pelo Conselho Nacional do Ministério Público
#        - CNMP e pelo Conselho Nacional de Trânsito - CONTRAN. (Incluído pela Lei nº 12.694, de 2012)
#
#        Art. 116. Os veículos de propriedade da União, dos Estados e do Distrito Federal, devidamente registrados e
#        licenciados, somente quando estritamente usados em serviço reservado de caráter policial, poderão usar placas
#        particulares, obedecidos os critérios e limites estabelecidos pela legislação que regulamenta o uso de veículo
#        oficial.
#
#        http://www.ctbdigital.com.br/?p=Comentarios&Registro=19&campo_busca=&artigo=115
#        http://pt.wikipedia.org/wiki/Placas_de_identifica%C3%A7%C3%A3o_de_ve%C3%ADculos_no_Brasil#Cores
#
#         +-----------------------------------+-----------------------------+
#         |                                   |            COR              |
#         | CATEGORIA DO VEÍCULO              +-----------------------------+
#         |                                   |       PLACA E TARJETA       |
#         |                                   +----------+------------------+
#         |                                   | Fundo    | Caracteres       |
#         +===================================+==========+==================+
#         | Particular                        | Cinza    | Preto            |
#         +-----------------------------------+----------+------------------+
#         | Aluguel                           | Vermelho | Branco           |
#         +-----------------------------------+----------+------------------+
#         | Experiência/Fabricante            | Verde    | Branco           |
#         +-----------------------------------+----------+------------------+
#         | Aprendizagem                      | Branco   | Vermelho         |
#         +-----------------------------------+----------+------------------+
#         | Coleção                           | Preto    | Branco           |
#         +-----------------------------------+----------+------------------+
#         | Coleção ( > 30 anos )             | Preto    | Cinza            |
#         +-----------------------------------+----------+------------------+
#         | Oficial                           | Branco   | Preto            |
#         +-----------------------------------+----------+------------------+
#         | Missão Diplomática                | Azul     | Branco           |
#         +-----------------------------------+----------+------------------+
#         | Corpo Consular                    | Azul     | Branco           |
#         +-----------------------------------+----------+------------------+
#         | Organismo Internacional           | Azul     | Branco           |
#         +-----------------------------------+----------+------------------+
#         | Corpo Diplomático                 | Azul     | Branco           |
#         +-----------------------------------+----------+------------------+
#         | Organismo Consular/Internacional  | Azul     | Branco           |
#         +-----------------------------------+----------+------------------+
#         | Acordo Cooperação Internacional   | Azul     | Branco           |
#         +-----------------------------------+----------+------------------+
#         | Representação                     | Preto    | Dourado          |
#         +-----------------------------------+----------+------------------+
#         | Representação (Presidência)       | Preto    | Verde/Amarelo    |
#         +-----------------------------------+----------+------------------+
#
#
#
#
#     """
#     CORES_FUNDO = (
#         ('Cinza', 'Cinza'),
#         ('Branco', 'Branco'),
#         ('Preto', 'Preto'),
#         ('Vermelho', 'Vermelho'),
#         ('Verde', 'Verde'),
#         ('Azul', 'Azul'),
#         ('Verde e Amarelo', 'Verde e Amarelo')
#     )
#
#     CORES_LETRAS = (
#         ('Cinza', 'Cinza'),
#         ('Branco', 'Branco'),
#         ('Preto', 'Preto'),
#         ('Vermelho', 'Vermelho'),
#         ('Dourado', 'Dourado')
#     )
#     descricao_resumida = models.CharField(u'Descrição Resumida', max_length=350)
#     descricao = models.CharField(u'Descrição', max_length=350)
#     cor_letras = models.CharField(verbose_name=u'Cor das Letras', max_length=255, choices=CORES_LETRAS)
#     cor_fundo = models.CharField(verbose_name=u'Cor do Fundo', max_length=255, choices=CORES_FUNDO)
#
#     def __unicode__(self):
#         return '{desc_resu} - {cor_letra} sobre fundo {cor_fundo}'.format(desc_resu=self.descricao_resumida,
#                                                                           cor_letra=self.cor_letras,
#                                                                           cor_fundo=self.cor_fundo)
#
#
# class Placa(ModeloBasico):
#     numero = models.CharField(max_length=7)
#     municipio = models.ForeignKey('municipios.Municipio')
#     eh_invalida = models.BooleanField(verbose_name=u'É inválida', default=False,
#                                       help_text=u'Marque caso seja veiculo '
#                                                 u'policial de investigação com placa "fria"')
#     tipo_placa = models.ForeignKey('TipoPlaca', verbose_name=u'Cor da Placa',
#                                    help_text=u'Selecione a cor da placa do veiculo conforme a sua utilização')
#
#     veiculo = models.OneToOneField('veiculos.Veiculo', related_name='placa')
#
#     def __unicode__(self):
#         return '{0} - {1}'.format(self.numero, self.municipio)
#
#
# class Periodo(models.Model):
#     data_inicial = models.DateTimeField()
#     data_final = models.DateTimeField()
#     descricao = models.TextField()
#

# class VeiculoPlaca(ModeloBasico):
#     placa = models.ForeignKey('Placa')
#     veiculo = models.ForeignKey('veiculos.Veiculo')
#
#
# class EspecieTipoVeicular(models.Model):
#     pass
#
#
# class UnidadeMedida(models.Model):
#     sigla = models.CharField(max_length=20)
#     descricao = models.TextField()
#
#
# class ConsumoCombustivel(models.Model):
#     medido_em = models.DateTimeField(_('Medido em'), auto_now_add=True, editable=False)
#     ativo = models.BooleanField(_(u'Esta ativo?'), default=True)
#     consumo = models.DecimalField(decimal_places=2, max_digits=4)
#     veiculo = models.ForeignKey('veiculos.Veiculo', related_name='consumo_combustivel_veiculo')
#
#
# class Odometro(models.Model):
#     valor = models.PositiveIntegerField()
#     data_registro = models.DateTimeField(auto_now_add=True)
#     tipo_registro = models.CharField(max_length=200, choices=(('entrada', 'Entrada'),
#                                                               ('saida', 'Saida'))
#     )
#
#     def __unicode__(self):
#         return '{0} - {1}'.format(self.valor, self.tipo_registro)


# class AcessorioVeiculoConservacao(models.Model):
#     ESTADO_CONSERVACAO = (
#         ('bom', 'Bom'),
#         ('regular', 'Regular'),
#         ('imprestavel', 'Imprestavel'),
#         ('faltando', 'Faltando'),
#     )
#
#     acessorio = models.ForeignKey('Acessorio')
#     veiculo = models.ForeignKey('veiculos.Veiculo')
#     conservacao = models.CharField(max_length=11, choices=ESTADO_CONSERVACAO)
#
#     class Meta:
#         verbose_name = u'Acessório'
#         verbose_name_plural = u'Acessórios'
#
