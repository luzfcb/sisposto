from django.shortcuts import render

# Create your views here.
from django.views import generic
from django_tables2 import SingleTableMixin, SingleTableView
from apps.posto import models
from apps.posto import tables
from apps.posto.tables import PostoListTable



#class PostoList(SingleTableMixin, generic.ListView):
class PostoList(SingleTableView):
    table_class = PostoListTable
    model = models.Posto
    paginate_by = 5


class PostoCreate(generic.CreateView):
    pass


class PostoDetail(generic.DetailView):
    pass


class PostoUpdate(generic.UpdateView):
    pass


class PostoDelete(generic.DeleteView):
    pass
