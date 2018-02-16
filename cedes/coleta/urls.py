from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index-geral'),
    path('<centro>/',index_centro,name='index-centro'),

    #objetivo estrutura física
    path('<centro>/estrutura/update/', EstruturaFisicaUpdate.as_view(), name='estrutura-fisica-update'),
    #usar <centro>/estrutura/1/update/
    path('<centro>/centromemoria/<pk>/update/', CentroMemoriaUpdate.as_view(), name='centro-memoria-update'),
    #usar <centro>/centromemoria/1/update/

    #objetivo pesquisa
    path('<centro>/pesquisa/add/', PesquisaCreate.as_view(), name='pesquisa-add'),
    path('<centro>/pesquisa/<pk>/update/', PesquisaUpdate.as_view(), name='pesquisa-update'),
    path('<centro>/pesquisa/<pk>/delete/', PesquisaDelete.as_view(), name='pesquisa-delete'),
    path('<centro>/pesquisa/list/', PesquisaList.as_view(), name='pesquisa-list'),
    path('<centro>/pesquisa/<pk>/', PesquisaDetail.as_view(template_name='coleta/pesquisa_detail.html'), name='pesquisa-detail'),

    #objetivo divulgação
    path('<centro>/evento/add/', EventoCreate.as_view(), name='evento-add'),
    path('<centro>/evento/<pk>/update/', EventoUpdate.as_view(), name='evento-update'),
    path('<centro>/evento/<pk>/delete/', EventoDelete.as_view(), name='evento-delete'),
    path('<centro>/evento/list/', EventoList.as_view(), name='evento-list'),
    path('<centro>/evento/<pk>/', EventoDetail.as_view(), name='evento-detail'),

    path('<centro>/publicacao/add/', PublicacaoCreate.as_view(), name='publicacao-add'),
    path('<centro>/publicacao/<pk>/update/', PublicacaoUpdate.as_view(), name='publicacao-update'),
    path('<centro>/publicacao/<pk>/delete/', PublicacaoDelete.as_view(), name='publicacao-delete'),
    path('<centro>/publicacao/list/', PublicacaoList.as_view(), name='publicacao-list'),
    path('<centro>/publicacao/<pk>/', PublicacaoDetail.as_view(), name='publicacao-detail'),

    path('<centro>/difusao/add/', DifusaoCreate.as_view(), name='difusao-add'),
    path('<centro>/difusao/<pk>/update/', DifusaoUpdate.as_view(), name='difusao-update'),
    path('<centro>/difusao/<pk>/delete/', DifusaoDelete.as_view(), name='difusao-delete'),
    path('<centro>/difusao/list/', DifusaoList.as_view(), name='difusao-list'),
    path('<centro>/difusao/<pk>/', DifusaoDetail.as_view(), name='difusao-detail'),

    #objetivo formação
    path('<centro>/formacao/add/', FormacaoCreate.as_view(), name='formacao-add'),
    path('<centro>/formacao/<pk>/update/', FormacaoUpdate.as_view(), name='formacao-update'),
    path('<centro>/formacao/<pk>/delete/', FormacaoDelete.as_view(), name='formacao-delete'),
    path('<centro>/formacao/list/', FormacaoList.as_view(), name='formacao-list'),
    path('<centro>/formacao/<pk>/', FormacaoDetail.as_view(template_name='coleta/formacao_detail.html'), name='formacao-detail'),

    path('<centro>/orientacao/add/', OrientacaoCreate.as_view(), name='orientacao-add'),
    path('<centro>/orientacao/<pk>/update/', OrientacaoUpdate.as_view(), name='orientacao-update'),
    path('<centro>/orientacao/<pk>/delete/', OrientacaoDelete.as_view(), name='orientacao-delete'),
    path('<centro>/orientacao/list/', OrientacaoList.as_view(), name='orientacao-list'),
    path('<centro>/orientacao/<pk>/', OrientacaoDetail.as_view(template_name='coleta/orientacao_detail.html'), name='orientacao-detail'),

    path('<centro>/intercambio/add/', IntercambioCreate.as_view(), name='intercambio-add'),
    path('<centro>/intercambio/<pk>/update/', IntercambioUpdate.as_view(), name='intercambio-update'),
    path('<centro>/intercambio/<pk>/delete/', IntercambioDelete.as_view(), name='intercambio-delete'),
    path('<centro>/intercambio/list/', IntercambioList.as_view(), name='intercambio-list'),
    path('<centro>/intercambio/<pk>/', IntercambioDetail.as_view(template_name='coleta/intercambio_detail.html'), name='intercambio-detail'),

    path('<centro>/intervencao/add/', IntervencaoCreate.as_view(), name='intervencao-add'),
    path('<centro>/intervencao/<pk>/update/', IntervencaoUpdate.as_view(), name='intervencao-update'),
    path('<centro>/intervencao/<pk>/delete/', IntervencaoDelete.as_view(), name='intervencao-delete'),
    path('<centro>/intervencao/list/', IntervencaoList.as_view(), name='intervencao-list'),
    path('<centro>/intervencao/<pk>/', IntervencaoDetail.as_view(template_name='coleta/intervencao_detail.html'), name='intervencao-detail'),

]
