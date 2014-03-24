# -*- coding: utf-8 -*-
from extra_views import InlineFormSet

from users.models import Pessoa
from .forms import UserProfileUpdateForm


class UserProfileInline(InlineFormSet):
    model = Pessoa

    form_class = UserProfileUpdateForm
