import pandas as pd
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
def select_indicador(indicadores_list):
    select = Select(title="Indicador", value="", options=indicadores_list)
    return select




def mapa(source,color_mapper,plot_width,plot_height):
    mapa_fig = figure(
        tools="pan,box_zoom,wheel_zoom,undo,reset,hover,tap",
        plot_width=plot_width,
        plot_height=plot_height,
    )
    # my_tile=bokeh.models.tiles.WMTSTileSource(
    #     url='https://api.mapbox.com/styles/v1/rdferrari/cj78ytz6l51pw2so2o3bj2d09/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoicmRmZXJyYXJpIiwiYSI6ImNpcDQ4Nm12YjAwNnJsZ20zOXdmc29obmcifQ.Shb8a3P1XAV8cPWR1yGDTA'
    # )
    # tile=mapa_fig.add_tile(my_tile)
    mapa_fig.grid.grid_line_color = None
    mapa_fig.axis[0].visible=False
    mapa_fig.axis[1].visible=False
    mapa_renderer=mapa_fig.patches(
        'x', 'y', source=source,
        fill_color={'field': 'indicador_selecionado', 'transform': color_mapper},
        fill_alpha=1.0,
        line_color="white",
        line_width=0.5,
    )
    mapa_renderer.nonselection_glyph=Patches(
        fill_color={'field': 'indicador_selecionado', 'transform': color_mapper},
        fill_alpha=1.0,
        line_color="white",
        line_width=0.5,
    )
    mapa_renderer.selection_glyph=Patches(
        fill_color={'field': 'indicador_selecionado', 'transform': color_mapper},
        fill_alpha=1.0,
        line_color="gray",
        line_width=5.0,
        line_alpha=0.8,
    )
    hover_mapa = mapa_fig.select_one(HoverTool)
    hover_mapa.point_policy = "follow_mouse"
    hover_mapa.tooltips = [
        ("UF", "@UF"),
        ('Indicador','@indicador_selecionado{0.00}'),
        # ('Meta Financeira','R$ @meta{0,0.00}'),
        # ('Realizado','R$ @realizado{0,0.00}'),
    ]
    mapa_fig.toolbar.logo=None
    mapa_fig.axis[0].visible=False
    mapa_fig.toolbar_location='above'
    return mapa_fig

def vbar(source_barras):
    barras_fig=figure(
        x_range=bokeh.models.ranges.FactorRange(factors=source_barras.data['fatores']),
        plot_height=300,
        # plot_width=plot_width,
        tools='xpan, xwheel_zoom,hover',
        y_range=Range1d(0.0,1.0),
        title='Distribuição do Indicador'
    )

    barras_fig.vbar(
        x='fatores',
        top='valores',
        width=0.5,
        source=source_barras,
        # fill_color={'field': 'valores', 'transform': color_mapper},
        line_color=None,
    )

    hover_barras =barras_fig.select_one(HoverTool)
    hover_barras.point_policy = "follow_mouse"
    hover_barras.tooltips = [
        ("Classificação", "@fatores"),
        ('Porcentagem','@valores{0.00}'),
    ]

    barras_fig.toolbar.logo=None
    barras_fig.toolbar_location='above'
    barras_fig.toolbar_sticky=False
    return barras_fig

def vbar_detail(source_barras):
    barras_fig=figure(
        x_range=bokeh.models.ranges.FactorRange(factors=source_barras.data['fatores']),
        plot_height=300,
        # plot_width=plot_width,
        tools='xpan, xwheel_zoom,hover',
        y_range=Range1d(0.0,1.0),
        title='Nenhum Estado Selecionado'
    )

    barras_fig.vbar(
        x='fatores',
        top='valores',
        width=0.5,
        source=source_barras,
        # fill_color={'field': 'valores', 'transform': color_mapper},
        line_color=None,
    )

    hover_barras =barras_fig.select_one(HoverTool)
    hover_barras.point_policy = "follow_mouse"
    hover_barras.tooltips = [
        ("Índice", "@fatores"),
        ('Valor','@valores{0.00}'),
    ]

    barras_fig.toolbar.logo=None
    barras_fig.toolbar_location='above'
    barras_fig.toolbar_sticky=False
    return barras_fig
