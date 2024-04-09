import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def grafico_histograma_frecuencias(vector_fo, nroIntervalos, minimo, maximo, amplitud, vector_li_ls):
    fig = px.histogram(vector_fo)
    fig.update_traces(xbins=dict(start=minimo, end=maximo, size=amplitud))
    fig.update_xaxes(tickvals=vector_li_ls)
    fig.show()

def table(df):
    fig = go.Figure(data=go.Table(
        header = dict(values=list(df.columns)),
        cells=dict(values=df.transpose().values.tolist())
    ))
    fig.show()


