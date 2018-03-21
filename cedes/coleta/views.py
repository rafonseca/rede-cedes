from django.shortcuts import render
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView)
from django.views.generic import ListView, DetailView
from django.views import View
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
# from django.contrib.admin.widgets import AdminDateWidget
from django.db import models





def index(request):
    return render(request, 'coleta/index_geral.html')


class CentroPesquisaDetail(UserPassesTestMixin, DetailView):
    model = CentroPesquisa
    slug_field = 'uf'
    slug_url_kwarg = 'centro'
    template_name = 'coleta/index_centro.html'

    def test_func(self):
        self.success_url = reverse_lazy('index-centro',)
        # kwargs={'centro':self.kwargs['centro']})
        # self.redirect_field_name = None
        obj = self.get_object()
        gestores = obj.gestores.all()
        return self.request.user in gestores


class ColetaUpdateView(UserPassesTestMixin, UpdateView):
    slug_field = 'centro'
    slug_url_kwarg = 'centro'

    def test_func(self):
        # self.success_url = reverse_lazy('index-centro',
        # kwargs={'centro':self.kwargs['centro']})
        self.redirect_field_name = None
        obj = self.get_object()
        gestores = obj.centro.gestores.all()
        return self.request.user in gestores

    def get_context_data(self, *args, **kwargs):
        context = super(
            ColetaUpdateView, self).get_context_data(*args, **kwargs)
        centro = self.kwargs['centro']
        centro_object = CentroPesquisa.objects.get(uf=centro)
        extra_context = {
            'centro': centro_object.uf,
            'nome_estado': centro_object.nome_estado,
            'nome_universidade': centro_object.ies,
            }
        context.update(extra_context)
        return context

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super(
            ColetaUpdateView, self).get_form_kwargs(*args, **kwargs)
        form_kwargs['centro'] = self.kwargs['centro']
        return form_kwargs


class ColetaCreateView(UserPassesTestMixin, CreateView):
    slug_field = 'centro'
    slug_url_kwarg = 'centro'

    def test_func(self):
        centro = self.kwargs['centro']
        obj = CentroPesquisa.objects.get(uf=centro)
        gestores = obj.gestores.all()
        return self.request.user in gestores

    def form_valid(self, form):
        self.object = form.save(commit=False)
        centro = self.kwargs['centro']
        self.object.centro = CentroPesquisa.objects.get(uf=centro)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
        # return HttpResponseRedirect(reverse('pesquisa-list',
        #                                     kwargs={'centro': centro}))

    def get_context_data(self, *args, **kwargs):
        context = super(
            ColetaCreateView, self).get_context_data(*args, **kwargs)
        centro = self.kwargs['centro']
        centro_object = CentroPesquisa.objects.get(uf=centro)
        extra_context = {
            'centro': centro_object.uf,
            'nome_estado': centro_object.nome_estado,
            'nome_universidade': centro_object.ies,
            }
        context.update(extra_context)
        return context

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super(
            ColetaCreateView, self).get_form_kwargs(*args, **kwargs)
        form_kwargs['centro'] = self.kwargs['centro']
        return form_kwargs


class ColetaListView(ListView):
    def get_queryset(self):
        return super().get_queryset().filter(centro=self.kwargs['centro'])

    def get_context_data(self, *args, **kwargs):
        context = super(
            ColetaListView, self).get_context_data(*args, **kwargs)
        centro = self.kwargs['centro']
        centro_object = CentroPesquisa.objects.get(uf=centro)
        extra_context = {
            'centro': centro_object.uf,
            'nome_estado': centro_object.nome_estado,
            'nome_universidade': centro_object.ies,
            }
        context.update(extra_context)
        return context


class EstruturaFisicaUpdate(ColetaUpdateView):
    model = EstruturaFisica
    form_class = EstruturaFisicaForm

    def get_success_url(self):
        return reverse_lazy('index-centro')


class CentroMemoriaUpdate(ColetaUpdateView):
    model = CentroMemoria
    form_class = CentroMemoriaForm

    def get_success_url(self):
        return reverse_lazy('index-centro')


class PesquisaCreate(ColetaCreateView):
    model = Pesquisa
    form_class = PesquisaForm

    def get_success_url(self):
        return reverse_lazy('pesquisa-list', kwargs=dict(centro=self.object.centro))


class PesquisaUpdate(ColetaUpdateView):
    model = Pesquisa
    form_class = PesquisaForm

    def get_success_url(self):
        return reverse_lazy('pesquisa-list', kwargs=dict(centro=self.object.centro))

class PesquisaList(ColetaListView):
    model = Pesquisa


class PesquisaDetail(DetailView):
    model = Pesquisa


class PesquisaDelete(DeleteView):
    model = Pesquisa

    def get_success_url(self):
        return reverse_lazy('pesquisa-list', kwargs=dict(centro=self.object.centro))



class EventoCreate(ColetaCreateView):
    model = Evento
    form_class = EventoForm

    def get_success_url(self):
        return reverse_lazy('evento-list', kwargs=dict(centro=self.object.centro))


class EventoUpdate(ColetaUpdateView):
    model = Evento
    form_class = EventoForm

    def get_success_url(self):
        return reverse_lazy('evento-list', kwargs=dict(centro=self.object.centro))


