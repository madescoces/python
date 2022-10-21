import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

from printPlot import *
from prismShape import *

import warnings
warnings.filterwarnings('ignore')

#   Dada la siguiente matriz que determina nodos, pesos y conexiones
#       a   b   c   d   e   t
#   a       12      14
#   b           7   4   11  23
#   c                   2   10
#   d                   6
#   e                       9

# Diseño del plot con plot blanco para dejar espacio para las notas
anotaciones = input('Presentar anotaciones en el gráfico? s/n: ')

if(anotaciones == 's'):
    fig= plt.figure(figsize=(20,10), dpi=72)
    axs= fig.subplots(1, 2, sharex=True, sharey=True,  gridspec_kw={'width_ratios': [1, 1.5]})
else:
    fig= plt.figure(figsize=(12,10), dpi=72)
    axs= fig.add_subplot(1,1,1)

# Asignación de variables para valores, nodos, pesos, etc del grafo
pesos = [   ('a','b',12),('b','c',7),('a','d',14),('b','d',4),('b','e',11),('c','e',2),('d','e',6),
            ('b','t',23),('c','t',10),('e','t',9)   ]

# Clase para el grafo
class Grafo():    
    _G_ = nx.Graph()        # objeto grafo de librería networx
    _pos_ = dict()          # diccionario de posiciones
    _pesos_ = list()        # lista de pesos de arista

    def __init__(self, pesos_: list(), **kwargs):
        self._pesos_ = pesos_       # atributo obligatorio 
        if (('diGraph' in kwargs) and kwargs['diGraph']==True):
            self._G_ = nx.DiGraph() # si deseo representar un digrafo uso este keyarg

    # Get de el objeto grafo
    def get_grafo(self):
        return self._G_

    # dibuja el grafo
    def draw(self, **kwargs):        
        self.edgesAndWeight()   # Settins de los pesos de arista
        self._pos_ = nx.shell_layout(self._G_) if not 'layout' in kwargs else kwargs['layout']  # Tipo de layout
        # Dibuja los nodos
        nx.draw_networkx_nodes  (
                                    self._G_,
                                    pos= self._pos_,
                                    node_shape= 'o' if not 'shape' in kwargs else kwargs['shape'],
                                    node_size= 1500 if not 'size' in kwargs else kwargs['size'],
                                    node_color= 'orange' if not 'color' in kwargs else kwargs['color'], 
                                    edgecolors= 'gray'                              
                                )
        # Dibuja las etiquetas
        nx.draw_networkx_labels (
                                    self._G_,
                                    pos= self._pos_,
                                    font_size = 10 if not 'font_size' in kwargs else kwargs['font_size'],                     
                                    font_weight= 'regular' if not 'font_weight' in kwargs else kwargs['font_weight'],                     
                                    font_color= 'snow' if not 'n_font_color' in kwargs else kwargs['n_font_color']
                                )
        # Diguja las aristas
        nx.draw_networkx_edges  (
                                    self._G_,
                                    pos= self._pos_,
                                    node_size= 1500 if not 'size' in kwargs else kwargs['size'],
                                    edge_color= list(self._G_[x][y]['edge_color'] for x,y in self._G_.edges()),
                                    connectionstyle='arc3, rad = 0.05',
                                    arrowstyle= '-|>',
                                    arrowsize= 15
                                )
        # Dibuja las etiquetas de las aristas
        nx.draw_networkx_edge_labels    (
                                            self._G_,
                                            pos= self._pos_,
                                            edge_labels = nx.get_edge_attributes( self._G_,'weight' ),
                                            font_size = 12 if not 'e_font_size' in kwargs else kwargs['e_font_size'],
                                            font_color = 'gray' if not 'e_font_color' in kwargs else kwargs['n_font_color'],
                                            label_pos= 0.25 if not 'label_pos' in kwargs else kwargs['label_pos']
                                        )
    #Genera los pesos de las aristas
    def edgesAndWeight(self, **kwargs):
        self._G_.add_weighted_edges_from    (
                                                self._pesos_,
                                                edge_color='orange' if not 'e_color' in kwargs else kwargs['e_color']
                                            )    
    # Impresión de listas en modo más legible
    def listaPrint(self, func, **kwargs):
        texto = ''
        for i, node in enumerate(func):
            if( i < len(func)-1):
                texto += node + ', ' if not 'sep' in kwargs else kwargs['sep']
            else:
                texto += node
        return texto

    # Impresión de pares de datos en modo más legible
    def tuplePrint(self, func, **kwargs):
        texto = ''
        sep = ',' if not 'sep' in kwargs else kwargs['sep']

        for i, x in enumerate(func):
            if( i < len(func)-1):
                texto += '(' + str(x[0]) + sep + str(x[1]) + ')' + ', '  
            else:
                texto += '(' + str(x[0]) + sep + str(x[1]) + ')'   
        return texto
    
    # Genera la matriz de incidencia del grafo
    def matrizIncidencia(self):
        I =  nx.incidence_matrix(self._G_, np.sort(list(self._G_.nodes())), weight='none')
        return I.todense()
    
    # Genera la matriz de adyacencia del grafo, con y sin pesos, en caso del grafo ser = nx.Graph() la misma se imprime simétrica, para imprimir una matriz asimetrica usar nx.Digraph
    def matrizAdyacencia(self, **kwargs):
        A = nx.adjacency_matrix(self._G_, np.sort(list(self._G_.nodes())), weight='weight' if not 'weight' in kwargs else kwargs['weight'])
        return A.todense()

    # Pesos de las aristas que llegan a un nodo
    def valoresAristaDelNodo(self, nodo):
        nodosC = {}
        for key,value in zip(self._G_[nodo],self._G_[nodo].values()):
            nodosC[key] = value['weight']
        return nodosC

    def pathMasCorto(self, origen, **kwargs):
        try: 
            path = nx.algorithms.shortest_path(self._G_, origen, weight='weight' if not 'weight' in kwargs else kwargs['weight'])
            return path
                    
        except nx.NetworkXAlgorithmError:
            print(f'\nNo existe ruta posible desde el {origen} hacia otros nodos')
    
    def pathMasCortoLength(self, origen, **kwargs):
        try: 
            path = nx.algorithms.shortest_path_length(self._G_, origen, weight='weight' if not 'weight' in kwargs else kwargs['weight'])
            return path
                    
        except nx.NetworkXAlgorithmError:
            print(f'\nNo existe ruta posible desde el {origen} hacia otros nodos')

    def promFloydW(self, **kwargs):
        try: 
            prom = nx.algorithms.average_shortest_path_length(self._G_, method="floyd-warshall", weight='weight' if not 'weight' in kwargs else kwargs['weight'])
            return prom
                    
        except nx.NetworkXAlgorithmError:
            print(f'\nError al procesar el promedio')

    def dijkstra_path(self, origen, destino):
        try: 
            path = nx.algorithms.dijkstra_path(self._G_, origen, destino)
            return path
                    
        except nx.NetworkXAlgorithmError:
            print(f'\nNo existe ruta posible entre {origen} y {destino}')

    def dijkstra_path_length(self, origen, destino):
        try: 
            len = nx.algorithms.dijkstra_path_length(self._G_, origen, destino)
            return len
                    
        except nx.NetworkXAlgorithmError:
            print(f'\nNo existe ruta posible entre {origen} y {destino}')

    def single_source_dijkstra_path_length(self, origen):
        try: 
            len = nx.algorithms.single_source_dijkstra_path_length(self._G_, origen)
            return len
                    
        except nx.NetworkXAlgorithmError:
            print(f'\nPosiblemente {origen} no tenga aristas')
    
    def radio(self):
        try:
            radio = nx.radius(self._G_)
            return radio
        
        except nx.NetworkXException as e:
            print(f"Imposible calcular el radio, motivo: {e}")
    
    def diametro(self):
        try:    
           diam = nx.diameter(self._G_)
           return diam

        except nx.NetworkXException as e:
            print(f"Imposible calcular el diámetro, motivo: {e}")

    def excentricidad(self):
        try:
            ecc = nx.eccentricity(self._G_)
            return ecc

        except nx.NetworkXException as e:
            print(f"Imposible calcular excentricidad, motivo: {e}")
    
    def centro(self):
        try:
            centro = nx.center(self._G_)
            return centro

        except nx.NetworkXException as e:
            print(f"Imposible calcular el centro, motivo: {e}")
    
    def periferia(self):
        try:
            per = self.listaPrint(nx.periphery(self._G_))
            return per

        except nx.NetworkXException as e:
            print(f"Imposible calcular periferia, motivo: {e}")
    
    def densidad(self):
        try:
            den = nx.density(self._G_)
            return den
    
        except nx.NetworkXException as e:
            print(f"Imposible calcular densidad, motivo: {e}")

