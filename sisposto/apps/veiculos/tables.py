# -*- coding: utf-8 -*-

from django_tables2 import tables
from apps.veiculos import models

TEMPLATE = '''
   <a href="{% url veiculo_edit record.pk %}" class="tbl_icon edit">Edit</a>
   <a href="{% url veiculo_delete record.pk %}" class="tbl_icon delete">Delete</a>
'''

# http://stackoverflow.com/questions/6275193/django-tables2-linkcolumn-multiple-items-in-the-same-cell

class VeiculoListTable(tables.Table):
    column_name = tables.columns.TemplateColumn(TEMPLATE)
    class Meta:
        model = models.Veiculo
