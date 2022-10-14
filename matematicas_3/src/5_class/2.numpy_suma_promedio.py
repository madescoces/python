# 2. Resolver con numpy. Calcular la suma de los elementos de a (ejercicio anterior) utilizando 
# dos 'for' anidados, luego hacerlo mismo con la función np.sum
import numpy as np

listaLISTAS = [ [-44,22],
                [12.0,51],
                [1300,-5.0] ]

def sumar(matriz):
    suma = 0
    for fila in matriz:
        for element in fila:
            suma += element
    return suma

def prom(matriz,end=0):
    suma = 0
    counter = 0
    
    if (end):
        for fila in matriz[0:end]:
            for element in fila:
                counter +=1
                suma += element
    else:
        for fila in matriz:
            for element in fila:
                counter +=1
                suma += element
        
    return suma/counter


print(f'\nSuma Usando for anidado: {sumar(listaLISTAS)}\n')
print(f'Suma Usando numpy: {np.sum(listaLISTAS)}')

print(f'\nPromedio Usando for anidado: {prom(listaLISTAS,2)}')
print(f'Promedio Usando numpy: {np.mean(listaLISTAS[0:2])}')