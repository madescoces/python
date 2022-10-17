# Copyright Pablo Foglia(c)
def changeDijkstraPathColor(grafo, dijkstraPath):
    for i,e in enumerate(dijkstraPath):
        if(i<(len(dijkstraPath)-1)):
            grafo[e][dijkstraPath[i+1]]['edge_color'] = 'blue'