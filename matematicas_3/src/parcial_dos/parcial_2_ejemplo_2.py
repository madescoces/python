import re
import networkx as nx
from matplotlib import pyplot as plt
import numpy as np
from printPlot import *

import warnings
warnings.filterwarnings('ignore')

"""
    A   B   C   D   E   F   G
A               6       2
B   5               12      1
C           4
D                           2
E           6
F   9
G
"""
fig = plt.figure(figsize=(12,8), dpi=72)
ax = fig.subplots(1, 2, sharex=True, sharey=True,  gridspec_kw={'width_ratios': [1, 4]})

pesos = [   ('A','D',6),('A','F',2),('B','A',5),('B','E',12),('B','G',1),
            ('C','C',4),('D','G',2),('E','C',6),('F','A',9) ]

class Grafo():    
    _G_ = nx.Graph()
    _pos_ = dict()
    _pesos_ = list()
    
    def __init__(self, pesos_: list(), **kwargs):
        self._pesos_ = pesos_  
        if (('diGraph' in kwargs) and kwargs['diGraph']==True):
            self._G_ = nx.DiGraph()
    
    def get_grafo(self):
        return self._G_
    
    def draw(self, **kwargs):        
        self.edgesAndWeight()
        self._pos_ = nx.shell_layout(self._G_)
        nx.draw_networkx_nodes  (
                                    self._G_,
                                    pos= self._pos_,
                                    node_shape= 'o' if not 'shape' in kwargs else kwargs['shape'],
                                    node_size= 1000 if not 'size' in kwargs else kwargs['size'],
                                    node_color= 'orange' if not 'color' in kwargs else kwargs['color'], 
                                    edgecolors= 'gray'                              
                                )
        
        nx.draw_networkx_labels (
                                    self._G_,
                                    pos= self._pos_,
                                    font_size = 10 if not 'font_size' in kwargs else kwargs['font_size'],                     
                                    font_weight= 'regular' if not 'font_weight' in kwargs else kwargs['font_weight'],                     
                                    font_color= 'snow' if not 'n_font_color' in kwargs else kwargs['n_font_color']
                                )

        nx.draw_networkx_edges  (
                                    self._G_,
                                    pos= self._pos_,
                                    node_size= 1000 if not 'size' in kwargs else kwargs['size'],
                                    edge_color= list(self._G_[x][y]['edge_color'] for x,y in self._G_.edges()),
                                    connectionstyle='arc3, rad = 0.05',
                                    arrowstyle= '-|>',
                                    arrowsize= 15
                                )
        
        nx.draw_networkx_edge_labels    (
                                            self._G_,
                                            pos= self._pos_,
                                            edge_labels = nx.get_edge_attributes( self._G_,'weight' ),
                                            font_size = 12 if not 'e_font_size' in kwargs else kwargs['e_font_size'],
                                            font_color = 'gray' if not 'e_font_color' in kwargs else kwargs['n_font_color'],
                                            label_pos= 0.25 if not 'label_pos' in kwargs else kwargs['label_pos']
                                        )

    def edgesAndWeight(self, **kwargs):
        self._G_.add_weighted_edges_from    (
                                                self._pesos_,
                                                edge_color='orange' if not 'e_color' in kwargs else kwargs['e_color']
                                            )

    def matrizIncidencia(self):
        I =  nx.incidence_matrix(self._G_, np.sort(list(self._G_.nodes())), weight='none')
        return print(f"\nLa matriz de incidencia del grafo:\n {I.todense()}")

    def matrizAdjacencia(self):
        A = nx.adjacency_matrix(self._G_, np.sort(list(self._G_.nodes())), weight='weight')
        return print(f"\nLa matriz de adjacencia del grafo:\n {A.todense()}")

    def dijkstra_path(self, origen, destino):
        try: 
            nx.algorithms.dijkstra_path(self._G_, origen, destino)
            print(f"\nRuta ponderada más corta entre {origen} y {destino} es: {nx.algorithms.dijkstra_path(myGrafo.get_grafo(),origen,destino)}")
                    
        except nx.NetworkXAlgorithmError:
            print(f'\nNo existe ruta posible entre {origen} y {destino}')
    
    def radio(self):
        try:
            print(f"\nRadio del grafo: {nx.radius(self._G_)}")
        
        except nx.NetworkXException as e:
            print(f"Imposible calcular el radio, motivo: {e}")
    
    def diametro(self):
        try:    
           print(f"\nDiámetro del grafo: {nx.diameter(self._G_)}")

        except nx.NetworkXException as e:
            print(f"Imposible calcular el diámetro, motivo: {e}")

    def excentricidad(self):
        try:
            print(f"\nExcentricidad del grafo: {nx.eccentricity(self._G_)}")

        except nx.NetworkXException as e:
            print(f"Imposible calcular excentricidad, motivo: {e}")
    
    def centro(self):
        try:
            print(f"\nCentro del grafo: {nx.center(self._G_)}")

        except nx.NetworkXException as e:
            print(f"Imposible calcular el centro, motivo: {e}")
    
    def periferia(self):
        try:
            print(f"\nPeriferia del grafo: {nx.periphery(self._G_)}")

        except nx.NetworkXException as e:
            print(f"Imposible calcular periferia, motivo: {e}")
    
    def densidad(self):
        try:
            print(f"\nDensidad del grafo: {nx.density(self._G_)}")
    
        except nx.NetworkXException as e:
            print(f"Imposible calcular densidad, motivo: {e}")



# Genero una instancia de la clase grafo
myGrafo = Grafo(pesos)
myGrafo.draw()
printPlot('Grafo sin dirección',fig)

print(f"\nVecinos de 'C': {list(myGrafo.get_grafo().neighbors('C'))}")
myGrafo.matrizIncidencia()
myGrafo.matrizAdjacencia()
myGrafo.dijkstra_path('D','F')
myGrafo.radio()
myGrafo.diametro()
myGrafo.excentricidad()
myGrafo.centro()
myGrafo.periferia()
myGrafo.densidad()

# Dibujo Dirigido
fig2 = plt.figure(figsize=(12,8), dpi=72)
ax2 = fig2.subplots(1, 2, sharex=True, sharey=True,  gridspec_kw={'width_ratios': [1, 4]})

myGrafoDirigido = Grafo(pesos, diGraph=True)
myGrafoDirigido.draw()

printPlot('Grafo Direcionado',fig2)


#extraer los nombres de las ciudades:
texto = """ "3475","3592","Male","52","GBR","217.4833333","Regular"
            "13594","13853","Female","40","NY","272.55","Regular"
            "12012","12256","Male","31","FRA","265.2833333","Regular"
            "10236","10457","Female","33","MI","256.15","Regular"
            "9476","9686","Male","33","NY","252.25","Regular"
            "1720","1784","Male","40","NJ","201.9666667","Regular"
            "15736","16020","Female","30","CA","283.5666667","Regular" """

# Encuentra el primer encuentro
# print(re.search(r'\D',texto))

# Lista con los nombres de las ciudades:
print()
print(re.findall(r'[A-Z]{2,3}',texto))