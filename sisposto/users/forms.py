# -*- coding: utf-8 -*-
from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Button, Submit
from django import forms

from .models import User, Pessoa


class UserForm(forms.ModelForm):
    #user_permissions = PermissionSelectMultipleField()

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_style = 'inline'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'

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


class UMixin(object):
    def __init__(self, *args, **kwargs):
        super(UMixin, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.render_unmentioned_fields = True
        self.helper.layout = Layout(
            FormActions(
                Button('cancel', 'Cancelar', css_class='btn-default'),
                Submit('salvar', u'Salvar modificacoes'),
            )
        )




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



