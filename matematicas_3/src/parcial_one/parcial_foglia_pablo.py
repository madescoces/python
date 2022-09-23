from turtle import width
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

#Alumnos totales= 1000

#Alumnos que aprobaron literatura=680: 
literatura = {"Romántica": 40, "Clásica": 118, "Fantástica": 50, "Moderna": 95,"Antigüa": 56, 
"Poesía": 131, "Cuento": 87, "Novela": 103}

#Alumnos que aprobaron biologia=320:
biologia = (40, 50, 60, 75, 34, 61)

#Alumnos que aprobaron matemáticas=490:
matematica = [34, 40, 61, 75, 87, 90, 103]

#Convierton en set para operar los conjuntos:
literaturaSet = set(literatura.values())
biologiaSet = set(biologia)
matematicaSet = set(matematica)
U = 1000 #Universo total

##################################################################################
# Funciones de operación de conjuntos 
##################################################################################
def suma_todo(coleccion):
    suma = 0
    for item in coleccion:
        suma += item
    return suma

def intersect(x, y, z = set()):
    if z:
        return (x & y & z)
    else:
        return (x & y)

def union(x, y, z = set()):
    if z:
        return (x | y | z)
    else:
        return (x | y)

def soloPertenceA( x, y, z ):
    return (x - y) & (x - z)

def aObExclusiva(x, y):
    suma = 0
    x_o_y = ((x | y) - (x & y))
    for elemento in x_o_y:
        suma += elemento
    return suma

def aObInclusiva( x, y ):
    suma = 0
    x_o_y = ((x - y) | y)
    for elemento in x_o_y:
        suma += elemento
    return suma

def alMenosDos( x, y, z ):
    suma = 0
    dosOmas = union(x,y,z)-((z-(x|y))|((x^y)-z))
    print("dos o mas " + str(dosOmas))
    for elemento in dosOmas:
        suma += elemento
    return suma

##################################################################################
# Operaciones de conjuntos
##################################################################################
AiBiC = intersect(literaturaSet, biologiaSet, matematicaSet)
AuBuC = union (literaturaSet,biologiaSet,matematicaSet) 
AminusBuC = soloPertenceA(literaturaSet,biologiaSet,matematicaSet)
BminusAuC = soloPertenceA(biologiaSet,literaturaSet,matematicaSet)
CminusAuB = soloPertenceA(matematicaSet,literaturaSet,biologiaSet)
AiB = intersect(literaturaSet,biologiaSet) - AiBiC
AiC = intersect(literaturaSet,matematicaSet) - AiBiC
BiC = intersect(biologiaSet,matematicaSet) - AiBiC
N = U - sum(AuBuC) #Correspondiente al complemento de (AUBUC)
##################################################################################
# Testing prints
##################################################################################
print(f"Conjunto de literatura: {literaturaSet}")
print(f"Conjunto de biologia: {biologiaSet}")
print(f"Conjunto de matemática:{matematicaSet}")
print(f"A∩B∩C= {AiBiC}")
print(f"A-(B∪C)= {AminusBuC}")
print(f"B-(A∪C)= {BminusAuC}")
print(f"C-(A∪B)= {CminusAuB}")
print(f"A∩B= {AiB}")
print(f"A∩C= {AiC}")
print(f"C∩B= {BiC}")
print(f"Conjunto Universal= {U}")
print(f"Fuera de conjuntos= {N}")

##################################################################################
# Gráfico de resultados
##################################################################################
# preparamos la ventana del gráfico
figDPI = 150
fig = plt.figure('Primer parcial -> Foglia Pablo -> Evualuación de asignaturas', figsize=(9,5.5), dpi=figDPI)

# dibujamos los diagramas
diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
    "Literatura", "Biologia", "Matemática"))

# establecemos el tamaño de la fuente
for subset in ("111", "110", "101", "100", "011", "010", "001"):
    diagram.get_label_by_id(subset).set_fontsize(10)

# transferimos los resultados de las operaciones
diagram.get_label_by_id('100').set_text(AminusBuC)
diagram.get_label_by_id('010').set_text(BminusAuC)
diagram.get_label_by_id('001').set_text(CminusAuB)
diagram.get_label_by_id('110').set_text(AiB)
diagram.get_label_by_id('011').set_text(BiC)
diagram.get_label_by_id('101').set_text(AiC)
diagram.get_label_by_id('111').set_text(AiBiC)

# marcamos los contornos
c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), linewidth=0.4, color="black")
x_text= -1.20
y_text= 0
space= -0.1
# agregamos más datos aclaratorios al gráfico
plt.text(x_text,0.45,
        s=f"Universo ---->   {U} ",
        size=12, ha="left", va="top", bbox=dict(boxstyle="square",
        ec=(1.0,0.7,0.5),
        fc=(1.0,0.9,0.8),))

# Texto fuera del conjunto
plt.text(0.55, -0.5,      
        f"Fuera de los\n conjuntos = {N}",
        size=12, ha="left", va="top", bbox=dict(boxstyle="square",
        ec=(1.0,0.7,0.5),
        fc=(1.0,0.9,0.8),))

# Respondemos las preguntas
plt.text(x_text, y_text+space ,
         s="Respuestas solicitadas: ",
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(x_text,y_text+space*2,
         s=f"Aprobaron Todas = {sum(AiBiC)}",
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(x_text,y_text+space*3,
         s=f"Aprobaron Literatura y Matemática= {sum(AiC)}",
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(x_text,y_text+space*4,
         s=f"Aprobaron Solo Literatura= {sum(AminusBuC)}",
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(x_text,y_text+space*5,
         s=f"Aprobaron Solo Biologia= {sum(BminusAuC)}",
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(x_text,y_text+space*6,
         s=f"Aprobaron Solo Matemática= {sum(CminusAuB)}",
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(x_text,y_text+space*7,
         s=f"Aprobaron Al menos dos= {alMenosDos(literaturaSet,biologiaSet,matematicaSet)}",
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

from matplotlib.patches import Rectangle
plt.gca().add_patch(Rectangle([-5,-2.5],10, 5, facecolor="#c5a63c", alpha=0.3, zorder=2))
#plt.axis('on')  # Recuadro
plt.title("Alumnos que participaron en cada evaluación:")
plt.show()
##################################################################################
# Fin de programa
##################################################################################