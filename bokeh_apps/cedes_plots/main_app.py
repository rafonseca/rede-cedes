import os
import numpy as np
import pandas as pd
import bokeh

from bokeh.models import (
    HoverTool,
    ColumnDataSource,
    LinearColorMapper,
    CategoricalColorMapper,
    formatters,
    )
from bokeh import palettes
from . import my_plots

### Load Static Data (No global ColumnDataSource!)
data_dir='../data'
# indicadores_df=pd.read_excel(os.path.join(data_dir,'Tabela-CEDES.xlsx'),'tabela_indicadores')
tabela_UF_df=pd.read_excel(os.path.join(data_dir,'Tabela-02.xlsx'),0)
tabela_UF_df.replace('na',np.nan,inplace=True)
tabela_UF_df.index=tabela_UF_df['UF']
tabela_pesquisa_df=pd.read_excel(os.path.join(data_dir,'Tabela-02.xlsx'),1)
### load shapefile
try:
    lim_uf=pd.read_pickle(os.path.join(data_dir,'LIM_UF.pkl'))
except(FileNotFoundError):
    import geopandas as gpd
    from .aux_geo import getCoords
    lim_uf=gpd.read_file(os.path.join(data_dir,'LIM_UF.shp'))
    lim_uf=lim_uf.to_crs({'init':'epsg:3857'})
    lim_uf.geometry=lim_uf.simplify(10000)
    lim_uf['x']=lim_uf.apply(getCoords, geom_col="geometry", coord_type="x", axis=1)
    lim_uf['y']=lim_uf.apply(getCoords, geom_col="geometry", coord_type="y", axis=1)
    lim_uf.to_pickle(os.path.join(data_dir,'LIM_UF.pkl'))

from .aux_geo import get_sigla
lim_uf['UF']=lim_uf['NM_ESTADO'].apply(get_sigla)
lim_uf.index=lim_uf['UF']
lim_uf.sort_index(inplace=True)
tabela_UF_df.sort_index(inplace=True)
print(lim_uf.index)
print(tabela_UF_df.index)
### Compute indicadores
indicadores_df=pd.DataFrame(index=tabela_UF_df.index)
indicadores_df['ind_1_1']=tabela_UF_df.iloc[:,1:7].sum(axis=1)/6.0
indicadores_df['ind_1_2']=tabela_UF_df.iloc[:,7]
indicadores_df['ind_2_1']=tabela_UF_df.iloc[:,8]/tabela_UF_df.iloc[:,9]
indicadores_df['ind_2_3']=tabela_UF_df.iloc[:,10]/tabela_UF_df.iloc[:,9]
indicadores_list=list(indicadores_df.columns)
indicadores_df['x']=lim_uf['x'].apply(np.asarray)
indicadores_df['y']=lim_uf['y'].apply(np.asarray)

import operator, functools
### Define Layout

def get_whole_layout( ):
    main_source=ColumnDataSource(data=indicadores_df)
    main_source.add([0]*len(indicadores_df.index),name='indicador_selecionado')
    overview_source=ColumnDataSource()
    overview_source.add(['muito baixo','baixo','médio','alto','muito alto'],name='fatores')
    overview_source.add([0]*5,name='valores')
    detail_source=ColumnDataSource()
    detail_source.add(indicadores_list,name='fatores')
    detail_source.add([0]*len(indicadores_list),name='valores')
    indice_color_mapper= LinearColorMapper(palette=palettes.Greens[9][::-1],low=0,high=1.0)
    plot_width=900
    map_plot_height=900
    widget1=my_plots.select_indicador(indicadores_list)
    plot1=my_plots.mapa(main_source,indice_color_mapper,plot_width,map_plot_height)
    plot2=my_plots.vbar(overview_source)
    plot3=my_plots.vbar_detail(detail_source)
    ### Plots Dynamic functions.
    def update_main_source(attr,old,new):
        update_dict={'indicador_selecionado': np.asarray(indicadores_df[new])}
        main_source.data.update(update_dict)
        return
    def update_overview_source(attr,old,new):
        count,div=np.histogram(indicadores_df[new],bins=5,range=(0,1.0))
        count=count/count.sum()
        update_dict={'valores': count}
        overview_source.data.update(update_dict)
        return
    def update_detail_source(attr,old,new):
        inds_1d = new['1d']['indices']
        if not inds_1d:
            detail=[0]*len(indicadores_list)
            detail_title='Nenhum Estado Selecionado'
        else:
            detail=indicadores_df.loc[:,indicadores_list].iloc[inds_1d]
            print(detail)
            detail_title=functools.reduce(operator.concat,detail.index.tolist())
            detail=detail.mean().tolist()
            print(detail)
        update_dict={'valores': detail}
        plot3.title.text=detail_title
        detail_source.data.update(update_dict)
        return
    widget1.on_change('value',update_main_source)
    widget1.on_change('value',update_overview_source)
    main_source.on_change('selected',update_detail_source)

    ### Get Layout
    from bokeh.layouts import layout,column,row,widgetbox
    whole_layout=layout([
                [plot1],
                [widgetbox(widget1)],
                [plot2],
                [plot3],
            ],
                sizing_mode='fixed',
    )
    return whole_layout
