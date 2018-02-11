from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$',index),
    #objetivo estrutura física
    url(r'estrutura/<int:pk>/update/', EstruturaFisicaUpdate.as_view(), name='estrutura-fisica-update'),

    #objetivo pesquisa
    url(r'pesquisa/add/', PesquisaCreate.as_view(), name='pesquisa-add'),
    url(r'pesquisa/(?P<pk>\d+)/update/', PesquisaUpdate.as_view(), name='pesquisa-update'),
    url(r'pesquisa/(?P<pk>\d+)/delete/', PesquisaDelete.as_view(), name='pesquisa-delete'),
    url(r'pesquisa/list/', PesquisaList.as_view(), name='pesquisa-list'),
    url(r'pesquisa/(?P<pk>\d+)/', PesquisaDetail.as_view(template_name='coleta/pesquisa_detail.html'), name='pesquisa-detail'),

    #objetivo divulgação
    url(r'evento/add/', EventoCreate.as_view(), name='evento-add'),
    url(r'evento/(?P<pk>\d+)/update/', EventoUpdate.as_view(), name='evento-update'),
    url(r'evento/(?P<pk>\d+)/delete/', EventoDelete.as_view(), name='evento-delete'),
    url(r'evento/list/', EventoList.as_view(), name='evento-list'),
    url(r'evento/(?P<pk>\d+)/', EventoDetail.as_view(), name='evento-detail'),

    url(r'publicacao/add/', PublicacaoCreate.as_view(), name='publicacao-add'),
    url(r'publicacao/(?P<pk>\d+)/update/', PublicacaoUpdate.as_view(), name='publicacao-update'),
    url(r'publicacao/(?P<pk>\d+)/delete/', PublicacaoDelete.as_view(), name='publicacao-delete'),
    url(r'publicacao/list/', PublicacaoList.as_view(), name='publicacao-list'),
    url(r'publicacao/(?P<pk>\d+)/', PublicacaoDetail.as_view(), name='publicacao-detail'),

    url(r'difusao/add/', DifusaoCreate.as_view(), name='difusao-add'),
    url(r'difusao/(?P<pk>\d+)/update/', DifusaoUpdate.as_view(), name='difusao-update'),
    url(r'difusao/(?P<pk>\d+)/delete/', DifusaoDelete.as_view(), name='difusao-delete'),
    url(r'difusao/list/', DifusaoList.as_view(), name='difusao-list'),
    url(r'difusao/(?P<pk>\d+)/', DifusaoDetail.as_view(), name='difusao-detail'),

    #objetivo formação
    url(r'formacao/add/', FormacaoCreate.as_view(), name='formacao-add'),
    url(r'formacao/(?P<pk>\d+)/update/', FormacaoUpdate.as_view(), name='formacao-update'),
    url(r'formacao/(?P<pk>\d+)/delete/', FormacaoDelete.as_view(), name='formacao-delete'),
    url(r'formacao/list/', FormacaoList.as_view(), name='formacao-list'),
    url(r'formacao/(?P<pk>\d+)/', FormacaoDetail.as_view(template_name='coleta/formacao_detail.html'), name='formacao-detail'),

    url(r'orientacao/add/', OrientacaoCreate.as_view(), name='orientacao-add'),
    url(r'orientacao/(?P<pk>\d+)/update/', OrientacaoUpdate.as_view(), name='orientacao-update'),
    url(r'orientacao/(?P<pk>\d+)/delete/', OrientacaoDelete.as_view(), name='orientacao-delete'),
    url(r'orientacao/list/', OrientacaoList.as_view(), name='orientacao-list'),
    url(r'orientacao/(?P<pk>\d+)/', OrientacaoDetail.as_view(template_name='coleta/orientacao_detail.html'), name='orientacao-detail'),

    url(r'intercambio/add/', IntercambioCreate.as_view(), name='intercambio-add'),
    url(r'intercambio/(?P<pk>\d+)/update/', IntercambioUpdate.as_view(), name='intercambio-update'),
    url(r'intercambio/(?P<pk>\d+)/delete/', IntercambioDelete.as_view(), name='intercambio-delete'),
    url(r'intercambio/list/', IntercambioList.as_view(), name='intercambio-list'),
    url(r'intercambio/(?P<pk>\d+)/', IntercambioDetail.as_view(template_name='coleta/intercambio_detail.html'), name='intercambio-detail'),

    url(r'intervencao/add/', IntervencaoCreate.as_view(), name='intervencao-add'),
    url(r'intervencao/(?P<pk>\d+)/update/', IntervencaoUpdate.as_view(), name='intervencao-update'),
    url(r'intervencao/(?P<pk>\d+)/delete/', IntervencaoDelete.as_view(), name='intervencao-delete'),
    url(r'intervencao/list/', IntervencaoList.as_view(), name='intervencao-list'),
    url(r'intervencao/(?P<pk>\d+)/', IntervencaoDetail.as_view(template_name='coleta/intervencao_detail.html'), name='intervencao-detail'),



]
