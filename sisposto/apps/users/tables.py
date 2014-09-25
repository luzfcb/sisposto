# -*- coding: utf-8 -*-
from django_tables2 import tables

from .models import User

class UserTables(tables.Table):
    class Meta:
        model = User