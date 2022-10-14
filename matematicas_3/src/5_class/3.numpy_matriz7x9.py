# 3.Generar una matriz de 7 por 9. Las primeras 3 columnas de la matriz tienen que tener el valor 0. 
# La cuarta columna debe tener el valor 0.5,excepto por el último valor de esa columna, que tiene 
# que ser 0.7. Las otras tres columnas  deben tener el valor 1. Luego imprimir la matriz.
# imprimir también el promedio de la última fila.

import numpy as np

matriz = np.zeros((7,9))
matriz[:,2] += 0.4
matriz[:,3] += 0.5
matriz[6,3] += 0.2
matriz[:,6:10] += 1

print(f'\nLa matriz final es: {matriz}\n')
print(f'Sumatoria de la última fila: {np.sum(matriz[len(matriz)-1])}')