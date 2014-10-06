# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_cnh_combustivel_cor_fornecedor_orgao_produto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(help_text='Data e Hora em que este registro foi criado', verbose_name='Criando em', auto_now_add=True)),
                ('modificado_em', models.DateTimeField(help_text='Data e Hora em que este registro foi modificado', verbose_name='Modificado em', auto_now=True)),
                ('esta_ativo', models.BooleanField(default=True, verbose_name='Esta ativo?')),
                ('nome', models.CharField(max_length=255)),
                ('criado_por', models.ForeignKey(related_name='veiculos_fabricante_criado_por', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('modificado_por', models.ForeignKey(related_name='veiculos_fabricante_modificado_por', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['nome'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(help_text='Data e Hora em que este registro foi criado', verbose_name='Criando em', auto_now_add=True)),
                ('modificado_em', models.DateTimeField(help_text='Data e Hora em que este registro foi modificado', verbose_name='Modificado em', auto_now=True)),
                ('esta_ativo', models.BooleanField(default=True, verbose_name='Esta ativo?')),
                ('modelo', models.CharField(max_length=255)),
                ('ano_fabricacao', models.PositiveIntegerField(help_text='Ano de Fabrica\xe7\xe3o constante no documento do ve\xedculo. Ex.: 1896')),
                ('ano_modelo', models.PositiveIntegerField(help_text='Ano do Modelo constante no documento do ve\xedculo. Ex.: 1896')),
                ('chassi', models.CharField(help_text='N\xfamero do Chassi', max_length=30)),
                ('renavan', models.CharField(help_text='N\xfamero do Renavan - Registro Nacional de Ve\xedculos Automotores', max_length=255)),
                ('numero_portas', models.PositiveIntegerField(help_text='N\xfamero de portas excluindo-se o bagageiro')),
                ('consumo_medio_por_litro_teorico', models.DecimalField(help_text='Gasto informado na documenta\xe7\xe3o tecnica do veiculo', verbose_name='Consumo Te\xf3rico de Combustivel por litro', max_digits=8, decimal_places=2, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('volume_maximo_tanque', models.DecimalField(help_text='Volume m\xe1ximo em litros', max_digits=8, decimal_places=2, validators=[django.core.validators.MinValueValidator(0.0)])),
                ('lotacao_maxima', models.IntegerField(help_text='Numero maximo de passageiros do veiculo incluindo o condutor')),
                ('categoria_habilitacao_minima', models.CharField(help_text='Categoria de Habilita\xe7\xe3o min\xedma exigida ao condutor para conduzir o veiculo', max_length=12, verbose_name='Categoria Minima', choices=[('A', 'Categoria A'), ('B', 'Categoria B'), ('C', 'Categoria C'), ('D', 'Categoria D'), ('E', 'Categoria E'), ('AB', 'Categoria AB'), ('AC', 'Categoria AC'), ('AD', 'Categoria AD'), ('AE', 'Categoria AE')])),
                ('tipo_veiculo', models.CharField(max_length=100, choices=[('1', 'Carro'), ('2', 'Caminhonete')])),
                ('eh_caracterizado', models.NullBooleanField(default=None, help_text='Marque caso o veiculo possua logomarca oficial do Poder Executivo, Legislativo, Judici\xe1rio ou Org\xe3o o qual pertence', verbose_name='\xc9 caracterizado?')),
                ('situacao_patrimonial', models.CharField(default='EM UTILIZACAO', max_length=500, choices=[('EM UTILIZACAO', 'Em Utiliza\xe7\xe3o pelo Estado'), ('LEILOADO', 'Leiloado'), ('DOADO', 'Doado')])),
                ('esta_liberado_de_pernoite', models.BooleanField(default=False, help_text='Marque caso o veiculo esteja autorizado a permanecer fora das garagens do estado ap\xf3s o horario normal de expediente', verbose_name='Est\xe1 liberado de Pernoite?')),
                ('esta_bloqueado_abastecimento', models.BooleanField(default=False, help_text='Marque caso tenha sido identificado alguma irregulariedade em rela\xe7\xe3o ao veiculo', verbose_name='Est\xe1 com Abastecimento Bloqueado?')),
                ('cor_predominante', models.ForeignKey(verbose_name='Cor Predominante', to='core.Cor')),
                ('criado_por', models.ForeignKey(related_name='veiculos_veiculo_criado_por', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('fabricante', models.ForeignKey(to='veiculos.Fabricante')),
                ('modificado_por', models.ForeignKey(related_name='veiculos_veiculo_modificado_por', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('orgao', models.ForeignKey(to='core.Orgao')),
                ('tipo_combustivel', models.ForeignKey(verbose_name='Tipo de Combustivel', to='core.Combustivel')),
            ],
            options={
                'ordering': ['orgao', 'tipo_combustivel', 'situacao_patrimonial'],
            },
            bases=(models.Model,),
        ),
    ]
