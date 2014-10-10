from django.core.urlresolvers import reverse_lazy
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
    model = models.Veiculo
    success_url = reverse_lazy('veiculo_list')


class VeiculoDetail(generic.DetailView):
    model = models.Veiculo
    success_url = reverse_lazy('veiculo_list')


class VeiculoUpdate(generic.UpdateView):
    model = models.Veiculo
    success_url = reverse_lazy('veiculo_list')


class VeiculoDelete(generic.DeleteView):
    model = models.Veiculo
    success_url = reverse_lazy('veiculo_list')
