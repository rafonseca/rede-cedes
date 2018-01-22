from django.contrib import admin

# Register your models here.
from .models import *

class PesquisadorLocalInline(admin.TabularInline):
    model=Pesquisador
    fk_name='centro_local'
    extra=3

class PesquisadorColaboradorInline(admin.TabularInline):
    model=Pesquisador
    fk_name='centro_colaborador'
    extra=3

class PesquisaInline(admin.TabularInline):
    model=Pesquisa
    extra=3

class CentroPesquisaAdmin(admin.ModelAdmin):
    inlines= [
        PesquisadorLocalInline,
        PesquisadorColaboradorInline,
        PesquisaInline,
    ]

# class Meta2Admin(admin.ModelAdmin):
#     inlines= [
#         PesquisadorLocalInline,
#         PesquisadorColaboradorInline,
#         PesquisaInline,
#     ]

admin.site.register(CentroPesquisa,CentroPesquisaAdmin)
admin.site.register(Pesquisador)
admin.site.register(Pesquisa)
admin.site.register(EstruturaFisicaModel)
admin.site.register(Meta2)
#admin.site.register(Meta2,Meta2Admin)
admin.site.register(Evento)
admin.site.register(DifusaoMidiatica)

admin.site.register(AtividadeFormacao)
admin.site.register(Orientacao)
admin.site.register(Intercambio)
admin.site.register(IntervencaoPolitica)


# from import_export import resources
# from import_export.admin import ImportExportModelAdmin

# class CentroPesquisaResource(resources.ModelResource):
#     class Meta:
#         model = CentroPesquisa
# class CentroPesquisaAdmin(ImportExportModelAdmin):
#     resource_class = CentroPesquisaResource
#
# class PesquisadorResource(resources.ModelResource):
#     class Meta:
#         model = Pesquisador
# class PesquisadorAdmin(ImportExportModelAdmin):
#     resource_class = PesquisadorResource
#
# class PesquisaResource(resources.ModelResource):
#     class Meta:
#         model = Pesquisa
# class PesquisaAdmin(ImportExportModelAdmin):
#     resource_class = PesquisaResource
#
# class Meta_1Resource(resources.ModelResource):
#     class Meta:
#         model = Meta_1
# class Meta_1Admin(ImportExportModelAdmin):
#     resource_class = Meta_1Resource


# admin.site.register(CentroPesquisa,CentroPesquisaAdmin)
# admin.site.register(Pesquisador,PesquisadorAdmin)
# admin.site.register(Pesquisa,PesquisaAdmin)
# admin.site.register(Meta_1,Meta_1Admin)
# admin.site.register(Meta_2,Meta_2Admin)
