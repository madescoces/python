from turtle import width
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

lit = {"Romántica":40,"Clásica":118,"Fantástica":50,"Moderna":95,"Antigüa":56,"Poesía":131,"Cuento":87,"Novela":103}
bio = (40,50,60,75,34,61)
mat = [34,40,61,75,87,90,103]

#####
# funciones
#####
def unirTodos(*args):
    resultado = []
    for col in args:
        if (type(dict()) == type(col)):
            resultado.append(set(col.values()))
        else:
            resultado.append(set(col))
    return resultado

def sumarColeccion(col):
    suma = 0
    if (type(dict()) == type(col)):
        for item in col.values():
            suma += item
    else:
        for item in col:
            suma += item
    return suma

def soloPertenceA(col):
    return (col[0] - col[1]) & (col[0] - col[2])

def intersect(col):
    if len(col) == 3:
        return (col[0] & col[1] & col[2])
    else:
        return (col[0] & col[1])

def union(col):
    if len(col) == 3:
        return (col[0] | col[1] | col[2])
    else:
        return (col[0] | col[1])
####
# variables auxiliares
####
U = 1000 #Universo total
N = U - sum(union(unirTodos(lit,bio,mat))) #Correspondiente al complemento de (AUBUC)

#####
# grafica
#####

figDPI = 150
fig = plt.figure('Primer parcial -> Foglia Pablo -> Evualuación de asignaturas', figsize=(9,5.5), dpi=figDPI)

# dibujamos los diagramas
diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=(
    "Literatura", "Biologia", "Matemática"))

# establecemos el tamaño de la fuente
for subset in ("111", "110", "101", "100", "011", "010", "001"):
    diagram.get_label_by_id(subset).set_fontsize(10)

# transferimos los resultados de las operaciones
diagram.get_label_by_id('100').set_text(soloPertenceA(unirTodos(lit,bio,mat)))
diagram.get_label_by_id('100').set_size(6.5)
diagram.get_label_by_id('010').set_text(soloPertenceA(unirTodos(bio,lit,mat)))
diagram.get_label_by_id('010').set_size(6.5)
diagram.get_label_by_id('001').set_text(soloPertenceA(unirTodos(mat,bio,lit)))
diagram.get_label_by_id('001').set_size(6.5)
diagram.get_label_by_id('110').set_text(intersect(unirTodos(lit,bio))-intersect(unirTodos(lit,bio,mat)))
diagram.get_label_by_id('110').set_size(6.5)
diagram.get_label_by_id('011').set_text(intersect(unirTodos(bio,mat))-intersect(unirTodos(lit,bio,mat)))
diagram.get_label_by_id('011').set_size(6.5)
diagram.get_label_by_id('101').set_text(intersect(unirTodos(lit,mat))-intersect(unirTodos(lit,bio,mat)))
diagram.get_label_by_id('101').set_size(6.5)
diagram.get_label_by_id('111').set_text(intersect(unirTodos(lit,bio,mat)))
diagram.get_label_by_id('111').set_size(6.5)

# marcamos los contornos
c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), linewidth=0.4, color="black")
x_text= -1.20
y_text= 0
space= -0.1

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
         s="Respuestas: ",
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(x_text,y_text+space*2,
         s=f"Aprobaron Todas = {sum(intersect(unirTodos(lit,bio,mat)))}",
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(x_text,y_text+space*3,
         s=f"Aprobaron Literatura y Matemática= {sum(intersect(unirTodos(lit,mat)))}",
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(x_text,y_text+space*4,
         s=f"Aprobaron Solo Literatura= {sum(soloPertenceA(unirTodos(lit,bio,mat)))}",
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(x_text,y_text+space*5,
         s=f"Aprobaron Solo Biologia= {sum(soloPertenceA(unirTodos(bio,lit,mat)))}",
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(x_text,y_text+space*6,
         s=f"Aprobaron Solo Matemática= {sum(soloPertenceA(unirTodos(mat,lit,bio)))}",
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

print(sum(soloPertenceA(unirTodos(lit,bio,mat))))
print(sum(soloPertenceA(unirTodos(bio,lit,mat))))
print(sum(soloPertenceA(unirTodos(mat,lit,bio))))
plt.text(x_text,y_text+space*7,
         s=f"Aprobaron Al menos dos= {sum(union(unirTodos(lit,bio,mat)))-sum(soloPertenceA(unirTodos(lit,bio,mat))|soloPertenceA(unirTodos(bio,mat,lit))|soloPertenceA(unirTodos(mat,lit,bio)))-sum(intersect(unirTodos(lit,bio,mat)))}",
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





















