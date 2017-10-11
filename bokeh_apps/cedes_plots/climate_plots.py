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
def select_municipio(indices_df):
    select = Select(title="Município:", value="", options=list(indices_df.index))
    return select

def multi_select_municipio(indices_df,width=300):
    select = MultiSelect(title="Município(s):", value=[], options=list(indices_df.index),width=width)
    return select

def table_select_municipio(source_indice,):
    columns = TableColumn(field='municipio',title='Município(s):')

    tabela=DataTable(
        source=source_indice,
        columns=[columns],
        row_headers=False,
        fit_columns=True,
        selectable=True,
        width=300,
    )
    return tabela


def select_indice(indices_df):
    select = Select(title="Índice:", value=indices_df.columns[-1], options=list(indices_df.columns))
    return select


def mapa(dfsource,indice_label,indice_name,color_mapper,plot_width,plot_height):
    mapa_vulnerabilidade = figure(
        tools="pan,box_zoom,wheel_zoom,undo,reset,hover,tap",
        plot_width=plot_width,
        plot_height=plot_height,
    )
    my_tile=bokeh.models.tiles.WMTSTileSource(
        url='https://api.mapbox.com/styles/v1/rdferrari/cj78ytz6l51pw2so2o3bj2d09/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1IjoicmRmZXJyYXJpIiwiYSI6ImNpcDQ4Nm12YjAwNnJsZ20zOXdmc29obmcifQ.Shb8a3P1XAV8cPWR1yGDTA'
    )
    # tile=mapa_vulnerabilidade.add_tile(my_tile)
    mapa_vulnerabilidade.grid.grid_line_color = None
    mapa_vulnerabilidade.axis[0].visible=False
    mapa_vulnerabilidade.axis[1].visible=False
    mapa_renderer=mapa_vulnerabilidade.patches(
        'x', 'y', source=dfsource,
        fill_color={'field': 'indice', 'transform': color_mapper},
        fill_alpha=1.0,
        line_color="white",
        line_width=0.5,
    )
    mapa_renderer.nonselection_glyph=Patches(
        fill_color={'field': 'indice', 'transform': color_mapper},
        fill_alpha=1.0,
        line_color="white",
        line_width=0.5,
    )
    mapa_renderer.selection_glyph=Patches(
        fill_color={'field': 'indice', 'transform': color_mapper},
        fill_alpha=1.0,
        line_color="gray",
        line_width=5.0,
        line_alpha=0.8,
    )
    hover_mapa = mapa_vulnerabilidade.select_one(HoverTool)
    hover_mapa.point_policy = "follow_mouse"
    hover_mapa.tooltips = [
        ("Município", "@municipio"),
        ('Índice','@indice{0.00}'),
        ('Meta Financeira','R$ @meta{0,0.00}'),
        ('Realizado','R$ @realizado{0,0.00}'),
    ]
    mapa_vulnerabilidade.toolbar.logo=None
    mapa_vulnerabilidade.axis[0].visible=False
    mapa_vulnerabilidade.toolbar_location='above'
    return mapa_vulnerabilidade


def bolhas(dfsource,indice_label,color,preset_hover,plot_width,finance_formatter):
    scatter_gastos_indice=figure(
        plot_height=300,
        plot_width=plot_width,
        tools="pan,box_zoom,wheel_zoom,box_select,tap,hover",
    )
    scatter_renderer=scatter_gastos_indice.circle(
        x='indice',
        y='meta',
        source=dfsource,
        size='sqrt_pop',
        # radius='sqrt_pop',
        fill_alpha=0.5,
        fill_color=color,
        line_color=None
    )
    ay0=scatter_gastos_indice.yaxis[0]
    ay0.formatter=finance_formatter
    ay0.axis_label="Meta Financeira (R$)"
    ax0=scatter_gastos_indice.xaxis[0]
    ax0.axis_label="Índice Selecionado"

    hover_scatter=scatter_gastos_indice.select_one(HoverTool)
    hover_scatter.point_policy=preset_hover.point_policy
    hover_scatter.tooltips=preset_hover.tooltips
    hover_scatter.tooltips.append(('População(2016)',"@pop_2016"))
    scatter_gastos_indice.toolbar.logo=None
    scatter_gastos_indice.toolbar_location='above'
    scatter_gastos_indice.axis[1].axis_label_standoff=0
    return scatter_gastos_indice

