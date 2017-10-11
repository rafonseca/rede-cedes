import pandas as pd
import numpy as np
from bokeh.models import (
    ColumnDataSource,
    )
def make_treemap(meta):
    meta=pd.Series(meta)
    meta/=meta.sum()
    x0=0.0
    x1=1.0
    y0=0.0
    y1=1.0
    l_left=[]
    l_right=[]
    l_top=[]
    l_bottom=[]
    for i,area in enumerate(meta):
        if (i % 2)==0:
            left=x0
            top=y1
            bottom=y0
            #area=(y1-y0)*(x1-x0) => x1=x0+area/(y1-y0)
            x0+=area/(y1-y0)
            right=x0
        else:
            left=x0
            top=y1
            right=x1
            y1-=area/(x1-x0)
            bottom=y1
        l_left.append(left)
        l_right.append(right)
        l_top.append(top)
        l_bottom.append(round(bottom,10))
    return dict(left=l_left, right=l_right, top=l_top, bottom=l_bottom)

def cartesian2polar(vector):
    nb_factors=len(vector)
    angle_step=2*np.pi/nb_factors
    angle_step_vector=angle_step*np.arange(nb_factors)
    complex_coord=np.exp(1j*angle_step_vector)*vector
    xs=np.real(complex_coord)
    ys=np.imag(complex_coord)
    return pd.Series({'xs': xs.tolist(), 'ys': ys.tolist()})


def make_radar_chart(source_df):
    radar_source_df=source_df.apply(cartesian2polar,axis=1)
    return radar_source_df

def vbar(source_detalhe_indicadores,plot_width):
    barras=figure(
        plot_height=300,
        plot_width=plot_width,
        tools='',
        x_range=bokeh.models.ranges.FactorRange(factors=source_detalhe_indicadores.data['fatores']),
        y_range=Range1d(0.0,1.0)
    )

    barras.vbar(
        x='fatores',
        width=0.5,
        top='valores',
        source=source_detalhe_indicadores,
        # fill_color={'field': 'valores', 'transform': indice_color_mapper},
        line_color=None,
    )
    barras.toolbar.logo=None
    barras.toolbar_location='above'
    barras.toolbar_sticky=False
    return barras
