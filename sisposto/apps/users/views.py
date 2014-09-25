from django.shortcuts import render
from django.views import generic
from django_tables2.views import SingleTableMixin

from .models import User

from .tables import UserTables


class UsersListView(SingleTableMixin, generic.ListView):
    model = User
    table_class = UserTables
