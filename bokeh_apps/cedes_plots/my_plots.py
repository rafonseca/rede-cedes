import pandas as pd
import numpy as np
import bokeh
from bokeh import palettes
from bokeh.models import (
    ColumnDataSource,
    LinearColorMapper,
    CategoricalColorMapper,
    Patches,
    HoverTool,
    Range1d,
    formatters,
    LinearAxis,
    CategoricalAxis,
    Legend,
    )
from bokeh.models.widgets import (
    DataTable,
    NumberFormatter,
    TableColumn,
    Select,
    MultiSelect,
    )
from bokeh.plotting import figure

### Plot Functions Definitions
def select_meta(metas_list):
    select = Select(title="Meta", value="meta_1", options=metas_list)
    return select

def select_indicador(indicadores_list):
    select = Select(title="Indicador", value="indicador_1_1", options=indicadores_list)
    return select

def mapa(source,color_mapper,plot_width,plot_height):
    mapa_fig = figure(
        tools="hover",
        plot_width=plot_width,
        plot_height=plot_height,
    )
    mapa_fig.grid.grid_line_color = None
    mapa_fig.axis[0].visible=False
    mapa_fig.axis[1].visible=False
    mapa_renderer=mapa_fig.patches(
        'x', 'y', source=source,
        fill_color={'field': 'indicador_selecionado', 'transform': color_mapper},
        fill_alpha=1.0,
        line_color="gray",
        line_width=0.5,
    )
    mapa_renderer.nonselection_glyph=Patches(
        fill_color={'field': 'indicador_selecionado', 'transform': color_mapper},
        fill_alpha=1.0,
        line_color="gray",
        line_width=0.5,
    )
    mapa_renderer.selection_glyph=Patches(
        fill_color={'field': 'indicador_selecionado', 'transform': color_mapper},
        fill_alpha=1.0,
        line_color="gray",
        line_width=2.0,
        line_alpha=0.8,
    )
    hover_mapa = mapa_fig.select_one(HoverTool)
    hover_mapa.point_policy = "follow_mouse"
    hover_mapa.tooltips = [
        ("Centro Rede CEDES:", "@nome_universidade"),
        ('Indicador','@indicador_selecionado{0.00}'),
    ]
    mapa_fig.toolbar.logo=None
    mapa_fig.axis[0].visible=False
    mapa_fig.toolbar_location=None
    return mapa_fig

def hbar_indicadores(source,color_mapper,plot_width,plot_height):
    fig=figure(
        y_range=bokeh.models.ranges.FactorRange(factors=source.data['UF'][::-1]),
        plot_height=plot_height,
        plot_width=plot_width,
        tools='hover',
        x_range=Range1d(0.0,1.0),
        # title='Indicador'
        x_axis_location='above'
    )

    fig.hbar(
        y='UF',
        right='indicador_selecionado',
        height=0.5,
        source=source,
        fill_color={'field': 'indicador_selecionado', 'transform': color_mapper},
        line_color=None,
    )

    hover_barras =fig.select_one(HoverTool)
    hover_barras.point_policy = "follow_mouse"
    hover_barras.tooltips = [
        ("UF", "@UF"),
        ('Indicador','@indicador_selecionado{0.00}'),
    ]

    fig.toolbar.logo=None
    # fig.toolbar_location='above'
    # fig.toolbar_sticky=False
    fig.grid.grid_line_color = None
    fig.toolbar_location=None
    # fig.x_axis_location='above'
    # fig.axis[1].visible=False

    return fig

def pizza_plot(source,color_mapper,title,plot_width,plot_height):
    fig=figure(
        # x_range=bokeh.models.ranges.FactorRange(factors=source.data['fatores']),
        plot_width=plot_width,
        plot_height=plot_height,
        tools='',
        # y_range=Range1d(0.0,1.0),
        title=title
    )

    fig.wedge(
        # x='fatores',
        # top='valores',
        # width=0.5,
        # inner_radius=0,
        # outer_radius=1,
        x=0,
        y=0,
        radius=0.4,
        start_angle='start_angle',
        end_angle='end_angle',
        source=source,
        fill_color={'field': 'fatores', 'transform': color_mapper},
        line_color='grey',
        legend='fatores',
    )
    # 
    # hover =fig.select_one(HoverTool)
    # hover.point_policy = "follow_mouse"
    # hover.tooltips = [
    #     ("Classificação", "@fatores"),
    #     ('Porcentagem','@valores{0.00}'),
    # ]

    fig.toolbar.logo=None
    fig.toolbar_location='above'
    fig.toolbar_sticky=True
    fig.grid.grid_line_color = None
    fig.axis[0].visible=False
    fig.axis[1].visible=False

    return fig

def vbar(source,color_mapper,title,plot_width,plot_height):
    fig=figure(
        x_range=bokeh.models.ranges.FactorRange(factors=source.data['fatores']),
        plot_width=plot_width,
        plot_height=plot_height,
        tools='xpan, xwheel_zoom,hover',
        y_range=Range1d(0.0,1.0),
        title=title
    )

    fig.vbar(
        x='fatores',
        top='valores',
        width=0.5,
        source=source,
        fill_color={'field': 'fatores', 'transform': color_mapper},
        line_color=None,
    )

    hover_barras =fig.select_one(HoverTool)
    hover_barras.point_policy = "follow_mouse"
    hover_barras.tooltips = [
        ("Classificação", "@fatores"),
        ('Porcentagem','@valores{0.00}'),
    ]

    fig.toolbar.logo=None
    fig.toolbar_location='above'
    fig.toolbar_sticky=True
    return fig


def table_select(source,plot_width,plot_height):
    columns = TableColumn(field='nome_UF',title='Centro Rede CEDES')

    tabela=DataTable(
        source=source,
        columns=[columns],
        row_headers=False,
        fit_columns=True,
        selectable=True,
        width=plot_width,
        height=plot_height,
    )
    return tabela


def vbar_detail(source,color_mapper,plot_width,plot_height):
    fig=figure(
        x_range=bokeh.models.ranges.FactorRange(factors=source.data['fatores']),
        plot_height=plot_height,
        plot_width=plot_width,
        tools='xpan, xwheel_zoom,hover',
        y_range=Range1d(0.0,1.0),
        title='Nenhum Centro Rede-CEDES Selecionado'
    )

    fig.vbar(
        x='fatores',
        top='valores',
        width=0.5,
        source=source,
        fill_color={'field': 'valores', 'transform': color_mapper},
        line_color=None,
    )
    fig.xaxis.major_label_orientation = np.pi/4
    hover_barras =fig.select_one(HoverTool)
    hover_barras.point_policy = "follow_mouse"
    hover_barras.tooltips = [
        ("Índice", "@fatores"),
        ('Valor','@valores{0.00}'),
    ]

    fig.toolbar.logo=None
    fig.toolbar_location='above'
    fig.toolbar_sticky=True
    return fig
