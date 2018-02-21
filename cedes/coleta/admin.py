from django.contrib import admin

# Register your models here.
from .models import *

<<<<<<< HEAD
admin.site.register(CentroPesquisa)
=======
class PesquisadorLocalInline(admin.TabularInline):
    model=Pesquisador
    fk_name='centro_local'
    extra=3

# class PesquisadorColaboradorInline(admin.TabularInline):
#     model=Pesquisador
#     fk_name='centro_colaborador'
#     extra=3

class PesquisaInline(admin.TabularInline):
    model=Pesquisa
    extra=3

class CentroPesquisaAdmin(admin.ModelAdmin):
    inlines= [
        PesquisadorLocalInline,
        # PesquisadorColaboradorInline,
        PesquisaInline,
    ]


admin.site.register(CentroPesquisa,CentroPesquisaAdmin)
>>>>>>> 9c7bebf86f0a64344c3f258ea84cea93d66fa010
admin.site.register(Pesquisador)
admin.site.register(Pesquisa)
admin.site.register(EstruturaFisica)
admin.site.register(Evento)
admin.site.register(DifusaoMidiatica)

admin.site.register(AtividadeFormacao)
admin.site.register(Orientacao)
admin.site.register(Intercambio)
admin.site.register(IntervencaoPolitica)
admin.site.register(CentroMemoria)
