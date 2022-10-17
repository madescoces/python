# 2 . Utilizar el algoritmo de Dijkstra para determinar en el grafo ponderado siguiente un camino de longitud mínima 
# entre los vértices Z y A. Construir el grafo.

import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
from dijkstraColor import *
from print import *

import warnings
warnings.filterwarnings('ignore')

fig = plt.figure(1, figsize=(10,8), dpi=72)
grafo = nx.Graph()
nodos = ['A','B','C','D','E','F','G','Z']
pos = {'A':(10,1),'B':(7,0),'C':(3,0),'D':(7,2),'E':(3,2),'F':(3,1),'G':(7,1),'Z':(0,1)}
eWeights = [    ('A','B',4),('A','D',5),('A','G',2),('B','C',5),('B','G',1),('D','E',2),('D','G',1),
                ('Z','E',3),('Z','C',1),('Z','F',2),('C','F',1),('E','F',1) ]

grafo.add_nodes_from(nodos)
grafo.add_edges_from([  ('A','B'),('A','D'),('A','G'),('B','C'),('B','G'),('D','E'),('D','G'),
                        ('Z','E'),('Z','C'),('Z','F'),('C','F'),('E','F')   ])

grafo.add_weighted_edges_from(  
                                eWeights,
                                edge_color='orange'
                            )
def draw():
    nx.draw_networkx( 
                        grafo,
                        pos=pos,
                        node_shape='h',
                        node_size=1000,
                        node_color='orange',
                        edge_color=list(grafo[x][y]['edge_color'] for x,y in grafo.edges()),
                        edgecolors='gray',
                        font_color='snow'
                    )

nx.draw_networkx_edge_labels(
                                grafo,
                                pos=pos,
                                edge_labels = nx.get_edge_attributes( grafo,'weight' ),
                                font_size = 12,
                                font_color = 'gray'
                            )

draw()
print('Grafo original', margin=True)

changeDijkstraPathColor(grafo,nx.algorithms.dijkstra_path( grafo,'Z','A' ))
draw()   
print('Camino más corto entre Z y A', margin=True)
