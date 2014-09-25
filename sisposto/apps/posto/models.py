# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from apps.core.models import ModeloBasico


class EncerranteBico(models.Model):
    numero_encerrante = models.PositiveIntegerField()

    bico = models.ForeignKey('Bico', related_name='registros_encerrantes')

    criado_em = models.DateTimeField('Criando em', auto_now_add=True, editable=False)
    modificado_em = models.DateTimeField('Modificado em', auto_now=True)
    ativo = models.BooleanField(u'Esta ativo?', default=True)

    @property
    def posto_nome(self):
        return self.bico.posto_nome

    @property
    def bomba_numero(self):
        return self.bico.numero_bico

    @property
    def tipo_combustivel(self):
        return self.bico.tipo_combustivel

    def __unicode__(self):
        return unicode(self.numero_encerrante)

    class Meta:
        ordering = ['-criado_em']
        get_latest_by = 'criado_em'
        app_label = 'postos'


class Bico(models.Model):
    numero_bico = models.PositiveIntegerField(verbose_name=u'Número do Bico de Abastecimento',
                                              help_text=u'Número Unico para identificação do Bico de Abastecimento',
    )
    tipo_combustivel = models.ForeignKey('core.Combustivel', verbose_name='Tipo de Combustivel')
    bomba = models.ForeignKey('Bomba', related_name='bicos', null=True)

    @property
    def posto_nome(self):
        return self.bomba.posto_nome

    def __unicode__(self):
        return unicode('Bico {0}'.format(self.numero_bico))

    @property
    def ultimo_encerrante(self):
        encerrante = self.registros_encerrantes.latest()
        return '%s | %s' % (encerrante.numero_encerrante, encerrante.criado_em)

    # @models.permalink
    # def get_absolute_url(self):
    #     return ('bico-edit', {
    #         'posto_pk': self.bomba.posto.pk,
    #         'bomba_pk': self.bomba.pk,
    #         'pk': self.pk})

    @property
    def get_url_keys(self):
        return (self.bomba.posto.pk,
                self.bomba.pk,
                self.pk)

    class Meta:
        app_label = 'postos'


class Bomba(models.Model):
    numero_bomba = models.PositiveIntegerField(verbose_name=u'Número da Bomba',
                                               help_text=u'Número Unico para identificação da Bomba',
    )

    posto = models.ForeignKey('Posto', related_name='bombas', null=True)

    @property
    def posto_nome(self):
        return self.posto.nome_posto

    @property
    def quantidade_bicos(self):
        return self.bicos.count()

    def __unicode__(self):
        return unicode('Bomba {0}'.format(self.numero_bomba))

    class Meta:
        app_label = 'postos'


class ArqueacaoVolume(models.Model):
    """
    Descreve a relacao entre a `altura_em_cm` e o `volume` do liquido combustivel dentro de um deterninado tanque.
    Basicamente eh uma relacao chave:valor, onde a chave eh `altura_em_cm` e o valor `volume`.

    Os dados necessarios para ArqueacaoVolume, são descritos na "Tabela Fisica Volumetrica" especifica para o tanque,
    Esta tabela eh disponibilizada apos analise do tanque pelo Inmetro, o qual fornece o Certificado de Arqueação e a respectiva tabela volumetrica

    referencias:
    http://www2.inmetro.gov.br/cartadeservicos/servico.php?id=10
    http://www.inmetro.gov.br/ftp_hp/kits/nie_dimel_021_rev03.pdf
    """
    altura_em_cm = models.PositiveIntegerField(verbose_name='Altura do liquido combustivel em cm')
    volume = models.DecimalField(max_digits=10, decimal_places=2)
    tanque = models.ForeignKey('Tanque', related_name='registros_volume_arqueadura')

    def __unicode__(self):
        return '{altura} cm = {volume} L'.format(altura=self.altura_em_cm, volume=self.volume)

    class Meta:
        app_label = 'postos'

