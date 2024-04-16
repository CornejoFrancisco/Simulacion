from decimal import Decimal, ROUND_HALF_UP

import plotly.graph_objects as go
import plotly.express as px
from Tools.demo import vector

from scripts.soporte import *
from plotly.subplots import make_subplots

def grafico_histograma_frecuencias(tipo_dist, vector_li_ls, vector_fo):

    print(vector_li_ls)
    fig = go.Figure(data=go.Bar(
                            x=vector_li_ls,
                            y=vector_fo,

                            marker=dict(color="lightcoral",
                                        line=dict(color='black', width=1))
                            ))
    fig.update_layout(title_text="Histograma de frecuencias de la variable aleatoria con distribucion "
                                 + tipo_dist, title_x=0.5,
                      xaxis_title="Intervalos de frecuencias",
                      yaxis_title="Frecuencias observadas",
                      xaxis=dict(tickfont=dict(size=10)),
                      bargap=0.0)
    fig.write_html('graficos.html', auto_open=True)
    """print(vector_li_ls)
    marcadores_x = dict(tickvals=vector_li_ls)

    max_i = vector_nros.index(max(vector_nros))
    vector_nros[max_i] = max(vector_nros) - 0.0001

    fig = go.Figure(data=go.Histogram(x=vector_nros,
                                      xbins=dict(start=min(vector_li_ls), end=max(vector_li_ls), size=amplitud),
                                      marker=dict(color="lightcoral",
                                                  line=dict(color='black', width=1))
                                      ))
    print(redondeo_vector_text(vector_li_ls))
    fig.update_layout(title_text="Histograma de frecuencias de la variable aleatoria con distribucion "
                                 + tipo_dist, title_x=0.5,
                      xaxis_title="Intervalos de frecuencias",
                      xaxis=dict(
                          ticktext=redondeo_vector_text(vector_li_ls))
                      )
    fig.update_xaxes(marcadores_x)
    fig.write_html('histograma.html', auto_open=True)"""


def tabla(df, tipo_dist):
    data_values = df.transpose().values.tolist()
    header = list(df.columns)

    fig = go.Figure(data=go.Table(
        header=dict(values=header),
        cells=dict(values=data_values)
    ))

    fig.update_layout(title_text="Tabla de frecuencias y prueba ji cuadrado "
                                 + tipo_dist, title_x=0.5)
    fig.write_html('tabla ji_cuadrado.html', auto_open=True)


"""def table_frecuencias(df, tipo_dist):
    intervalos = list(map(lambda x: x+1, list(df.index.values)))
    data_values = [intervalos] + df.transpose().values.tolist()
    header = ["Intervalo"] + list(df.columns)

    fig = go.Figure(data=go.Table(
        header=dict(values=header),
        cells=dict(values=data_values,)
    ))
    fig.update_layout(title_text="Tabla de frecuencias de la variable aleatoria con distribucion "
                                 + tipo_dist, title_x=0.5)
    fig.write_html('tabla_frecuencias.html', auto_open=True)"""

"""def tabla_fre_acum(df, tipo_dist):
    intervalos = list(map(lambda x: x+1, list(df.index.values)))
    data_values = [intervalos] + df.transpose().values.tolist()
    header = ["Nro Intervalo"] + list(df.columns)

    fig = go.Figure(data=go.Table(
        header=dict(values=header),
        cells=dict(values=data_values)
    ))
    fig.update_layout(title_text="Tabla de frecuencias agrupadas de la variable aleatoria con distribucion "
                                 + tipo_dist, title_x=0.5)
    fig.write_html('tabla_frecuencias_acum.html', auto_open=True)"""


def tabla_nros_aleatorios(df, tipo_dist):
    indice = list(map(lambda x: x + 1, df.index.values.tolist()))
    data_values = [indice] + list(df.transpose().values.tolist())
    header = ["indice nro aleatorio"] + list(df.columns)

    fig = go.Figure(data=go.Table(
        header=dict(values=header),
        cells=dict(values=data_values)
    ))
    fig.update_layout(title_text="Tabla de valores de la variable aleatoria con distribucion "
                                 + tipo_dist, title_x=0.5)
    fig.write_html('tabla_aleatorios.html', auto_open=True)
