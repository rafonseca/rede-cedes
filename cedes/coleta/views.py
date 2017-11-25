# from django.shortcuts import render
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
# from .models import (
#     CentroPesquisa,
#     Pesquisador,
#     Pesquisa,
# )
# from django.views.generic import ListView, DetailView
#
# class CentroPesquisaDetail(DetailView):
#     model = CentroPesquisa
#
# class CentroPesquisaList(ListView):
#     model = CentroPesquisa
#
# class CentroPesquisaCreate(CreateView):
#     model = CentroPesquisa
#     fields = ['nome']
#
# class CentroPesquisaUpdate(UpdateView):
#     model = CentroPesquisa
#     fields = '__all__'
#
# class CentroPesquisaDelete(DeleteView):
#     model = CentroPesquisa
#     success_url = reverse_lazy('centropesquisa-list')
