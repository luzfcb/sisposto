# -*- coding: utf-8 -*-
import autocomplete_light
from municipios.models import Municipio, UF

from .models import Combustivel

class MunicipioAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^nome', 'uf_sigla', ]
    #autocomplete_js_attributes = {'placeholder': 'Nome da Cidade/Estado'}
    attrs = {
        'data-autcomplete-minimum-characters': 0,
        'placeholder': 'Nome da Cidade/Estado',
    }
    #widget_attrs = {'data-widget-maximum-values': 3}
    limit_choices = 15

class UFAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^nome', 'uf', ]
    attrs = {
        'data-autcomplete-minimum-characters': 0,
        'placeholder': 'Nome do estado ou Sigla'}
    limit_choices = 28

class CombustivelAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^nome']
    attrs = {
        'data-autcomplete-minimum-characters': 0,
        'placeholder': 'Tipo de Combustivel'}
    limit_choices = 15



autocomplete_light.register(Municipio, MunicipioAutocomplete)
autocomplete_light.register(UF, UFAutocomplete)
autocomplete_light.register(Combustivel, CombustivelAutocomplete)
