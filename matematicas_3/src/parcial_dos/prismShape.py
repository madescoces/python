import numpy as np

def genXcord(size, lines):
    value = 2
    x_cord = [1,]
    for _ in np.arange(int(((size-(2 if size%2==0 else 1)) / lines))):
        for _ in np.arange(lines):    
            x_cord.append(value)
        value +=1
    x_cord.append(value)
    return tuple(x_cord)

def prismShape(node, **kwargs):
    dict_ = dict()
    lines = 2 if not 'lines' in kwargs else kwargs['lines']
    y_cord = (2,1,0) if not 'y_cord' in kwargs else kwargs['y_cord']
    x_cord = genXcord(len(node),lines) if not 'x_cord' in kwargs else kwargs['x_cord']
    
    # Colocación del primer nodo
    dict_[node[0]] = (x_cord[0],y_cord[int(lines/2)])
    
    # Colocación de los nodos del 2 en adelante
    j = 1
    
    for _ in np.arange(0,int(len(x_cord)-2) / lines ):        
        for e in np.arange(lines):                        
            dict_[node[j]] = (x_cord[j],y_cord[e]) if lines%2!=0 else (x_cord[j],y_cord[0 if e==0 else 2])               
            j += 1

    # Si la cantidad de nodos es par agrega el último nodo
    if (len(node)%2 == 0): 
        dict_[node[len(node)-1]] = (x_cord[-1],y_cord[1]) 
    
    return dict_