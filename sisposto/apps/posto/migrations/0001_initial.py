# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('municipios', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_cnh_combustivel_cor_fornecedor_orgao_produto'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArqueacaoVolume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('altura_em_cm', models.PositiveIntegerField(verbose_name='Altura do liquido combustivel em cm')),
                ('volume', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Bico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_bico', models.PositiveIntegerField(help_text='N\xfamero Unico para identifica\xe7\xe3o do Bico de Abastecimento', verbose_name='N\xfamero do Bico de Abastecimento')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Bomba',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_bomba', models.PositiveIntegerField(help_text='N\xfamero Unico para identifica\xe7\xe3o da Bomba', verbose_name='N\xfamero da Bomba')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EncerranteBico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_encerrante', models.PositiveIntegerField()),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criando em')),
                ('modificado_em', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('ativo', models.BooleanField(default=True, verbose_name='Esta ativo?')),
                ('bico', models.ForeignKey(related_name='registros_encerrantes', to='posto.Bico')),
            ],
            options={
                'ordering': ['-criado_em'],
                'get_latest_by': 'criado_em',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='EntradaCombustivel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(help_text='Data e Hora em que este registro foi criado', verbose_name='Criando em', auto_now_add=True)),
                ('modificado_em', models.DateTimeField(help_text='Data e Hora em que este registro foi modificado', verbose_name='Modificado em', auto_now=True)),
                ('esta_ativo', models.BooleanField(default=True, verbose_name='Esta ativo?')),
                ('empresa_fornecedora', models.CharField(max_length=255)),
                ('empresa_transportadora', models.CharField(max_length=255)),
                ('numero_nfe', models.CharField(max_length=20, verbose_name='N\xfamero da nota fiscal')),
                ('quantidade_combustivel', models.DecimalField(verbose_name='Quantidade de combustivel em Litros', max_digits=65, decimal_places=3)),
                ('valor_unitario_combustivel', models.DecimalField(verbose_name='Valor unitario em R$', max_digits=10, decimal_places=4)),
                ('valor_total_combustivel', models.DecimalField(verbose_name='Valor Total em R$', editable=False, max_digits=10, decimal_places=4)),
                ('combustivel', models.ForeignKey(related_name='entradas_combustiveis', to='core.Combustivel')),
                ('criado_por', models.ForeignKey(related_name='posto_entradacombustivel_criado_por', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('modificado_por', models.ForeignKey(related_name='posto_entradacombustivel_modificado_por', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Entrada de Combustivel',
                'verbose_name_plural': 'Entrada de Combustiveis',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Posto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.PositiveIntegerField(help_text='N\xfamero Unico para identifica\xe7\xe3o do posto', verbose_name='N\xfamero do Posto de Combustivel')),
                ('nome_posto', models.CharField(help_text='Nome \xfanico Posto de Combustivel ', unique=True, max_length=255, verbose_name='Nome')),
                ('municipio', models.ForeignKey(to='municipios.Municipio')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tanque',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.PositiveIntegerField(help_text='N\xfamero Unico para identifica\xe7\xe3o do tanque', verbose_name='N\xfamero do Tanque de Combustivel')),
                ('data_inicio_operacao', models.DateField(null=True, blank=True)),
                ('volume_maximo_armazenamento', models.DecimalField(max_digits=20, decimal_places=2)),
                ('volume_maximo_lastro', models.DecimalField(max_digits=10, decimal_places=2)),
                ('tipo_tanque', models.CharField(max_length=20, verbose_name='Tipo de disponibiliza\xe7\xe3o f\xedsica do Tanque', choices=[('subterraneo', 'Subterraneo'), ('aereo', 'A\xe9reo')])),
                ('data_emicao_certificado_arqueacao', models.DateField(help_text='Data da emicao pelo Inmetro do Certificado de arquea\xe7\xe3o do tanque e sua respectiva Tabela Volumetrica', verbose_name='Data da emicao do Certificado de arquea\xe7\xe3o')),
                ('posto', models.ForeignKey(related_name='tanques', to='posto.Posto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VolumeHistorico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('altura_em_cm_lida', models.DecimalField(help_text='Insera o valor real da altura do combustivel em rela\xe7\xe3o a r\xe9gua de medi\xe7\xe3o', verbose_name='Altura em cm', max_digits=23, decimal_places=3)),
                ('temperatura_combustivel_lida', models.DecimalField(null=True, max_digits=23, decimal_places=3, blank=True)),
                ('volume_de_combustivel_real', models.DecimalField(max_digits=23, decimal_places=3)),
                ('volume_de_combustivel_corrigido', models.DecimalField(max_digits=23, decimal_places=3)),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Registro criando em')),
                ('tanque', models.ForeignKey(related_name='volumehistoricos', to='posto.Tanque')),
            ],
            options={
                'ordering': ['-criado_em'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='bomba',
            name='posto',
            field=models.ForeignKey(related_name='bombas', to='posto.Posto', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bico',
            name='bomba',
            field=models.ForeignKey(related_name='bicos', to='posto.Bomba', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bico',
            name='tipo_combustivel',
            field=models.ForeignKey(verbose_name='Tipo de Combustivel', to='core.Combustivel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='arqueacaovolume',
            name='tanque',
            field=models.ForeignKey(related_name='registros_volume_arqueadura', to='posto.Tanque'),
            preserve_default=True,
        ),
    ]
