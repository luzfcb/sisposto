from django.contrib import admin

# Register your models here.
from . import models
from apps.veiculos import forms


class VeiculoAdmin(admin.ModelAdmin):

    list_display = (
                 "modelo",
                 "fabricante",
                 "ano_fabricacao", "ano_modelo", "cor_predominante", "chassi", "renavan", "tipo_combustivel",
                 "numero_portas", "consumo_medio_por_litro_teorico", "volume_maximo_tanque", "lotacao_maxima",
                 "tipo_veiculo", "orgao", "eh_caracterizado", "situacao_patrimonial",
                 "esta_liberado_de_pernoite", "esta_bloqueado_abastecimento")

    def get_monicipio_name(self, obj):
        return u"{0} - {1}".format(obj.municipio.nome, obj.municipio.uf)
    get_monicipio_name.short_description = 'Municipio/Estado'
    get_monicipio_name.allow_tags = False
    list_filter = ['modelo', 'ano_fabricacao', 'categoria_habilitacao_minima', 'eh_caracterizado', 'esta_liberado_de_pernoite', 'cor_predominante']

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            return forms.VeiculoCreateForm
        else:
            #return super(VeiculoAdmin, self).get_form(request, obj, **kwargs)
            return forms.VeiculoUpdateForm


class FabricanteAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Fabricante, FabricanteAdmin)
admin.site.register(models.Veiculo, VeiculoAdmin)

