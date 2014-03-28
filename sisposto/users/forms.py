# -*- coding: utf-8 -*-
from django import forms
from django.forms import CharField, EmailField
from django.utils.translation import ugettext_lazy as _
from permissions_widget.forms import PermissionSelectMultipleField

from .models import User, Pessoa


class UserForm(forms.ModelForm):
    user_permissions = PermissionSelectMultipleField()

    class Meta:
        # Set this form to use the User model.
        model = User

        # Constrain the UserForm to just these fields.
        fields = ("first_name", "last_name",)


class UserProfileUpdateForm(forms.ModelForm):
    #combo = forms.ComboField([CharField(max_length=20), EmailField()])
    #arquivo = forms.FileField()
    #outro_usuario = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.SelectMultiple(attrs={'class': "custom-scroll"}))
    #usuarios = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': "checkbox-inline"}))
    class Meta:
        # Set this form to use the User model.
        model = Pessoa
        fields = ('nome_completo', 'data_de_nascimento', 'naturalidade')

    def save(self, commit=True):



        return super(UserProfileUpdateForm, self).save(commit)


class SignupForm(forms.Form):
    #signo_maia = forms.CharField(max_length=30, label='Signo Maia')
    #doenca_preferida = forms.CharField(max_length=30, label='Doenca Preferida')

    #def save(self, user):
    #    #doenca_preferida = self.cleaned_data['doenca_preferida']
    #    #signo_maia = self.cleaned_data['signo_maia']

    def signup(self, request, user):
    #    #doenca_preferida = self.cleaned_data['doenca_preferida']
    #    #signo_maia = self.cleaned_data['signo_maia']
        pass



