from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import  ListView, DetailView
from django.urls import reverse_lazy
from .models import *
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseRedirect
def index(request):
    return render(request,'coleta/index_geral.html')

def index_centro(request,centro):
    # print(request,centro)
    centro_object=CentroPesquisa.objects.get(uf=centro)
    return render(request,'coleta/index_centro.html',
        context={
            'centro':centro_onject.uf,
            'nome_estado':centro_object.nome_estado,
            'nome_universidade':centro_object.ies,
            })

class ColetaUpdateView(UserPassesTestMixin,UpdateView):
    slug_field='centro'
    slug_url_kwarg='centro'
    def test_func(self):
        # self.success_url = reverse_lazy('index-centro',kwargs={'centro':self.kwargs['centro']})
        self.redirect_field_name=None
        obj=self.get_object()
        gestores=obj.centro.gestores.all()
        return self.request.user in gestores
class ColetaCreateView(UserPassesTestMixin,CreateView):
    slug_field='centro'
    slug_url_kwarg='centro'
    def test_func(self):
        centro=self.kwargs['centro']
        obj=CentroPesquisa.objects.get(uf=centro)
        gestores=obj.gestores.all()
        return self.request.user in gestores
    def form_valid(self, form):
        self.object = form.save(commit=False)
        centro=self.kwargs['centro']
        self.object.centro=CentroPesquisa.objects.get(uf=centro)
        self.object.save()
        return HttpResponseRedirect(reverse('pesquisa-list',kwargs={'centro':centro}))
class ColetaListView(ListView):
    def get_queryset(self):
        return super().get_queryset().filter(centro=self.kwargs['centro'])


class EstruturaFisicaUpdate(ColetaUpdateView):
    model = EstruturaFisica
    fields= '__all__'

class CentroMemoriaUpdate(ColetaUpdateView):
    model = CentroMemoria
    fields= '__all__'

class PesquisaCreate(ColetaCreateView):
    model = Pesquisa
    fields = ['nome','linha','grupo_pesquisa']
class PesquisaUpdate(ColetaUpdateView):
    model = Pesquisa
    fields = ['nome','linha','grupo_pesquisa']
class PesquisaList(ColetaListView):
    model = Pesquisa
class PesquisaDetail(DetailView):
    model = Pesquisa
class PesquisaDelete(DeleteView):
    model = Pesquisa
    success_url = reverse_lazy('pesquisa-list')

class EventoCreate(ColetaCreateView):
    model = Evento
    fields = '__all__'
    success_url = reverse_lazy('evento-list')
class EventoUpdate(UpdateView):
    model = Evento
    fields = '__all__'
    success_url = reverse_lazy('evento-list')
class EventoList(ColetaListView):
    model = Evento
class EventoDelete(DeleteView):
    model = Evento
class EventoDetail(DetailView):
    model = Evento

class PublicacaoCreate(ColetaCreateView):
    model = Publicacao
    fields = '__all__'
    success_url = reverse_lazy('publicacao-list')
class PublicacaoUpdate(UpdateView):
    model = Publicacao
    fields = '__all__'
class PublicacaoList(ColetaListView):
    model = Publicacao
class PublicacaoDetail(DetailView):
    model = Publicacao
class PublicacaoDelete(DeleteView):
    model = Publicacao
    success_url = reverse_lazy('publicacao-list')

class DifusaoCreate(ColetaCreateView):
    model = DifusaoMidiatica
    fields = '__all__'
    success_url = reverse_lazy('difusao-list')
class DifusaoUpdate(UpdateView):
    model = DifusaoMidiatica
    fields = '__all__'
class DifusaoList(ColetaListView):
    model = DifusaoMidiatica
class DifusaoDelete(DeleteView):
    model = DifusaoMidiatica
    success_url = reverse_lazy('difusao-list')
class DifusaoDetail(DetailView):
    model = DifusaoMidiatica

class FormacaoCreate(ColetaCreateView):
    model = AtividadeFormacao
    fields = '__all__'
    success_url = reverse_lazy('formacao-list')
class FormacaoUpdate(UpdateView):
    model = AtividadeFormacao
    fields = '__all__'
class FormacaoList(ColetaListView):
    model = AtividadeFormacao
class FormacaoDelete(DeleteView):
    model = AtividadeFormacao
    success_url = reverse_lazy('formacao-list')
class FormacaoDetail(DetailView):
    model = AtividadeFormacao


class OrientacaoCreate(ColetaCreateView):
    model = Orientacao
    fields = '__all__'
    success_url = reverse_lazy('orientacao-list')
class OrientacaoUpdate(UpdateView):
    model = Orientacao
    fields = '__all__'
class OrientacaoList(ColetaListView):
    model = Orientacao
class OrientacaoDelete(DeleteView):
    model = Orientacao
    success_url = reverse_lazy('orientacao-list')
class OrientacaoDetail(DetailView):
    model = Orientacao

class IntercambioCreate(ColetaCreateView):
    model = Intercambio
    fields = '__all__'
    success_url = reverse_lazy('intercambio-list')
class IntercambioUpdate(UpdateView):
    model = Intercambio
    fields = '__all__'
class IntercambioList(ColetaListView):
    model = Intercambio
class IntercambioDelete(DeleteView):
    model = Intercambio
    success_url = reverse_lazy('intercambio-list')
class IntercambioDetail(DetailView):
    model = Intercambio

class IntervencaoCreate(ColetaCreateView):
    model = IntervencaoPolitica
    fields = '__all__'
    success_url = reverse_lazy('intervencao-list')
class IntervencaoUpdate(UpdateView):
    model = IntervencaoPolitica
    fields = '__all__'
class IntervencaoList(ColetaListView):
    model = IntervencaoPolitica
class IntervencaoDelete(DeleteView):
    model = IntervencaoPolitica
    success_url = reverse_lazy('intervencao-list')
class IntervencaoDetail(DetailView):
    model = IntervencaoPolitica