# Dibujo sin dirección
G = Grafo(pesos)
G.draw(shape='h')

# Notas del Plot con los valores solicitados solo se imprime si es requerido.
box= fs= xstart= ystart= step= 0
if(anotaciones == 's'):
    fs = 12             # font_size
    xstart = -3.8       # valor de inicio anotaciones
    ystart = 1          # altura de inicio anotaciones
    step = -0.092       # step de salto entre anotaciones
    box = 'true'        # solo en consola True, consola 
                
squareText("Número de Nodos: ", G.get_grafo().number_of_nodes(), box, size=fs, y=ystart + step*0, x=xstart)
squareText("Nodos: ", G.listaPrint(G.get_grafo().nodes()), box, size=fs, y=ystart + step*1, x=xstart)
squareText("Número de Enlaces: ", G.get_grafo().number_of_edges(), box, size=fs, y=ystart + step*2, x=xstart)
squareText("Enlaces: ", G.tuplePrint(G.get_grafo().edges()), box, size=fs, y=ystart + step*3, x=xstart)
squareText("Vecinos de b: ", G.listaPrint(list(G.get_grafo().neighbors('b'))), box, size=fs, y=ystart + step*4, x=xstart)
squareText("Aristas de cada nodo: ", G.tuplePrint(G.get_grafo().degree(), sep='= '),box, size=fs, y=ystart + step*5, x=xstart)
squareText("Aristas en modo Dicionario: ", dict(G.get_grafo().degree()),box, size=fs, y=ystart + step*6, x=xstart)
squareText("Matriz de adyacencia: \n", G.matrizAdyacencia(), box, size=fs, y=ystart + step*7.17, x=xstart, font_family='monospace')
squareText("Matriz de incidencia: \n", G.matrizIncidencia(), box, size=fs, y=ystart + step*7.17, x=xstart+0.68, font_family='monospace')
squareText("Valores de enlace nodo c: ",G.valoresAristaDelNodo('c'), box, size=fs, y=ystart + step*12, x=xstart)
squareText("Valor de la relación entre (b, e): ", G.get_grafo()['b']['e']['weight'], box, size=fs, y=ystart + step*13, x=xstart)
squareText("Ruta más corta desde a -> todos: ", G.pathMasCorto('a', weight='none'), box, size=fs, y=ystart + step*14, x=xstart)
squareText("Longitud de la ruta entre a -> todos: ", G.pathMasCortoLength('a', weight='none'), box, size=fs, y=ystart + step*15, x=xstart)
squareText("Promedio de la ruta mas corta Floyd-Warshall: ", G.promFloydW(weight='none'),box, size=fs, y=ystart + step*16, x=xstart)
squareText("Ruta más corta entre a y t usando Dijkstra: ", G.dijkstra_path('a','t'), box, size=fs, y=ystart + step*17, x=xstart)
squareText("Longitud de la ruta entre a y t usando Dijkstra: ", G.dijkstra_path_length('a','t'), box, size=fs, y=ystart + step*18, x=xstart)
squareText("Longitud de Ruta ponderada más corta 'c': ", G.single_source_dijkstra_path_length('c'), box, size=fs, y=ystart + step*19, x=xstart )
squareText("Radio: ", G.radio(), box, size=fs, y=ystart + step*20, x=xstart)
squareText("Diámetro: ", G.diametro(), box, size=fs, y=ystart + step*20, x=xstart + 0.35)
squareText("Excentricidad: ", G.excentricidad(), box, size=fs, y=ystart + step*21, x=xstart)
squareText("Centro: ", G.centro(), box, size=fs, y=ystart + step*20, x=xstart + 0.82)
squareText("Periferia: ", G.periferia(), box, size=fs, y=ystart+step*22, x=xstart)
squareText("Densidad: ", G.densidad(), box, size=fs, y=ystart+step*23, x=xstart)

