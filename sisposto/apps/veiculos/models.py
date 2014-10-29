# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
from apps import core
from apps.core.models import ModeloBasico
from django.core.validators import MinValueValidator

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
    # identificacao_patrimonial = models.CharField(max_length=100, null=True)
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

