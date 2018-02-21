from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(CentroPesquisa)
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
