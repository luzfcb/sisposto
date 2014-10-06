from django.shortcuts import render

# Create your views here.
from django.views import generic
from django_tables2 import SingleTableMixin
from apps.veiculos import models
from apps.veiculos import tables


class VeiculoList(SingleTableMixin, generic.ListView):
    table_class = tables.VeiculoListTable
    model = models.Veiculo
    paginate_by = 5


class VeiculoCreate(generic.CreateView):
    pass


class VeiculoDetail(generic.DetailView):
    pass


class VeiculoUpdate(generic.UpdateView):
    pass


class VeiculoDelete(generic.DeleteView):
    pass
