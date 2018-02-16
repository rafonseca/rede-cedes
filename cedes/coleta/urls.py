from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    #objetivo estrutura física
    path('estrutura/<pk>/update/', EstruturaFisicaUpdate.as_view(), name='estrutura-fisica-update'),
    path('centromemoria/<pk>/update/', CentroMemoriaUpdate.as_view(), name='centro-memoria-update'),

    #objetivo pesquisa
    path('pesquisa/add/', PesquisaCreate.as_view(), name='pesquisa-add'),
    path('pesquisa/<pk>/update/', PesquisaUpdate.as_view(), name='pesquisa-update'),
    path('pesquisa/<pk>/delete/', PesquisaDelete.as_view(), name='pesquisa-delete'),
    path('pesquisa/list/', PesquisaList.as_view(), name='pesquisa-list'),
    path('pesquisa/<pk>/', PesquisaDetail.as_view(template_name='coleta/pesquisa_detail.html'), name='pesquisa-detail'),

    #objetivo divulgação
    path('evento/add/', EventoCreate.as_view(), name='evento-add'),
    path('evento/<pk>/update/', EventoUpdate.as_view(), name='evento-update'),
    path('evento/<pk>/delete/', EventoDelete.as_view(), name='evento-delete'),
    path('evento/list/', EventoList.as_view(), name='evento-list'),
    path('evento/<pk>/', EventoDetail.as_view(), name='evento-detail'),

    path('publicacao/add/', PublicacaoCreate.as_view(), name='publicacao-add'),
    path('publicacao/<pk>/update/', PublicacaoUpdate.as_view(), name='publicacao-update'),
    path('publicacao/<pk>/delete/', PublicacaoDelete.as_view(), name='publicacao-delete'),
    path('publicacao/list/', PublicacaoList.as_view(), name='publicacao-list'),
    path('publicacao/<pk>/', PublicacaoDetail.as_view(), name='publicacao-detail'),

    path('difusao/add/', DifusaoCreate.as_view(), name='difusao-add'),
    path('difusao/<pk>/update/', DifusaoUpdate.as_view(), name='difusao-update'),
    path('difusao/<pk>/delete/', DifusaoDelete.as_view(), name='difusao-delete'),
    path('difusao/list/', DifusaoList.as_view(), name='difusao-list'),
    path('difusao/<pk>/', DifusaoDetail.as_view(), name='difusao-detail'),

    #objetivo formação
    path('formacao/add/', FormacaoCreate.as_view(), name='formacao-add'),
    path('formacao/<pk>/update/', FormacaoUpdate.as_view(), name='formacao-update'),
    path('formacao/<pk>/delete/', FormacaoDelete.as_view(), name='formacao-delete'),
    path('formacao/list/', FormacaoList.as_view(), name='formacao-list'),
    path('formacao/<pk>/', FormacaoDetail.as_view(template_name='coleta/formacao_detail.html'), name='formacao-detail'),

    path('orientacao/add/', OrientacaoCreate.as_view(), name='orientacao-add'),
    path('orientacao/<pk>/update/', OrientacaoUpdate.as_view(), name='orientacao-update'),
    path('orientacao/<pk>/delete/', OrientacaoDelete.as_view(), name='orientacao-delete'),
    path('orientacao/list/', OrientacaoList.as_view(), name='orientacao-list'),
    path('orientacao/<pk>/', OrientacaoDetail.as_view(template_name='coleta/orientacao_detail.html'), name='orientacao-detail'),

    path('intercambio/add/', IntercambioCreate.as_view(), name='intercambio-add'),
    path('intercambio/<pk>/update/', IntercambioUpdate.as_view(), name='intercambio-update'),
    path('intercambio/<pk>/delete/', IntercambioDelete.as_view(), name='intercambio-delete'),
    path('intercambio/list/', IntercambioList.as_view(), name='intercambio-list'),
    path('intercambio/<pk>/', IntercambioDetail.as_view(template_name='coleta/intercambio_detail.html'), name='intercambio-detail'),

    path('intervencao/add/', IntervencaoCreate.as_view(), name='intervencao-add'),
    path('intervencao/<pk>/update/', IntervencaoUpdate.as_view(), name='intervencao-update'),
    path('intervencao/<pk>/delete/', IntervencaoDelete.as_view(), name='intervencao-delete'),
    path('intervencao/list/', IntervencaoList.as_view(), name='intervencao-list'),
    path('intervencao/<pk>/', IntervencaoDetail.as_view(template_name='coleta/intervencao_detail.html'), name='intervencao-detail'),

]
