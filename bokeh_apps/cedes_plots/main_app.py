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
from bokeh.models.widgets import (
    DataTable,
    NumberFormatter,
    TableColumn,
    Select,
    MultiSelect,
    )
# from bokeh import palettes
from . import my_plots

### Load Static Data (No global ColumnDataSource!)
data_dir='../data'
# indicadores_df=pd.read_excel(os.path.join(data_dir,'Tabela-CEDES.xlsx'),'tabela_indicadores')
itens_df=pd.read_excel(os.path.join(data_dir,'dados_rede_cedes.xlsx'),'itens')
itens_df.replace('TRUE',1,inplace=True)
itens_df.replace('FALSE',0,inplace=True)
itens_df.replace('na',np.nan,inplace=True)
itens_df.index=itens_df['UF']
pesquisadores_df=pd.read_excel(os.path.join(data_dir,'dados_rede_cedes.xlsx'),'pesquisadores')
grupos_df=pd.read_excel(os.path.join(data_dir,'dados_rede_cedes.xlsx'),'grupos')
linhas_df=pd.read_excel(os.path.join(data_dir,'dados_rede_cedes.xlsx'),'linhas')
labels_df=pd.read_excel(os.path.join(data_dir,'dados_rede_cedes.xlsx'),'labels')
labels_df.index=labels_df['label_id']
descricao_curta_dict=labels_df['descricao_curta'].to_dict()
paletes_df=pd.read_excel(os.path.join(data_dir,'dados_rede_cedes.xlsx'),'paletes')
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
itens_df.sort_index(inplace=True)
print(lim_uf.index)
print(itens_df.columns)
print(itens_df)
### Compute indicadores
indicadores_df=pd.DataFrame(index=itens_df.index)
metas_df=pd.DataFrame(index=itens_df.index)
# Meta 1
indicadores_df['indicador_1_1']=itens_df.loc[:,['tem_sede','tem_banner','tem_telefone','tem_internet','equip_inf','moveis']].mean(axis=1)
indicadores_df['indicador_1_2']=itens_df.loc[:,['coordenador','coord_adj','apoio_tecnico','bolsistas','repr_pesquisadores','repr_social']].mean(axis=1)
metas_df['meta_1']=indicadores_df.loc[:,['indicador_1_1','indicador_1_2']].mean(axis=1)
# Meta 2
pesquisadores_df['is_phd']=pesquisadores_df['titulacao']=='Doutor(a)'
pesquisadores_df['is_local']=pesquisadores_df['vinculo']=='Pesquisador do Centro'
pesquisadores_df['is_local_phd']=pesquisadores_df['is_local'] & pesquisadores_df['is_phd']
pesquisadores_gr=pesquisadores_df.groupby('UF')
indicadores_df['indicador_2_1']=pesquisadores_gr['is_local_phd'].sum()/pesquisadores_gr['is_local'].sum()
indicadores_df['indicador_2_2']=1-pesquisadores_gr['is_local'].sum()/pesquisadores_gr['nome_bolsistas'].count()
indicadores_df['indicador_2_3']=linhas_df.groupby('UF')['nome_pesquisa'].count()/pesquisadores_gr['is_local'].sum()
metas_df['meta_2']=indicadores_df.loc[:,['indicador_2_1','indicador_2_2','indicador_2_3']].mean(axis=1)

indicadores_list=list(indicadores_df.columns)

indicadores_df.replace(np.nan,0,inplace=True)
indicadores_df['x']=lim_uf['x'].apply(np.asarray)
indicadores_df['y']=lim_uf['y'].apply(np.asarray)
indicadores_df['nome_universidade']=itens_df['nome_universidade']
# indicadores_df.sort_index(ascending=False,inplace=True)

metas_list=list(metas_df.columns)
metas_df.replace(np.nan,0,inplace=True)
metas_df['x']=indicadores_df['x']
metas_df['y']=indicadores_df['y']
# metas_df.sort_index(ascending=False,inplace=True)

import operator, functools
### Define Layout

