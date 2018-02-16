from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import  ListView, DetailView
from django.urls import reverse_lazy
from .models import *

def index(request):
    return render(request,'coleta/index_geral.html')

def index_centro(request,centro):
    # print(request,centro)
    return render(request,'coleta/index_centro.html',context={'centro':centro,'nome_estado':centro})


class EstruturaFisicaUpdate(UpdateView):
    model = EstruturaFisica
    fields= '__all__'
    success_url = reverse_lazy('index-centro')
    slug_field='centro'
    slug_url_kwarg='centro'

class CentroMemoriaUpdate(UpdateView):
    model = CentroMemoria
    fields= '__all__'
    success_url = reverse_lazy('index-centro')
    slug_field='centro'
    slug_url_kwarg='centro'


class PesquisaCreate(CreateView):
    model = Pesquisa
    fields = '__all__'
    success_url = reverse_lazy('pesquisa-list')
class PesquisaUpdate(UpdateView):
    model = Pesquisa
    fields = '__all__'
class PesquisaDelete(DeleteView):
    model = Pesquisa
    success_url = reverse_lazy('pesquisa-list')
class PesquisaList(ListView):
    model = Pesquisa
class PesquisaDetail(DetailView):
    model = Pesquisa

class EventoCreate(CreateView):
    model = Evento
    fields = '__all__'
    success_url = reverse_lazy('evento-list')
class EventoUpdate(UpdateView):
    model = Evento
    fields = '__all__'
class EventoDelete(DeleteView):
    model = Evento
    success_url = reverse_lazy('evento-list')
class EventoList(ListView):
    model = Evento
class EventoDetail(DetailView):
    model = Evento

class PublicacaoCreate(CreateView):
    model = Publicacao
    fields = '__all__'
    success_url = reverse_lazy('publicacao-list')
class PublicacaoUpdate(UpdateView):
    model = Publicacao
    fields = '__all__'
class PublicacaoDelete(DeleteView):
    model = Publicacao
    success_url = reverse_lazy('publicacao-list')
class PublicacaoList(ListView):
    model = Publicacao
class PublicacaoDetail(DetailView):
    model = Publicacao

class DifusaoCreate(CreateView):
    model = DifusaoMidiatica
    fields = '__all__'
    success_url = reverse_lazy('difusao-list')
class DifusaoUpdate(UpdateView):
    model = DifusaoMidiatica
    fields = '__all__'
class DifusaoDelete(DeleteView):
    model = DifusaoMidiatica
    success_url = reverse_lazy('difusao-list')
class DifusaoList(ListView):
    model = DifusaoMidiatica
class DifusaoDetail(DetailView):
    model = DifusaoMidiatica

class FormacaoCreate(CreateView):
    model = AtividadeFormacao
    fields = '__all__'
    success_url = reverse_lazy('formacao-list')
class FormacaoUpdate(UpdateView):
    model = AtividadeFormacao
    fields = '__all__'
class FormacaoDelete(DeleteView):
    model = AtividadeFormacao
    success_url = reverse_lazy('formacao-list')
class FormacaoList(ListView):
    model = AtividadeFormacao
class FormacaoDetail(DetailView):
    model = AtividadeFormacao


class OrientacaoCreate(CreateView):
    model = Orientacao
    fields = '__all__'
    success_url = reverse_lazy('orientacao-list')
class OrientacaoUpdate(UpdateView):
    model = Orientacao
    fields = '__all__'
class OrientacaoDelete(DeleteView):
    model = Orientacao
    success_url = reverse_lazy('orientacao-list')
class OrientacaoList(ListView):
    model = Orientacao
class OrientacaoDetail(DetailView):
    model = Orientacao

class IntercambioCreate(CreateView):
    model = Intercambio
    fields = '__all__'
    success_url = reverse_lazy('intercambio-list')
class IntercambioUpdate(UpdateView):
    model = Intercambio
    fields = '__all__'
class IntercambioDelete(DeleteView):
    model = Intercambio
    success_url = reverse_lazy('intercambio-list')
class IntercambioList(ListView):
    model = Intercambio
class IntercambioDetail(DetailView):
    model = Intercambio

class IntervencaoCreate(CreateView):
    model = IntervencaoPolitica
    fields = '__all__'
    success_url = reverse_lazy('intervencao-list')
class IntervencaoUpdate(UpdateView):
    model = IntervencaoPolitica
    fields = '__all__'
class IntervencaoDelete(DeleteView):
    model = IntervencaoPolitica
    success_url = reverse_lazy('intervencao-list')
class IntervencaoList(ListView):
    model = IntervencaoPolitica
class IntervencaoDetail(DetailView):
    model = IntervencaoPolitica
