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
fig= plt.figure(figsize=(20,10), dpi=72)
axs= fig.subplots(1, 2, sharex=True, sharey=True,  gridspec_kw={'width_ratios': [1, 1.5]})

# Asignación de variables para valores, nodos, pesos, etc del grafo
G = nx.Graph()
nodos = list(map(chr,np.arange(97,102))) + list(chr(116))
pos = prismShape(nodos)
eWeights = [    ('a','b',12),('b','c',7),('a','d',14),('b','d',4),('b','e',11),('c','e',2),('d','e',6),
                ('b','t',23),('c','t',10),('e','t',9)   ]

# Configuración del grafo para dibujado
def draw(grafo, pos_, pesos, **kwargs):  
    grafo.add_nodes_from(nodos) 

    grafo.add_weighted_edges_from   (
                                        pesos,
                                        edge_color='orange' if not 'e_color' in kwargs else kwargs['e_color']
                                    )
    nx.draw_networkx(
                        grafo,
                        pos= pos_,
                        node_shape= 'h',
                        node_size= 2000 if not 'size' in kwargs else kwargs['size'],
                        node_color= 'orange' if not 'color' in kwargs else kwargs['color'],
                        edge_color= list(grafo[x][y]['edge_color'] for x,y in grafo.edges()),
                        edgecolors= 'gray',
                        font_color= 'snow' if not 'n_font_color' in kwargs else kwargs['n_font_color'],
    )

    nx.draw_networkx_edge_labels(
                                grafo,
                                pos= pos_,
                                edge_labels = nx.get_edge_attributes( grafo,'weight' ),
                                font_size = 12 if not 'e_font_size' in kwargs else kwargs['e_font_size'],
                                font_color = 'gray' if not 'e_font_color' in kwargs else kwargs['n_font_color']
                            )

draw(G, pos, eWeights)

# Notas del Plot con los valores solicitados
fs = 12
xstart = -2.5
ystart = 2
step = -0.095
squareText("Número de Nodos: ", G.number_of_nodes(), size=fs, y=ystart+step*0, x=xstart)
squareText("Nodos: ", G.nodes(), size=fs, y=ystart+step*1, x=xstart)
squareText("Número de Enlaces: ", G.number_of_edges(), size=fs, y=ystart+step*2, x=xstart)
squareText("Enlaces: ", G.edges(), size=fs, y=ystart+step*3, x=xstart)
squareText("Vecinos de b: ", list(G.neighbors('b')), size=fs, y=ystart+step*4, x=xstart)
squareText("Aristas de cada nodo: ", G.degree(), size=fs, y=ystart+step*5, x=xstart)
squareText("Aristas en modo Dicionario: ", dict(G.degree()), size=fs, y=ystart+step*6, x=xstart)
squareText("Matriz de adyacencia: \n", nx.adjacency_matrix(G).todense(), size=fs, y=ystart+step*7.1, x=xstart, font_family='monospace')
squareText("Matriz de incidencia: \n", nx.incidence_matrix(G).todense(), size=fs, y=ystart+step*7.1, x=xstart+0.95, font_family='monospace')

nodosC = {}
for key,value in zip(G['c'],G['c'].values()):
    nodosC[key] = value['weight']
    
squareText("Valores de enlace nodo c: ", nodosC, size=fs, y=ystart+step*12, x=xstart)
squareText("Valores relación nodo b con e: ", G['b']['e']['weight'], size=fs, y=ystart+step*13, x=xstart)
squareText("Ruta más corta desde a hacia cualquier nodo: ", nx.algorithms.shortest_path(G, 'a', weight='weight'), size=fs, y=ystart+step*14, x=xstart)
squareText("Longitud de la ruta entre a: ", nx.shortest_path_length(G, 'a', weight='weight'), size=fs, y=ystart+step*15, x=xstart)
squareText("Promedio de la ruta mas corta usando Floyd-Warshall: ", nx.algorithms.average_shortest_path_length(G, weight='weight' ,method="floyd-warshall"),size=fs, y=ystart+step*16, x=xstart)
squareText("Ruta más corta entre a y t usando Dijkstra: ", nx.dijkstra_path(G,'a','t'), size=fs, y=ystart+step*17, x=xstart)
squareText("Longitud de la ruta entre a y t usando Dijkstra: ", nx.dijkstra_path_length(G,'a','t'), size=fs, y=ystart+step*18, x=xstart)
squareText("Longitud de Ruta ponderada más corta desde el nodo c:", nx.single_source_dijkstra_path_length(G,'c'), size=fs, y=ystart+step*19, x=xstart )
squareText("Radio: ", nx.radius(G), size=fs, y=ystart+step*20, x=xstart)
squareText("Diámetro: ", nx.diameter(G), size=fs, y=ystart+step*20, x=xstart+0.35)
squareText("Excentricidad: ", nx.eccentricity(G), size=fs, y=ystart+step*21, x=xstart)
squareText("Centro: ", nx.center(G), size=fs, y=ystart+step*20, x=xstart+0.82)
squareText("Periferia: ", nx.periphery(G), size=fs, y=ystart+step*22, x=xstart)
squareText("Densidad: ", nx.density(G), size=fs, y=ystart+step*23, x=xstart)
printPlot('Grafo Parcial: ', fig, margin=(0.01,0.01))


# Redibujado del grafo en forma dirigida
fig2= plt.figure(figsize=(12,10), dpi=72)
axs2= fig2.add_subplot(1,1,1)

H = G.to_directed()
draw(H, pos, eWeights)
printPlot('Grafo dirigido: ', fig2, margin=(0.01,0.01))

# print de consignas por consola:
print(f"Número de Nodos: {G.number_of_nodes()}")
print(f"Nodos: {G.nodes()}") 
print(f"Número de Enlaces: {G.number_of_edges()}")
print(f"Enlaces: {G.edges()}") 
print(f"Vecinos de b: {list(G.neighbors('b'))}")
print(f"Aristas de cada nodo: {G.degree()}")
print(f"Aristas en modo Dicionario: {dict(G.degree())}")
print(f"Matriz de adyacencia: \n{nx.adjacency_matrix(G).todense()}")
print(f"Matriz de incidencia: \n{nx.incidence_matrix(G).todense()}")
print(f"Valores de enlace nodo c: {nodosC}")
print(f"Valores relación nodo b con e: {G['b']['e']['weight']}")
print(f"Ruta más corta desde a hacia cualquier nodo: {nx.algorithms.shortest_path(G, 'a', weight='weight')}")
print(f"Longitud de la ruta entre a: {nx.shortest_path_length(G, 'a', weight='weight')}")
print(f"Promedio de la ruta mas corta usando Floyd-Warshall: {nx.algorithms.average_shortest_path_length(G, weight='weight' ,method='floyd-warshall')}")
print(f"Ruta más corta entre a y t usando Dijkstra: {nx.dijkstra_path(G,'a','t')}")
print(f"Longitud de la ruta entre a y t usando Dijkstra: {nx.dijkstra_path_length(G,'a','t')}")
print(f"Longitud de Ruta ponderada más corta desde el nodo c:{nx.single_source_dijkstra_path_length(G,'c')}")
print(f"Radio: {nx.radius(G)}")
print(f"Diámetro: {nx.diameter(G)}")
print(f"Excentricidad: {nx.eccentricity(G)}")
print(f"Centro: {nx.center(G)}")
print(f"Periferia: {nx.periphery(G)}")
print(f"Densidad: {nx.density(G)}")