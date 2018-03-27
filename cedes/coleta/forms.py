from django.forms.models import modelform_factory
from django import forms
from .labels import *
from .models import *
from django_select2 import forms as forms2


class ColetaFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        centro = kwargs.pop('centro')
        super(ColetaFormMixin, self).__init__(*args, **kwargs)
        # general widgets configuration
        for k, v in self.fields.items():
            print(k, v)
            if isinstance(v, forms.fields.DateField):
                v.widget = forms.SelectDateWidget(
                    years=range(2015, 2020))
            if k == 'bolsistas_envolvidos':
                v.queryset = Pesquisador.objects.filter(
                    centro=centro).filter(bolsista=True).order_by('nome')
            if k == 'pesquisadores_envolvidos':
                v.queryset = Pesquisador.objects.filter(
                    centro=centro).filter(bolsista=False).order_by('nome')
            isPesquisadorField = 'coordenador' in k
            isPesquisadorField |= k in [
                'autor', 'orientador', 'estudante_bolsista']
            if isPesquisadorField and \
                    isinstance(v, forms.ModelChoiceField):
                v.queryset = Pesquisador.objects.filter(
                    centro=centro).order_by('nome')





class EstruturaFisicaForm(ColetaFormMixin):
    class Meta:
        model = EstruturaFisica
        fields=[
                'tem_sede',
                'tem_banner',
                'tem_internet',
                'equip_inf',
                'moveis',
                'coordenador',
                'coord_adj',
                'apoio_tecnico',
                'bolsistas',
                'repr_pesquisadores',
                'repr_social',
                ]
        labels = labels_EstruturaFisica


class CentroMemoriaForm(ColetaFormMixin):
    class Meta:
        model = CentroMemoria
        fields=[
                'coordenador',
                'situacao_implementacao',
                'situacao_acervo_fisico',
                'tema',
                'pesquisadores_envolvidos',
                'bolsistas_envolvidos',
                'localizacao_digital',
                'num_titulos',
                ]
        labels = labels_CentroMemoria
        widgets = {
            'pesquisadores_envolvidos': forms2.Select2MultipleWidget,
            'bolsistas_envolvidos': forms2.Select2MultipleWidget,
        }

class PesquisaForm(ColetaFormMixin):
    class Meta:
        fields = ['nome', 'linha', 'grupo_pesquisa']
        labels = labels_Pesquisa
        model = Pesquisa

class EventoForm(ColetaFormMixin):
    class Meta:
        fields = [
            'nome',
            'tipo',
            'abrangencia',
            'coordenador_evento',
            'tema',
            'data_inicio',
            'data_fim',
            'num_participantes',
            'palestrantes',
            'publico_alvo',
            'descricao',
            'local',
            'pesquisadores_envolvidos',
            'bolsistas_envolvidos',
        ]
        widgets = {
            'pesquisadores_envolvidos': forms2.Select2MultipleWidget,
            'bolsistas_envolvidos': forms2.Select2MultipleWidget,
        }
        model = Evento
        labels = labels_Evento


class PublicacaoForm(ColetaFormMixin):
    class Meta:
        model = Publicacao
        fields = [
            'titulo',
            'tipo',
            'autor',
            'abrangencia',
            'referencia_abnt',
            'localizacao_digital',
        ]
        labels = labels_Publicacao

class DifusaoForm(ColetaFormMixin):
    class Meta:
        model = DifusaoMidiatica
        fields=[
            'titulo',
            'tipo',
            'data_inicio',
            'localizacao_digital',
            'coordenador',
            'bolsistas_envolvidos',
            'publico_alvo',
        ]
        labels = labels_DifusaoMidiatica
        widgets = {
            'bolsistas_envolvidos': forms2.Select2MultipleWidget,
        }


class FormacaoForm(ColetaFormMixin):
    class Meta:
        model = AtividadeFormacao
        fields = [
            'titulo',
            'tipo',
            'coordenador_formacao',
            'tema',
            'data_inicio',
            'data_fim',
            'total_horas',
            'num_participantes',
            'palestrantes',
            'publico_alvo',
            'descricao',
            'local',
            'pesquisadores_envolvidos',
            'bolsistas_envolvidos',
        ]
        labels = labels_AtividadeFormacao
        widgets = {
            'pesquisadores_envolvidos': forms2.Select2MultipleWidget,
            'bolsistas_envolvidos': forms2.Select2MultipleWidget,
        }


class OrientacaoForm(ColetaFormMixin):
    class Meta:
        model = Orientacao
        fields = [
            'titulo',
            'tipo',
            'data_inicio',
            'data_fim',
            'orientador',
            'autor',
            'descricao',
        ]
        labels = labels_Orientacao


class IntercambioForm(ColetaFormMixin):
    class Meta:
        model = Intercambio
        fields = [
            'coordenador',
            'estudante_bolsista',
            'data_inicio',
            'data_fim',
            'local',
            'ambito',
            'grupos_estudo',
            'descricao',
        ]
        labels = labels_Intercambio


class IntervencaoForm(ColetaFormMixin):
    class Meta:
        model = IntervencaoPolitica
        fields = [
            'coordenador',
            'nivel_governo',
            'ambito',
            'data_inicio',
            'data_fim',
            'local',
            'descricao',
            'publico_alvo',
            'pesquisadores_envolvidos',
            'bolsistas_envolvidos',
        ]
        labels = labels_IntervencaoPolitica
        widgets = {
            'pesquisadores_envolvidos': forms2.Select2MultipleWidget,
            'bolsistas_envolvidos': forms2.Select2MultipleWidget,
        }