def get_whole_layout( ):
    ### source definitions
    metas_source=ColumnDataSource(data=metas_df)
    metas_source.add([0]*len(metas_df.index),name='indicador_selecionado')

    indicadores_source=ColumnDataSource(data=indicadores_df)
    indicadores_source.add([0]*len(indicadores_df.index),name='indicador_selecionado')

    overview_metas_source=ColumnDataSource()
    overview_metas_source.add(['0-25','25-50','50-75','75-100'],name='fatores')
    overview_metas_source.add([0]*4,name='valores')

    overview_indicadores_source=ColumnDataSource()
    overview_indicadores_source.add(['0-25','25-50','50-75','75-100'],name='fatores')
    overview_indicadores_source.add([0]*4,name='valores')

    detail_source=ColumnDataSource()
    detail_source.add(indicadores_list,name='fatores')
    detail_source.add([0]*len(indicadores_list),name='valores')

    ### color mappers
    indicadores_cm= LinearColorMapper(palette=paletes_df['amarelo_4'].tolist(),low=0,high=1.0)
    overview_cm= CategoricalColorMapper(palette=paletes_df['amarelo_4'].tolist(),factors=overview_indicadores_source.data['fatores'])

    ### plots definitions
    widget1=Select(
        title="Meta",
        value="meta_1",
        options=[(i,descricao_curta_dict[i]) for i in metas_list]
        )
    plot1a=my_plots.mapa(metas_source,indicadores_cm,700,700)
    plot1b=my_plots.hbar_indicadores(metas_source,indicadores_cm,300,700)

    widget2=Select(
        title="Indicador",
        value="indicador_1_1",
        options=[(i,descricao_curta_dict[i]) for i in indicadores_list]
        )
    plot2a=my_plots.mapa(indicadores_source,indicadores_cm,700,700)
    plot2b=my_plots.hbar_indicadores(indicadores_source,indicadores_cm,300,700)


    plot3a=my_plots.vbar(overview_metas_source,overview_cm,'Meta Selecionada',500,300)
    plot3b=my_plots.vbar(overview_indicadores_source,overview_cm,'Indicador Selecionado',500,300)
    plot4=my_plots.vbar_detail(detail_source,indicadores_cm,1000,300)

    ### dynamic functions definitions
    def update_metas_source(attr,old,new):
        update_dict={'indicador_selecionado': np.asarray(metas_df[new])}
        metas_source.data.update(update_dict)
        return
    def update_indicadores_source(attr,old,new):
        update_dict={'indicador_selecionado': np.asarray(indicadores_df[new])}
        indicadores_source.data.update(update_dict)
        return

    def update_overview_indicadores_source(attr,old,new):
        count,div=np.histogram(indicadores_df[new],bins=4,range=(0,1.0))
        count=count/count.sum()
        update_dict={'valores': count}
        overview_indicadores_source.data.update(update_dict)
        return

    def update_overview_metas_source(attr,old,new):
        count,div=np.histogram(metas_df[new],bins=4,range=(0,1.0))
        count=count/count.sum()
        update_dict={'valores': count}
        overview_metas_source.data.update(update_dict)
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
        plot4.title.text=detail_title
        detail_source.data.update(update_dict)
        return

    ### dynamic interactions
    widget1.on_change('value',update_metas_source)
    widget2.on_change('value',update_indicadores_source)
    widget1.on_change('value',update_overview_metas_source)
    widget2.on_change('value',update_overview_indicadores_source)
    indicadores_source.on_change('selected',update_detail_source)

    #Initialize
    update_metas_source(None,None,'meta_1')
    update_indicadores_source(None,None,'indicador_1_1')
    update_overview_metas_source(None,None,'meta_1')
    update_overview_indicadores_source(None,None,'indicador_1_1')

    ### Get Layout
    from bokeh.layouts import layout,column,row,widgetbox
    whole_layout=layout([
                [widgetbox(widget1)],
                [plot1a,plot1b],
                [widgetbox(widget2)],
                [plot2a,plot2b],
                [plot3a,plot3b],
                [plot4]
            ],
                sizing_mode='fixed',
    )
    return whole_layout
