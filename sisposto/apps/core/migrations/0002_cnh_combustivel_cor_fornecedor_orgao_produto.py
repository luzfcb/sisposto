# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CNH',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(help_text='Data e Hora em que este registro foi criado', verbose_name='Criando em', auto_now_add=True)),
                ('modificado_em', models.DateTimeField(help_text='Data e Hora em que este registro foi modificado', verbose_name='Modificado em', auto_now=True)),
                ('esta_ativo', models.BooleanField(default=True, verbose_name='Esta ativo?')),
                ('numero_cnh', models.CharField(max_length=12, verbose_name='N\xfamero CNH')),
                ('categoria', models.CharField(max_length=12, verbose_name='Categoria', choices=[('A', 'Categoria A'), ('B', 'Categoria B'), ('C', 'Categoria C'), ('D', 'Categoria D'), ('E', 'Categoria E'), ('AB', 'Categoria AB'), ('AC', 'Categoria AC'), ('AD', 'Categoria AD'), ('AE', 'Categoria AE')])),
                ('validade', models.DateField(null=True)),
                ('criado_por', models.ForeignKey(related_name='core_cnh_criado_por', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('modificado_por', models.ForeignKey(related_name='core_cnh_modificado_por', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['-numero_cnh', '-categoria', '-validade'],
                'verbose_name': 'CNH',
                'verbose_name_plural': 'CNHs',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Combustivel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name': 'Combustivel',
                'verbose_name_plural': 'Combustiveis',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name': 'Cor',
                'verbose_name_plural': 'Cores',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(help_text='Data e Hora em que este registro foi criado', verbose_name='Criando em', auto_now_add=True)),
                ('modificado_em', models.DateTimeField(help_text='Data e Hora em que este registro foi modificado', verbose_name='Modificado em', auto_now=True)),
                ('esta_ativo', models.BooleanField(default=True, verbose_name='Esta ativo?')),
                ('nome', models.CharField(max_length=255)),
                ('nome_fantasia', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=255)),
                ('criado_por', models.ForeignKey(related_name='core_fornecedor_criado_por', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('modificado_por', models.ForeignKey(related_name='core_fornecedor_modificado_por', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Orgao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(help_text='Data e Hora em que este registro foi criado', verbose_name='Criando em', auto_now_add=True)),
                ('modificado_em', models.DateTimeField(help_text='Data e Hora em que este registro foi modificado', verbose_name='Modificado em', auto_now=True)),
                ('esta_ativo', models.BooleanField(default=True, verbose_name='Esta ativo?')),
                ('dtvalido_de', models.DateField(auto_now_add=True, verbose_name='Data inicial de utilizacao')),
                ('dtvalido_ate', models.DateField(null=True, verbose_name='Data final de utilizacao', blank=True)),
                ('nome', models.CharField(max_length=255)),
                ('sigla', models.CharField(max_length=20)),
                ('criado_por', models.ForeignKey(related_name='core_orgao_criado_por', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('modificado_por', models.ForeignKey(related_name='core_orgao_modificado_por', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('criado_em', models.DateTimeField(help_text='Data e Hora em que este registro foi criado', verbose_name='Criando em', auto_now_add=True)),
                ('modificado_em', models.DateTimeField(help_text='Data e Hora em que este registro foi modificado', verbose_name='Modificado em', auto_now=True)),
                ('esta_ativo', models.BooleanField(default=True, verbose_name='Esta ativo?')),
                ('criado_por', models.ForeignKey(related_name='core_produto_criado_por', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
                ('modificado_por', models.ForeignKey(related_name='core_produto_modificado_por', editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
