from django.shortcuts import render
from django.views import generic

from .models import User
# Create your views here.
class UsersListView(generic.ListView):
    model = User
