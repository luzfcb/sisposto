# -*- coding: utf8 -*-
from extra_views import InlineFormSet
from users.models import UserProfile
from .forms import UserProfileUpdateForm


class UserProfileInline(InlineFormSet):
    model = UserProfile

    form_class = UserProfileUpdateForm
