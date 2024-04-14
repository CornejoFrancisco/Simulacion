import plotly.graph_objects as go
from plotly.subplots import make_subplots


def grafico_histograma_frecuencias(vector_fo, minimo, maximo, amplitud, vector_li_ls, tipo_dist):
    marcadores_x = dict(tickvals=vector_li_ls)
    ls = max(maximo, max(vector_li_ls))
    fig = go.Figure(data=go.Histogram(x=vector_fo,
                                      xbins=dict(start=min(vector_li_ls), end=maximo, size=amplitud),
                                      marker=dict(color="lightcoral",
                                                  line=dict(color='black', width=1))
                                      ))
    fig.update_layout(title_text="Histograma de frecuencias de la variable aleatoria con distribucion "
                                 + tipo_dist, title_x=0.5,
                      xaxis_title="Intervalos de frecuencias"
                      )
    fig.update_xaxes(marcadores_x)

    fig.write_html('histograma.html', auto_open=True)


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
    intervalos = list(map(lambda x: x + 1, df.index.values.tolist()))
    data_values = [intervalos] + list(df.transpose().values.tolist())
    header = ["indice nro aleatorio"] + list(df.columns)

    fig = go.Figure(data=go.Table(
        header=dict(values=header),
        cells=dict(values=data_values)
    ))
    fig.update_layout(title_text="Tabla de valores de la variable aleatoria con distribucion "
                                 + tipo_dist, title_x=0.5)
    fig.write_html('tabla_aleatorios.html', auto_open=True)
