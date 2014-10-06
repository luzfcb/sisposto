import autocomplete_light
from django import forms
from apps.posto import models


class PostoCreateForm(autocomplete_light.ModelForm):
    class Meta:
        model = models.Posto
        fields = '__all__'

class PostoUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Posto
        fields = '__all__'
