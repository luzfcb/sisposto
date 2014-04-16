# -*- coding: utf-8 -*-

from allauth.account.forms import SignupForm as AllAuthSignupForm
from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Button, Submit
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.forms import CharField, EmailField
from django.utils.translation import ugettext_lazy as _
from permissions_widget.forms import PermissionSelectMultipleField

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

class UserAtualizarForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super(UserAtualizarForm, self).__init__(*args, **kwargs)
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


class UserAllAuthSignupForm(UMixin, AllAuthSignupForm):
    username = forms.CharField(label=_("Username"),
                               max_length=30,
                               min_length=app_settings.USERNAME_MIN_LENGTH,
                               widget=forms.TextInput(
                                   attrs={'placeholder':
                                          _('Username'),
                                          'autofocus': 'autofocus'}))
    email = forms.EmailField(widget=forms.TextInput(attrs=
                                                    {'placeholder':
                                                     _('E-mail address')}))

    def __init__(self, *args, **kwargs):
        email_required = kwargs.pop('email_required',
                                    app_settings.EMAIL_REQUIRED)
        self.username_required = kwargs.pop('username_required',
                                            app_settings.USERNAME_REQUIRED)
        super(UserAllAuthSignupForm, self).__init__(*args, **kwargs)
        # field order may contain additional fields from our base class,
        # so take proper care when reordering...
        field_order = ['email', 'username']
        merged_field_order = list(self.fields.keys())
        if email_required:
            self.fields["email"].label = ugettext("E-mail")
            self.fields["email"].required = True
        else:
            self.fields["email"].label = ugettext("E-mail (optional)")
            self.fields["email"].required = False
            if self.username_required:
                field_order = ['username', 'email']

        # Merge our email and username fields in if they are not
        # currently in the order.  This is to allow others to
        # re-arrange email and username if they desire.  Go in reverse
        # so that we make sure the inserted items are always
        # prepended.
        for field in reversed(field_order):
            if not field in merged_field_order:
                merged_field_order.insert(0, field)
        set_form_field_order(self, merged_field_order)
        if not self.username_required:
            del self.fields["username"]

    def clean_username(self):
        value = self.cleaned_data["username"]
        value = get_adapter().clean_username(value)
        return value

    def clean_email(self):
        value = self.cleaned_data["email"]
        value = get_adapter().clean_email(value)
        if app_settings.UNIQUE_EMAIL:
            if value and email_address_exists(value):
                self.raise_duplicate_email_error()
        return value

    def raise_duplicate_email_error(self):
        raise forms.ValidationError(_("A user is already registered"
                                      " with this e-mail address."))

    def custom_signup(self, request, user):
        custom_form = super(BaseSignupForm, self)
        if hasattr(custom_form, 'signup') and callable(custom_form.signup):
            custom_form.signup(request, user)
        else:
            warnings.warn("The custom signup form must offer"
                          " a `def signup(self, request, user)` method",
                          DeprecationWarning)
            # Historically, it was called .save, but this is confusing
            # in case of ModelForm
            custom_form.save(user)