printPlot('Grafo sin dirección', fig) 

# Dibujo Dirigido
if(input('Desea ver el dibujo dirigido s/n: ')=='s'):
    fig2= plt.figure(figsize=(12,10), dpi=72)
    ax2 = fig2.add_subplot(1,1,1)
    myGrafoDirigido = Grafo(pesos, diGraph=True)
    myGrafoDirigido.draw()

    printPlot('Grafo Direcionado',fig2)


# Expresiones Regulares
import re 

class Regulares():
    txt= reg= ""
    def __init__(self, reg_, txt_):
        self.txt= txt_
        self.reg= reg_

    def printAllReg(self):
        print(self.reg)
        return print(re.findall(self.reg,self.txt))


    def printReg(self):
        return print(re.match(self.reg,self.txt))


texto = """ 98.140.180.244 - harber4797 [21/Jun/2019:16:01:53 -0700] "POST /seize/b2b/synergistic HTTP/2.0" 203 9396
229.231.201.185 - - [21/Jun/2019:16:01:35 -0700] "HEAD /supply-chains/brand/strategic HTTP/1.1" 405 28109
197.150.196.204 - thiel4558 [21/Jun/2019:16:01:05 -0700] "PATCH /compelling HTTP/2.0" 500 14180 """
exp = r'[A-Z]{1,}\s\/*.*\d\.\d'

regex = Regulares(exp,texto)
regex.printAllReg()