class VolumeHistorico(models.Model):
    """
    Registra a medicao do volume do combustivel.

    """
    #volume_de_combustivel_lida = models.DecimalField(max_digits=23, decimal_places=3)
    altura_em_cm_lida = models.DecimalField(verbose_name='Altura em cm', max_digits=23, decimal_places=3,
                            help_text=u'Insera o valor real da altura do combustivel em relação a régua de medição')
    temperatura_combustivel_lida = models.DecimalField(max_digits=23, decimal_places=3, blank=True,
                                                       null=True)
    volume_de_combustivel_real = models.DecimalField(max_digits=23, decimal_places=3)

    volume_de_combustivel_corrigido = models.DecimalField(max_digits=23, decimal_places=3)
    tanque = models.ForeignKey('Tanque', related_name='volumehistoricos')
    criado_em = models.DateTimeField('Registro criando em', auto_now_add=True, editable=False)

    def __unicode__(self):
        return unicode(self.volume_de_combustivel_corrigido)

    def clean(self):
        arqueacaoVolumeInstance = ArqueacaoVolume.objects.get(tanque_id=self.tanque_id, altura_em_cm__exact=self.altura_em_cm_lida)

        self.volume_de_combustivel_corrigido = arqueacaoVolumeInstance.volume
        super(VolumeHistorico, self).clean()


    def save(self, *args, **kwargs):
        #arqueacaoVolumeInstance = ArqueacaoVolume.objects.get(tanque_id=self.tanque_id, altura_em_cm__exact=self.altura_em_cm_lida)
       # self.volume_de_combustivel_corrigido = arqueacaoVolumeInstance.volume
        super(VolumeHistorico, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-criado_em']
        app_label = 'postos'

#signals.pre_save.connect(volumeHistorico_antes_salvar_function, sender=VolumeHistorico)



class Tanque(models.Model):

    numero = models.PositiveIntegerField(verbose_name=u'Número do Tanque de Combustivel',
                                         help_text=u'Número Unico para identificação do tanque',
    )

    data_inicio_operacao = models.DateField(null=True, blank=True)
    volume_maximo_armazenamento = models.DecimalField(max_digits=20, decimal_places=2)
    volume_maximo_lastro = models.DecimalField(max_digits=10, decimal_places=2)

    tipo_tanque = models.CharField(max_length=20,
                                   verbose_name='Tipo de disponibilização física do Tanque',
                                   choices=(
                                       ('subterraneo', 'Subterraneo'),
                                       ('aereo', 'Aéreo'),)
    )


    #tipo_combustivel = models.ForeignKey('core.Combustivel', verbose_name='Tipo de Combustivel')

    posto = models.ForeignKey('Posto', related_name='tanques')


    data_emicao_certificado_arqueacao = models.DateField(
        verbose_name='Data da emicao do Certificado de arqueação',
        help_text=u'Data da emicao pelo Inmetro do Certificado de arqueação do tanque e sua respectiva Tabela Volumetrica')

    def __unicode__(self):
        return unicode('{0} - {1}'.format(self.numero, self.volume_maximo_armazenamento))

    class Meta:
        app_label = 'postos'


class Posto(models.Model):
    numero = models.PositiveIntegerField(verbose_name=u'Número do Posto de Combustivel',
                                         help_text=u'Número Unico para identificação do posto')

    nome_posto = models.CharField(max_length=255, unique=True,
                                  verbose_name=u'Nome',
                                  help_text=u'Nome único Posto de Combustivel ',
                                  )

    municipio = models.ForeignKey('municipios.Municipio')

    @property
    def quantidade_tanques(self):
        return self.tanques.count()

    @property
    def quantidade_bombas(self):
        return self.bombas.count()


    #def get_absolute_url(self):
    #    return '/posto/{id}/'.format(id=self.id)

    def __unicode__(self):
        return unicode(u'Posto Numero: {0} - Nome: {1}'.format(self.numero, self.nome_posto))

    @models.permalink
    def get_absolute_url(self):
        return ('posto-edit', self.pk, )

    class Meta:
        app_label = 'postos'


#class EstoqueContabil(models.Model):
#    numero_nfe = models.CharField(max_length=20,
#                                  verbose_name=unicode(u'Número da nota fiscal'),
#    )
#
#    empresa_fornecedora = models.ForeignKey('core.Fornecedor', related_name='estoquescontabeis_fornecedora')
#    empresa_transportadora = models.ForeignKey('core.Fornecedor', related_name='estoquescontabeis_transportadora')
#
#    qnt_total_combustivel = models.DecimalField(max_digits=65, decimal_places=3, )
#    valor_unitario_combustivel = models.DecimalField(max_digits=10, decimal_places=4, )
#    tipo_combustivel = models.ForeignKey('core.Combustivel', verbose_name='Tipo do Combustivel')
#
#    #user = models.ForeignKey('auth.User')
#
#
#
#    def valor_total(self):
#        return self.valor_unitario_combustivel * self.qnt_total_combustivel
#
#    def __unicode__(self):
#        return u'NF-e: {0} - Fornecedor: {1} - Qnt Combustivel: {2}L - V. Unitario: R${3} - V. Total: R${4}'.format(
#            self.numero_nfe, self.empresa_fornecedora.nome_fantasia, self.qnt_total_combustivel,
#            self.valor_unitario_combustivel, self.valor_total())






class EntradaCombustivel(ModeloBasico):
    """
    Eh realizado uma entrada de combustivel por nota-fiscal,
    nao podera haver mais de um tipo de combustivel na mesma
    nota fiscal e na mesma entrada de combustivel
    """
    empresa_fornecedora = models.CharField(max_length=255)
    empresa_transportadora = models.CharField(max_length=255)

    combustivel = models.ForeignKey('core.Combustivel', related_name='entradas_combustiveis')
    numero_nfe = models.CharField(max_length=20,
                                  verbose_name=unicode(u'Número da nota fiscal'), )
    quantidade_combustivel = models.DecimalField(verbose_name='Quantidade de combustivel em Litros', max_digits=65,
                                                 decimal_places=3, )

    valor_unitario_combustivel = models.DecimalField(verbose_name='Valor unitario em R$', max_digits=10,
                                                     decimal_places=4)

    valor_total_combustivel = models.DecimalField(verbose_name='Valor Total em R$', max_digits=10,
                                                  decimal_places=4,
                                                  editable=False
    )

    def valor_total_calculado(self):
        """
        Calcula o valor total do combustivel, realizando a multiplicacao da
        quantidade_combustivel pelo valor_unitario_combustivel.

        No calculo, eh utilizado calculo de numeros decimais em detrimento a utilizacao de
        numeros de ponto flutuante (float, double), devido aos problemas de precisao ja conhecidos,
        como explicado nos links:

        http://www.ibm.com/developerworks/library/j-jtp0114/
        http://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html
        http://docs.python.org/2/tutorial/floatingpoint.html
        http://docs.python.org/2/library/decimal.html#module-decimal
        http://pymotw.com/2/decimal/

        """
        resultado = self.valor_unitario_combustivel * self.quantidade_combustivel
        return resultado

    valor_total_calculado.short_description = 'Valor total Calculado pelo sistema'

    class Meta:
        verbose_name = 'Entrada de Combustivel'
        verbose_name_plural = 'Entrada de Combustiveis'
        app_label = 'postos'
