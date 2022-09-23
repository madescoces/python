import matplotlib.pyplot as plt
from matplotlib_venn import venn3_unweighted 

AiBiC = 50
AiB = 62-AiBiC
AiC = 58-AiBiC
BiC = 98-AiBiC
A = 80-(AiB+AiC+AiBiC)  # Laptop = 80
B = 110-(AiB+BiC+AiBiC) # Celu = 110
C = 125-(AiC+BiC+AiBiC) # Ipod = 125 
AuB = A+B-AiB
AuC = A+C-AiC
BuC = B+C-BiC
N=0
U = AiBiC+AiB+AiC+BiC+A+B+C+N

conjunto = venn3_unweighted(subsets=(A,B,AiB,C,AiC,BiC,AiBiC),
    set_labels=('Laptop','Celular','Ipod'),alpha=0.5,normalize_to=1.2)

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

plt.text(-1.1,1.25,'Diagrama de preferencia vehicular',fontsize=16)

plt.show()