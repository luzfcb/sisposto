# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import User, Pessoa


class UserForm(forms.ModelForm):

    class Meta:
        # Set this form to use the User model.
        model = User

        # Constrain the UserForm to just these fields.
        fields = ("first_name", "last_name")


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        # Set this form to use the User model.
        model = Pessoa
        fields = ('nome_completo', 'data_de_nascimento', 'naturalidade')

    def save(self, commit=True):



        return super(UserProfileUpdateForm, self).save(commit)


class SignupForm(forms.Form):
    signo_maia = forms.CharField(max_length=30, label='Signo Maia')
    doenca_preferida = forms.CharField(max_length=30, label='Doenca Preferida')

    def save(self, user):
        doenca_preferida = self.cleaned_data['doenca_preferida']
        signo_maia = self.cleaned_data['signo_maia']
        print('#########################################')
        print('funcao_save')
        print('doenca_preferida: ', doenca_preferida)
        print('signo_maia: ', signo_maia)
        print('#########################################')

    def signup(self, request, user):
        doenca_preferida = self.cleaned_data['doenca_preferida']
        signo_maia = self.cleaned_data['signo_maia']
        print('#########################################')
        print('funcao_signup')
        print('doenca_preferida: ', doenca_preferida)
        print('signo_maia: ', signo_maia)
        print('request: ', request)
        print('user: ', user.username)
        print('#########################################')
