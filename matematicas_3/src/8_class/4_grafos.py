import numpy as np
import networkx as nx
from matplotlib import pyplot as plt
from printPlot import *
from dijkstraColor import *
from prismShape import *

# Solamente para que no salgan los warnings. no se de que pero bue...
import warnings
warnings.filterwarnings('ignore')

grafo = nx.Graph()
nodos = list(map(chr, np.arange(97, 105)))
pos = prismShape(nodos, lines=3)

eWeights = [    ('a','b',6),('a','e',9),('e','f',3),('f','d',10),('b','c',12),('f','g',3),('f','h',2)  ]

grafo.add_nodes_from(nodos)

grafo.add_weighted_edges_from   (
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
printPlot('Cantidad de combustible entre poblaciones: ', margin=True)