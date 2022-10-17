from tkinter import RIGHT
from matplotlib.offsetbox import PaddedBox
import matplotlib.pyplot as plt
import numpy as np

def printPlot(etiquetas, valores, varWidth=0.65, **kwargs):
    anchoFigura = 8
    altoFigura = 8
    tituloFigura = ''

    if 'titulo' in kwargs:
        tituloFigura = kwargs['titulo']
    if 'alto' in kwargs:
        altoFigura = kwargs['alto']
    if 'ancho' in kwargs:
        anchoFigura = kwargs['ancho']        

    # creacion del gráfico a mostrar
    fig = plt.figure(figsize=(anchoFigura,altoFigura) ) # constrained_layout=True --> sirve para ajustar al marco
    ax = fig.add_subplot(111)
    
    # grafico de barras horizontales
    ax.barh( etiquetas, valores, varWidth)

    # Settings para que las barras se vean en RGB
    for x,y in zip(etiquetas,valores):
        rgb = np.random.rand(3,)
        ax.barh(x,y,varWidth,color=[rgb])
    
    #plt.bar_label(bars, labels=valores, padding=3)
    ax.xaxis.set_tick_params(labelsize=6, pad = 5)
    ax.yaxis.set_tick_params(labelsize=6, pad = 10)
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    # Cambia el formato de y para que no se muestre en modo cientifico
    current_values = plt.gca().get_xticks()
    plt.gca().set_xticklabels(['{:,.0f}'.format(x) for x in current_values])

    # grilla decorativa
    ax.grid(visible= True, color ='grey',
            linestyle='--', dashes=(5, 5), linewidth = 0.5,
            alpha = 0.2)

    # Invierte el ordenamiento de las provincias
    ax.invert_yaxis()

    ax.set_title(tituloFigura,
                loc ='left',
                size = 12,
                alpha = 0.85 )

    # Ajuste para que la figura no se escape del limite
    fig.subplots_adjust(left=0.18)
    
    # Wattermark
    fig.text(0.88, 0.14, '(c) Pablo Daniel Foglia', fontsize = 12,
            color ='grey', ha ='right', va ='bottom',
            alpha = 0.7)

    # Texto de las barras
    for i in ax.patches:
        plt.text( i.get_width(), i.get_y()+0.5,
                "  " + str(round(i.get_width(), 2)),
                fontsize = 6, fontweight ='regular',
                color ='grey' )

    

    plt.show()