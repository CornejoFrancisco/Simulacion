import matplotlib.pyplot as plt

def grafico_histograma_frecuencias(vector_fo, nroIntervalos, vector_li_ls):
    fig, ax = plt.subplots()
    ax.hist(vector_fo)
    plt.hist(vector_fo, bins=vector_li_ls, color='blue')
    plt.show()

def prueba_hist():
    dataset = [10,20,30,40,30,20,10]
    fig, ax = plt.subplots()
    ax.hist(dataset, bins=10, color='blue')
    plt.show()
