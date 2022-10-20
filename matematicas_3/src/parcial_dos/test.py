import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edge("reddit", "youtube", w=5)
G.add_edge("reddit", "google", w=10)
G.add_edge("google", "reddit", w=30)
G.add_edge("youtube", "reddit", w=20)
print(G.adj)

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=[5000, 50, 300])
nx.draw_networkx_labels(G, pos)
"""for edge in G.edges(data=True):
    w = edge[2]['w']
    nx.draw_networkx_edges(G, pos, edgelist=[(edge[0],edge[1])], arrowsize=w, node_size=[5000, 50, 300])"""
plt.show()