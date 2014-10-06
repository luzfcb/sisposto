# -*- coding: utf-8 -*-

from django_tables2 import tables
from apps.veiculos import models


class VeiculoListTable(tables.Table):
    class Meta:
        model = models.Veiculo