def hbar_ind_gastos(source_barras_municipio_indice,
                    source_barras_municipio_gastos,
                    indice_color_mapper,
                    gastos_color_mapper,
                    gastos_max,
                    plot_width,
                    finance_formatter,
                   ):
    barras_municipio=figure(
        y_range=bokeh.models.ranges.FactorRange(factors=['indice','meta','realizado']),
        plot_height=300,
        plot_width=plot_width,
        tools='xpan, xwheel_zoom,hover',
        x_range=Range1d(0.0,1.0)
    )
    barras_municipio.extra_x_ranges= {"gastos_range": Range1d(start=0.0, end=gastos_max)}
    barras_municipio.hbar(
        y='fatores',
        height=0.5,
        right='valores',
        source=source_barras_municipio_indice,
        fill_color={'field': 'valores', 'transform': indice_color_mapper},
        line_color=None,
    )
    barras_municipio.hbar(
        y='fatores',
        height=0.5,
        right='valores',
        source=source_barras_municipio_gastos,
        x_range_name='gastos_range',
        fill_color={'field': 'valores', 'transform': gastos_color_mapper},
        line_color=None,
    )
    barras_municipio.add_layout(LinearAxis(x_range_name="gastos_range"),'above')
    barras_municipio.xaxis[0].formatter=finance_formatter
    barras_municipio.xaxis[0].axis_label='Meta Financeira (R$)'
    barras_municipio.xaxis[1].axis_label='Índice Principal'

    def rename_factors():
        rename_factors_dict={
        'indice': 'Índice',
        'meta': 'R$ Previsto',
        'realizado': 'R$ Realizado',
        }
        return rename_factors_dict[tick]

    barras_municipio.yaxis[0].formatter=formatters.FuncTickFormatter.from_py_func(rename_factors)
    barras_municipio.yaxis[0].minor_tick_out=0
    barras_municipio.yaxis[0].major_tick_out=0

    hover_barras =barras_municipio.select_one(HoverTool)
    hover_barras.point_policy = "follow_mouse"
    hover_barras.tooltips = [
        # ("Município", "@municipio"),
        # ('Índice','@indice{0.00}'),
        # ('Meta Financeira','R$ @meta{0,0.00}'),
        # ('Realizado','R$ @realizado{0,0.00}'),
        ("Valor", '@valores{0,0.00}'),
    ]

    barras_municipio.toolbar.logo=None
    barras_municipio.toolbar_location='above'
    barras_municipio.toolbar_sticky=False
    return barras_municipio


from charts_lib import make_radar_chart
def aranha(source,labels,radar_color_mapper,plot_height=300,plot_width=400):
    fig=figure(
        plot_height=plot_height,
        plot_width=plot_width,
        tools='pan,box_zoom,wheel_zoom,reset',
        x_range=Range1d(-2,4),
        y_range=Range1d(-2,2),
        active_scroll=None,
    )
    nb_factors=len(labels)
    linear_grid=[0.2,0.4,0.6,0.8,1.0]
    radar_grid_df=pd.DataFrame(columns=labels)
    for col in labels:
        radar_grid_df[col]=linear_grid
    source_grid=ColumnDataSource(make_radar_chart(radar_grid_df))
    fig.patches(
        xs='xs',
        ys='ys',
        source=source_grid,
        fill_color=None,
        line_color='grey',
        line_alpha=0.5,
    )
    radar_text_df=pd.DataFrame(data=[[1.2]*nb_factors],columns=labels)
    radar_text_polar_df=make_radar_chart(radar_text_df)
    source_text=ColumnDataSource(dict(
        index=labels,
        x=radar_text_polar_df['xs'][0],
        y=radar_text_polar_df['ys'][0],
        ))
    fig.text(
        x='x',
        y='y',
        source=source_text,
        text='index',
        text_align='center',
        text_baseline='middle',
        text_font='Helvetica',
        text_font_size='8pt',
    )

    r_patches=fig.patches(
        xs='xs',
        ys='ys',
        source=source,
        fill_color=None,
        line_color={'field':'municipio','transform': radar_color_mapper},
        line_width=2,
        legend='municipio',
    )
    # patches_tooltips=[("Município:", "@municipio")]
    # patches_hover = HoverTool(renderers=[r_patches], tooltips=patches_tooltips)
    # fig.add_tools(patches_hover)

    fig.toolbar.logo=None
    fig.toolbar_location='above'
    fig.toolbar_sticky=True
    fig.grid.grid_line_color = None
    fig.axis[0].visible=False
    fig.axis[1].visible=False
    return fig


def htreemap(funcao_data_source,orcamento_color_mapper,plot_width,):
    htreemap_funcao=figure(
        #title='Funções do Plano Plurianual',
        plot_height=300,
        plot_width=plot_width,
        tools='pan,hover,box_zoom,reset',
        #active_scroll='wheel_zoom',
    )
    htreemap_funcao_renderer=htreemap_funcao.quad(
        source=funcao_data_source,
        left='left',
        right='right',
        top='top',
        bottom='bottom',
        fill_color={'field': 'NMFUNCAO', 'transform': orcamento_color_mapper},
        line_color='white',
        legend='NMFUNCAO',
    )
    htreemap_funcao.legend.location = "center_left"
    htreemap_funcao.toolbar.logo=None
    htreemap_funcao.toolbar_location='above'
    hover_htreemap=htreemap_funcao.select_one(HoverTool)
    hover_htreemap.point_policy = "follow_mouse"
    hover_htreemap.tooltips = [
        ('Função','@NMFUNCAO'),
        ('Meta Financeira','R$ @VLMETAFINANCEIRA{0,0.00}'),
        ('Realizado','R$ @VLREALIZADOFINANCEIRO{0,0.00}'),
    ]
    htreemap_funcao.axis.visible=False
    # htreemap_funcao.legend.click_policy="hide"
    return htreemap_funcao

def tabela_orcamento(source_gastos,gastos_cols,gastos_cols_titles,plot_width):
    columns_gastos = [ TableColumn(field=col,title=title) for col, title in zip(gastos_cols,gastos_cols_titles,) ]
    columns_gastos[-1].formatter=NumberFormatter(format='0,0.00',language='pt-br',text_align='right')
    columns_gastos[-2].formatter=NumberFormatter(format='0,0.00',language='pt-br',text_align='right')
    tabela=DataTable(
        source=source_gastos,
        columns=columns_gastos,
        row_headers=False,
        fit_columns=True,
        width=plot_width,
    )
    return tabela
