# 4. La siguiente linea crea una matriz aleatoria de 5 por 5 con valores entre 0 y 1
# Imprimir las posiciones (Fila y columna) de los elementos de la matriz que son mayores que 0.5
import numpy as np

matriz_aleatoria=np.random.rand(5,5)
print(f'Matriz aleatoria de 5x5: \n {matriz_aleatoria}')
print(f'Valores mayores que 0.5: \n {matriz_aleatoria[matriz_aleatoria > 0.5]}')


