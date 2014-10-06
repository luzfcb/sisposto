# -*- coding: utf-8 -*-

from django_tables2 import tables
from apps.posto import models


class PostoListTable(tables.Table):
    class Meta:
        model = models.Posto
        fields = ('nome_posto', 'municipio')
        exclude = ('id', )