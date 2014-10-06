import autocomplete_light
from datetimewidget.widgets import DateTimeWidget
from django import forms
from apps.veiculos import models


class VeiculoCreateForm(autocomplete_light.ModelForm):
    class Meta:
        model = models.Veiculo
        fields = '__all__'
        # widgets = {
        #     #Use localization and bootstrap 3
        #     'datetime': DateTimeWidget(usel10n = True, bootstrap_version=3)
        # }

class VeiculoUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Veiculo
        fields = ('fabricante', 'modelo')