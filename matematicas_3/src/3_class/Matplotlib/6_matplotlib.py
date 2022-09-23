import matplotlib.pyplot as plt
import numpy as np

grupo1 = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
grupo2 = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
rango = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
x = np.arange(len(rango))

fig, ax = plt.subplots()
ax.set_title('Calificaciones por deportista')

scatterUno = plt.scatter(rango,grupo1,color='r')
scatterDos = plt.scatter(rango,grupo2,color='b')
plt.show()