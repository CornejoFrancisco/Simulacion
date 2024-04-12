import plotly.graph_objects as go


def grafico_histograma_frecuencias(vector_fo, minimo, maximo, amplitud, vector_li_ls):
    histograma = go.Histogram(x=vector_fo, xbins=dict(start=minimo, end=maximo, size=amplitud))
    marcadores_x = dict(tickvals=vector_li_ls)
    fig = go.Figure(histograma)
    fig.update_xaxes(marcadores_x)
    """fig = px.histogram(vector_fo)
    fig.update_traces(xbins=dict(start=minimo, end=maximo, size=amplitud))"""
    fig.write_html('histograma.html', auto_open=True)

def table_frecuencias(df):
    fig = go.Figure(data=go.Table(
        header=dict(values=list(df.columns)),
        cells=dict(values=df.transpose().values.tolist())
    ))
    fig.write_html('tabla_frecuencias.html', auto_open=True)

def tabla_nros_aleatorios(df, distr):
    fig = go.Figure(data=go.Table(
        header=dict(values=list(df.columns)),
        cells=dict(values=df.transpose().values.tolist())
    ))
    fig.write_html('tabla_aleatorios.html', auto_open=True)



