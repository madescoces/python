"""8. En una encuesta de 80 dueños de casa, se descubrió que:
• 30 tenían al menos un perro.
• 42 tenían al menos un gato.
• 21 tenían al menos una mascota "otra" (pez, tortuga, reptil, hámster, etc.).
• 20 Tenían perro(s) y gato (s).
• 10 tenían gato(s) y mascota(s) otra.
• 8 tenían perro(s) y mascota(s) otra.
• 5 tenían los tres tipos de mascotas."""

import matplotlib.pyplot as plt
from matplotlib_venn import venn3_unweighted 

AiBiC = 5
AiB = 20-AiBiC
AiC = 8-AiBiC
BiC = 10-AiBiC
A = 30-(AiB+AiC+AiBiC)  # Perros = 30
B = 42-(AiB+BiC+AiBiC) # Gatos = 42
C = 21-(AiC+BiC+AiBiC) # Otros = 21 
AuB = A+B-AiB
AuC = A+C-AiC
BuC = B+C-BiC
N=20
U = AiBiC+AiB+AiC+BiC+A+B+C+N

conjunto = venn3_unweighted(subsets=(A,B,AiB,C,AiC,BiC,AiBiC),
    set_labels=('Perros','Gatos','Otros'),alpha=0.5,normalize_to=1.2)

# Agrego el conjunto universal con un circulo como delimitador
from matplotlib.patches import Circle
plt.gca().add_patch(Circle([0,0],1,fill=False))
plt.xlim(-1.05,1.05)
plt.ylim(-1.05,1.05)

# Etiqueta del universo
plt.text(-0.9,1.1,
    s=f"U = {U} ",
    size=12, ha="left", va="top", bbox=dict(boxstyle="square",
        ec=(1.0,0.7,0.5),
        fc=(1.0,0.9,0.8),))

# Etiqueta del complemento
plt.text(0.28,-0.75,
    s=f"Fuera de conjuntos: {N}",
    size=12, ha="left", va="top", bbox=dict(boxstyle="square",
        ec=(1.0,0.7,0.5),
        fc=(1.0,0.9,0.8),))

plt.text(-1.5,1.25,'Diagrama de encuesta "mascotas preferidas"',fontsize=16)

plt.show()