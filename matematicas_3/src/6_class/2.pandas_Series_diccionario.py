import numpy as np
import pandas as pd 
import os

# Cambio de directorio para encontrar la base de nombres
os.chdir('D:/Usuario/Pablo/Escritorio/workspace/python/matematicas_3/src/6_class/')

# Cambio los decimales a solamente 2, no anda siempre....
# np.set_printoptions(precision=2)
# pd.options.display.float_format = '${:,.2f}'.format

def returnSerie(dic):
    #genero matriz con min, max, media y desviacion std  
    matrix = np.min(list(dic.values()),axis=1)
    matrix = np.vstack([matrix, np.max(list(dic.values()),axis=1)])
    matrix = np.vstack([matrix, np.round(np.mean(list(dic.values()),axis=1),decimals=2)])
    matrix = np.vstack([matrix, np.round(np.std(list(dic.values()),axis=1),decimals=2)])
    matrix = np.swapaxes(matrix,0,1)
    #genero panda Series con los valores a retornar
    data = pd.Series(list(matrix),index=dic.keys(), dtype=np.float64)  
    return data

calificaciones = {}

# Carga de datos desde el txt origen al diccionario de notas
with open('nombres.txt', mode='r', encoding='utf-8') as f:
    for item in f:
        calificaciones[item.rstrip()] = list(np.random.randint(0, 10 , size=8))

my_dataFrame = returnSerie(calificaciones)
print(f"\n{my_dataFrame}")

