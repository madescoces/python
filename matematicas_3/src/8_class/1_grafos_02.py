import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

import warnings
warnings.filterwarnings('ignore')

fig = plt.figure(1, figsize=(10, 10), dpi=72)
grafo = nx.DiGraph()
nodos = list(np.arange(0,8))

grafo.add_nodes_from(nodos)
grafo.add_edges_from([(0,1),(0,2),(0,6),(1,3),(1,4),(2,3),(2,5),(2,6),(2,7),(3,5),(7,4)])

lbls = { 0:'CEO',1:'Lider X',2:'Lider Y',3:'a',4:'b',5:'c',6:'d',7:'e' }
colors = ['snow','turquoise','orange','turquoise','turquoise','orange','orange','orange']
edge_colors = ['turquoise','orange','turquoise','turquoise','orange','orange','orange','orange','turquoise','turquoise']
weight = [1250,2500,2500,1700,1700,1700,1700,1700]

edge_lbls = {   
                (0,1):'3.0',(0,2):'4.5',(0,6):'5.0',(1,3):'6.0',(1,4):'8.5',
                (2,3):'6.5',(2,5):'10.5',(2,6):'7.0',(2,7):'9.5',(3,5):'1.5',
                (7,4):'6.0'    
            }

nx.draw_networkx(   
                    grafo,
                    pos=nx.shell_layout(grafo),
                    labels= lbls,
                    node_shape= 'h',
                    node_size= weight,
                    node_color= colors,
                    edge_color= edge_colors,
                    edgecolors= "gray",
                    font_size= 8
                 )

nx.draw_networkx_edge_labels( 
                                grafo,
                                pos= nx.shell_layout(grafo),
                                edge_labels= edge_lbls,
                                font_color= 'gray'
                            )

plt.title('Proyecto Urgente', color='gray', size = 12 )
plt.margins(y=0.1, x=0.1)
plt.axis('off')
plt.show()

# Datos para graficas
cen = list(nx.degree_centrality(grafo).values())
cenInt = list(nx.betweenness_centrality(grafo).values())
cenCer = list(nx.closeness_centrality(grafo).values())
etiquetas = list(lbls.values())

# Grafico de Centralidad
plt.bar(np.array(etiquetas), np.array(cen), width=0.65, color='lightcoral')
plt.show()

# Grafico de Centralidad Intermediacion
plt.bar(np.array(etiquetas), np.array(cenInt), width=0.65, color='springgreen')
plt.show()

# Grafico de Centralidad Cercania
plt.bar(np.array(etiquetas), np.array(cenCer), width=0.65, color='gold')
plt.show()