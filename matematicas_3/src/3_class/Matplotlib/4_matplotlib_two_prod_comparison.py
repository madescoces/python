import matplotlib.pyplot as plt
import numpy as np

producto_1 = (20, 35, 30, 35, 27)
producto_2 = (25, 32, 34, 20, 25)
producto_dif = tuple(map( lambda i,j : abs(i - j), producto_1, producto_2))
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']

x = np.arange(len(dias))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots()
fig.set_size_inches(10,5)
rects1 = ax.bar(x - width, producto_1, width, label='Producto 1')
rects2 = ax.bar(x, producto_2, width, label='Producto 2')
rects3 = ax.bar(x + width, producto_dif, width, label='Diferencia')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Cantidad producida en unidades')
ax.set_title('Comparativa por día de producción')
ax.set_xticks(x, dias)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)

fig.tight_layout()

plt.show()