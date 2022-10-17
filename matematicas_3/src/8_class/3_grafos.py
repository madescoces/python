import networkx as nx
import numpy as np
from matplotlib import pyplot as plt
from prismShape import *
from print import *
from dijkstraColor import *

# Solamente para que no salgan los warnings. no se de que pero bue...
import warnings
warnings.filterwarnings('ignore')

fig = plt.figure(figsize=(10,8), dpi=72)

#Generación del grafo vacío.
grafo = nx.Graph()
nodos = list(map(chr, np.arange(97, 111)))
pos = prismShape(nodos)
eWeights = [    ('a','b',6),('a','c',9),('a','d',3),('b','c',10),('b','e',12),('c','e',3),('c','f',2),
                ('c','d',4),('d','f',15),('d','g',10),('e','f',8),('e','h',4),('e','i',11),('f','g',9),
                ('f','i',10),('g','j',13),('h','i',7),('h','k',20),('h','l',11),('i','l',11),('i','j',15),
                ('j','l',11),('j','m',9),('k','l',13),('k','n',6),('l','m',5),('l','n',12),('m','n',5)  ]

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


start = 1.25
squareText("Radio:", nx.radius(grafo),x=-0.5,y=start)
squareText("Diámetro:", nx.diameter(grafo),x=-0.5,y=start-0.15)
squareText("Centro:", nx.center(grafo),x=-0.5,y=start-0.15*2)
squareText("Periferia:", nx.periphery(grafo),x=-0.5,y=start-0.15*3)
squareText("Densidad:", nx.density(grafo),x=-0.5,y=start-0.15*4)
squareText("Excentricidad:", nx.eccentricity(grafo),x=-0.5,y=start-0.15*5)
print('Costos en miles de dólares entre nodos', margin=True)

changeDijkstraPathColor(grafo,nx.algorithms.dijkstra_path( grafo,'n','a' ))
squareText("Costo total en USD: ", sumDijkstraPath(grafo,nx.algorithms.dijkstra_path( grafo,'n','a' ))*1000,x=-0.5,y=0.75)
draw()   
print('Red más económica entre los nodos (A,N)', margin=True)