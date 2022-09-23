import matplotlib.pyplot as plt
import numpy as np

cafe = np.array([5, 5, 7, 6, 7, 4])
te = np.array([1, 2, 0, 2, 1, 3])
agua = np.array([10, 0, 14, 12, 15, 13])
nombres = ['María', 'Pablo', 'Ema', 'Franco', 'Estefanía', 'Pedro']

x = np.arange(len(nombres))    # Cantidad de lugares para las labels
width = 0.35                   # Ancho de las barras

fig, ax = plt.subplots()

barra_uno = ax.bar(x, agua, width, label='Agua', color='#0e80c1')
barra_dos = ax.bar(x, te, width, bottom=agua, label='Té', color='#f3b41c')
barra_tres = ax.bar(x, cafe, width, bottom=agua+te, label='Café', color='#6a5c3a')

ax.axhline(0, color='grey', linewidth=0.8)
ax.set_title('Comparación de líquidos ingeridos por persona')
ax.set_xticks(x, nombres)
ax.legend()

# Label with label_type 'center' instead of the default 'edge'
ax.bar_label(barra_uno, label_type='center')
ax.bar_label(barra_dos, label_type='center')
ax.bar_label(barra_tres, label_type='center')
ax.bar_label(barra_tres)

plt.show()