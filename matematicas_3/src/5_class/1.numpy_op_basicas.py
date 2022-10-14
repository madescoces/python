import numpy as np

listaLISTAS = [ [-44,22],
                [12.0,51],
                [1300,-5.0] ]

#Restarle 5 a la segunda fila
listaNP = np.array(listaLISTAS)

print(f"Array Original: \n {listaLISTAS}")
listaNP[1] -= 5
print(f"\nArray restando 5 a la fila 1: \n {listaNP}")


#Multiplicar todo por 2
listaNP = np.array(listaLISTAS)

print(f"\nArray Original: \n {listaLISTAS}")
listaNP *= 2
print(f"\nArray multiplicado por 2: \n {listaNP}")

#Dividir por -5 las dos primeras filas
listaNP = np.array(listaLISTAS)

print(f"\nArray Original: \n {listaLISTAS}")
listaNP[0:2,:] /= -5
print(f"\nArray dividido por -5 en fila 0 y 1: \n {listaNP}")

#Imprimir la última fila de la matriz
listaNP = np.array(listaLISTAS)
print(f"\nLa última fila es: {listaNP[len(listaNP)-1]}")