class EventoList(ColetaListView):
    model = Evento


class EventoDelete(DeleteView):
    model = Evento

    def get_success_url(self):
        return reverse_lazy(
            'evento-list', kwargs=dict(centro=self.object.centro))


class EventoDetail(DetailView):
    model = Evento


class PublicacaoCreate(ColetaCreateView):
    model = Publicacao
    form_class = PublicacaoForm

    def get_success_url(self):
        return reverse_lazy('publicacao-list', kwargs=dict(centro=self.object.centro))


class PublicacaoUpdate(ColetaUpdateView):
    model = Publicacao
    form_class = PublicacaoForm
    def get_success_url(self):
        return reverse_lazy('publicacao-list', kwargs=dict(centro=self.object.centro))

class PublicacaoList(ColetaListView):
    model = Publicacao


class PublicacaoDetail(DetailView):
    model = Publicacao


class PublicacaoDelete(DeleteView):
    model = Publicacao
    def get_success_url(self):
        return reverse_lazy('publicacao-list', kwargs=dict(centro=self.object.centro))


class DifusaoCreate(ColetaCreateView):
    model = DifusaoMidiatica
    form_class = DifusaoForm

    def get_success_url(self):
        return reverse_lazy(
            'difusao-list', kwargs=dict(centro=self.object.centro))


class DifusaoUpdate(ColetaUpdateView):
    model = DifusaoMidiatica
    form_class = DifusaoForm

    def get_success_url(self):
        return reverse_lazy('difusao-list', kwargs=dict(centro=self.object.centro))


class DifusaoList(ColetaListView):
    model = DifusaoMidiatica


class DifusaoDelete(DeleteView):
    model = DifusaoMidiatica

    def get_success_url(self):
        return reverse_lazy('difusao-list', kwargs=dict(centro=self.object.centro))


class DifusaoDetail(DetailView):
    model = DifusaoMidiatica


class FormacaoCreate(ColetaCreateView):
    model = AtividadeFormacao
    form_class = FormacaoForm

    def get_success_url(self):
        return reverse_lazy('formacao-list', kwargs=dict(centro=self.object.centro))


class FormacaoUpdate(ColetaUpdateView):
    model = AtividadeFormacao
    form_class = FormacaoForm

    def get_success_url(self):
        return reverse_lazy('formacao-list', kwargs=dict(centro=self.object.centro))



class FormacaoList(ColetaListView):
    model = AtividadeFormacao


class FormacaoDelete(DeleteView):
    model = AtividadeFormacao

    def get_success_url(self):
        return reverse_lazy('formacao-list', kwargs=dict(centro=self.object.centro))


class FormacaoDetail(DetailView):
    model = AtividadeFormacao


class OrientacaoCreate(ColetaCreateView):
    model = Orientacao
    form_class = OrientacaoForm

    def get_success_url(self):
        return reverse_lazy('orientacao-list', kwargs=dict(centro=self.object.centro))


class OrientacaoUpdate(ColetaUpdateView):
    model = Orientacao
    form_class = OrientacaoForm

    def get_success_url(self):
        return reverse_lazy('orientacao-list', kwargs=dict(centro=self.object.centro))


class OrientacaoList(ColetaListView):
    model = Orientacao


class OrientacaoDelete(DeleteView):
    model = Orientacao

    def get_success_url(self):
        return reverse_lazy('orientacao-list', kwargs=dict(centro=self.object.centro))


class OrientacaoDetail(DetailView):
    model = Orientacao


class IntercambioCreate(ColetaCreateView):
    model = Intercambio
    form_class = IntercambioForm

    def get_success_url(self):
        return reverse_lazy('intercambio-list', kwargs=dict(centro=self.object.centro))


class IntercambioUpdate(ColetaUpdateView):
    model = Intercambio
    form_class = IntercambioForm

    def get_success_url(self):
        return reverse_lazy('intercambio-list', kwargs=dict(centro=self.object.centro))


class IntercambioList(ColetaListView):
    model = Intercambio


class IntercambioDelete(DeleteView):
    model = Intercambio

    def get_success_url(self):
        return reverse_lazy('intercambio-list', kwargs=dict(centro=self.object.centro))


class IntercambioDetail(DetailView):
    model = Intercambio


class IntervencaoCreate(ColetaCreateView):
    model = IntervencaoPolitica
    form_class = IntervencaoForm

    def get_success_url(self):
        return reverse_lazy('intervencao-list', kwargs=dict(centro=self.object.centro))


class IntervencaoUpdate(ColetaUpdateView):
    model = IntervencaoPolitica
    form_class = IntervencaoForm

    def get_success_url(self):
        return reverse_lazy('intervencao-list', kwargs=dict(centro=self.object.centro))


class IntervencaoList(ColetaListView):
    model = IntervencaoPolitica


class IntervencaoDelete(DeleteView):
    model = IntervencaoPolitica

    def get_success_url(self):
        return reverse_lazy('intervencao-list', kwargs=dict(centro=self.object.centro))


class IntervencaoDetail(DetailView):
    model = IntervencaoPolitica
