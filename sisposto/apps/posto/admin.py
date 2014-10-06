from django.contrib import admin

# Register your models here.
from apps.posto import forms
from apps.utils.autoregister import autoregister_admin


from . import models

class PostoAdmin(admin.ModelAdmin):
    form = forms.PostoCreateForm
    list_display = ('numero', 'nome_posto', 'get_monicipio_name')

    def get_monicipio_name(self, obj):
        return u"{0} - {1}".format(obj.municipio.nome, obj.municipio.uf)
    get_monicipio_name.short_description = 'Municipio/Estado'
    get_monicipio_name.allow_tags = False
    list_filter = ['nome_posto', 'municipio__uf' ]


admin.site.register(models.Posto, PostoAdmin)

autoregister_admin(models)