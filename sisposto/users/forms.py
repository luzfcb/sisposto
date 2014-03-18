# -*- coding: utf-8 -*-
from django import forms


from .models import User, UserProfile


class UserForm(forms.ModelForm):

    class Meta:
        # Set this form to use the User model.
        model = User

        # Constrain the UserForm to just these fields.
        fields = ("first_name", "last_name")


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        # Set this form to use the User model.
        model = UserProfile
        fields = ('nome_completo', 'data_de_nascimento', 'naturalidade')
