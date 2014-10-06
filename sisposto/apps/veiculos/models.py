# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
from apps import core
from apps.core.models import ModeloBasico
from django.core.validators import MinValueValidator


SITUACAO_PATRIMONIAL = (
    ('EM UTILIZACAO', 'Em Utilização pelo Estado'),
    ('LEILOADO', 'Leiloado'),
    ('DOADO', 'Doado'),
)


class Fabricante(ModeloBasico):
    nome = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class Veiculo(ModeloBasico):
    # informacoes do veiculo propriamente padrao para qualquer veiculo
    fabricante = models.ForeignKey('Fabricante')
    modelo = models.CharField(max_length=255)
    ano_fabricacao = models.PositiveIntegerField(
        help_text=u'Ano de Fabricação constante no documento do veículo. Ex.: 1896')
    ano_modelo = models.PositiveIntegerField(help_text=u'Ano do Modelo constante no documento do veículo. Ex.: 1896')
    cor_predominante = models.ForeignKey('core.Cor', verbose_name=u'Cor Predominante')
    chassi = models.CharField(max_length=30, help_text=u'Número do Chassi')
    renavan = models.CharField(max_length=255,
                               help_text=u'Número do Renavan - Registro Nacional de Veículos Automotores')
    tipo_combustivel = models.ForeignKey('core.Combustivel', verbose_name=u'Tipo de Combustivel')
    #placa = models.ForeignKey(Placa, related_name='veiculo', unique=True)
    numero_portas = models.PositiveIntegerField(help_text=u'Número de portas excluindo-se o bagageiro')

    #acessorios = models.ManyToManyField('Acessorio', through='AcessorioVeiculoConservacao', verbose_name=u'Acessórios')

    consumo_medio_por_litro_teorico = models.DecimalField(verbose_name=u'Consumo Teórico de Combustivel por litro',
                                                          help_text=u'Gasto informado na documentação tecnica do veiculo em KM/L',
                                                          max_digits=8,
                                                          decimal_places=2,
                                                          validators=[MinValueValidator(0.0)]
    )
    # declarei do lado errado da relacao
    # consumo_medio_por_litro_atual = models.ForeignKey('ConsumoCombustivel')
    volume_maximo_tanque = models.DecimalField(help_text=u'Volume máximo em litros',
                                               max_digits=8,
                                               decimal_places=2,
                                               validators=[MinValueValidator(0.0)]
    )
    lotacao_maxima = models.IntegerField(help_text=u'Numero maximo de passageiros do veiculo incluindo o condutor')
    categoria_habilitacao_minima = models.CharField(verbose_name='Categoria Minima', max_length=12, choices=core.models.CNH.CNHTipo,
                                                    help_text=u'Categoria de Habilitação miníma exigida ao '
                                                              u'condutor para conduzir o veiculo')

    #    odometro_atual = models.OneToOneField('Odometro', related_name='Odometro_atual',
    #                                          help_text=u'Insira o valor atual do hodometro do veiculo')
    #    odometro_anterior = models.ForeignKey('Odometro', related_name='Odometro_anterior', help_text=u'')

    tipo_veiculo = models.CharField(max_length=100, choices=(('1', 'Carro'),
                                                             ('2', 'Caminhonete'))
    )

    # informacoes de controle veicular
    orgao = models.ForeignKey('core.Orgao')
    eh_caracterizado = models.NullBooleanField(verbose_name=u'É caracterizado?',
                                           default=None,
                                           help_text=u'Marque caso o veiculo possua logomarca oficial do Poder '
                                                     u'Executivo, Legislativo, Judiciário ou Orgão o qual pertence')

    situacao_patrimonial = models.CharField(max_length=500, choices=SITUACAO_PATRIMONIAL,
                                            default=SITUACAO_PATRIMONIAL[0][0])
    esta_liberado_de_pernoite = models.BooleanField(verbose_name=u'Está liberado de Pernoite?',
                                                    default=False,
                                                    help_text=u'Marque caso o veiculo esteja autorizado a permanecer '
                                                              u'fora das garagens do estado após o horario normal '
                                                              u'de expediente')

    esta_bloqueado_abastecimento = models.BooleanField(verbose_name=u'Está com Abastecimento Bloqueado?',
                                                       default=False,
                                                       help_text=u'Marque caso tenha sido identificado alguma '
                                                                 u'irregulariedade em relação ao veiculo')

    def __unicode__(self):
        return "{0}-{1}".format(self.id, self.orgao)

    class Meta:
        ordering = ['orgao', 'tipo_combustivel', 'situacao_patrimonial']

