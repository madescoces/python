import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

import warnings
warnings.filterwarnings('ignore')

# Creación del grafo
grafo = nx.DiGraph()
nodos = list(np.arange(0,8))

# Posiciones en Y
lvl1 = 10
lvl2 = 5
lvl3 = 0

# Pesos según importancia
tamLVL1 = 3500
tamLVL2 = 2750
tamLVL3 = 1650

grafo.add_edges_from([(0,1),(0,2),(1,3),(1,4),(2,5),(2,6),(2,7)])
posiciones = {0:(5.0,lvl1),1:(3,lvl2),2:(7,lvl2),3:(0,lvl3),4:(2.5,lvl3),5:(5,lvl3),6:(7.5,lvl3),7:(10,lvl3)}
etiquetas = {0:'CEO',1:'Lider: X',2:'Lider: Y',3:'a',4:'b',5:'c',6:'d',7:'e'}
col = ['snow','turquoise','orange','turquoise','turquoise','orange','orange','orange' ]
col_f = [ 'turquoise','orange','turquoise','turquoise','orange','orange','orange' ]
tam = [tamLVL1,tamLVL2,tamLVL2,tamLVL3,tamLVL3,tamLVL3,tamLVL3,tamLVL3]

grafo.add_nodes_from(nodos)

nx.draw_networkx(   grafo, 
                    pos= posiciones,    
                    labels= etiquetas,
                    node_shape= 'h',
                    node_color= col,
                    edge_color= col_f,
                    edgecolors= 'gray',
                    node_size= tam,
                    font_size= 9                    
                )

nx.draw_networkx_edge_labels(   grafo,
                                pos= posiciones,
                                edge_labels= {(0,1):'X', (0,2): 'Y'},
                                font_color= 'gray',
                                font_size= 7 )

plt.title('Organigrama de Empresa X', color='gray', size = 12 )
plt.margins(y=0.2)
plt.axis('off')
plt.show()