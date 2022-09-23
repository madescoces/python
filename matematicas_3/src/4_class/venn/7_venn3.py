import matplotlib.pyplot as plt
from matplotlib_venn import venn3_unweighted, venn3_circles

"""
i. n(A)
ii. n(C)
iii. n(A')
iv. n(A ∩ B)
v. n(A∪B∪C)
vi. n(A∩C')
vii. n(A∩B∩C)
viii. n(A'∩B'∩C')
"""

diagram = venn3_unweighted ((1,1,1,1,1,1,1),
    set_labels=("A","B","C"),
    set_colors=("#FFFFFF","#FFFFFF","#FFFFFF"))

# establecemos el tamaño de la fuente
for subset in ("111","110","101","100","011","010","001"):
    diagram.get_label_by_id(subset).set_fontsize(16)

circles = venn3_circles(subsets=(1,1,1,1,1,1,1),
    color="#000000",
    alpha=0.5,
    linewidth=3)

diagram.get_label_by_id('100').set_text('3') # A
diagram.get_label_by_id('010').set_text('8') # AiC
diagram.get_label_by_id('001').set_text('12')# C
diagram.get_label_by_id('110').set_text('7') # AiB
diagram.get_label_by_id('011').set_text('4') # BiC
diagram.get_label_by_id('101').set_text('8') # B
diagram.get_label_by_id('111').set_text('8') # AiBiC

N = 6

nA =    int(diagram.get_label_by_id('100').get_text()) + \
        int(diagram.get_label_by_id('010').get_text()) + \
        int(diagram.get_label_by_id('110').get_text()) + \
        int(diagram.get_label_by_id('111').get_text())

nC =    int(diagram.get_label_by_id('010').get_text()) + \
        int(diagram.get_label_by_id('001').get_text()) + \
        int(diagram.get_label_by_id('011').get_text()) + \
        int(diagram.get_label_by_id('111').get_text())
        
U =     int(diagram.get_label_by_id('100').get_text()) + \
        int(diagram.get_label_by_id('010').get_text()) + \
        int(diagram.get_label_by_id('001').get_text()) + \
        int(diagram.get_label_by_id('110').get_text()) + \
        int(diagram.get_label_by_id('101').get_text()) + \
        int(diagram.get_label_by_id('011').get_text()) + \
        int(diagram.get_label_by_id('111').get_text()) + \
        N

nA_ =   U - nA         
AiB =   int(diagram.get_label_by_id('110').get_text()) + \
        int(diagram.get_label_by_id('111').get_text())

AiC =   int(diagram.get_label_by_id('110').get_text()) + \
        int(diagram.get_label_by_id('010').get_text())

AuBuC = U - N

AiBiC = int(diagram.get_label_by_id('111').get_text())

AiC_ = nA - AiC

#Text box para solo pertenecientes al conjunto A
plt.annotate(f'n(A): {nA}', 
    xy= diagram.get_label_by_id('100').get_position(),
    xytext= (-100,20),
    size= 'medium',
    ha= 'center',
    textcoords= 'offset points',
    bbox= dict(boxstyle='round, pad = 0.5', fc='lime', alpha=0.3),
    arrowprops= dict(arrowstyle='->',connectionstyle='arc3, rad = -0.2',color='gray')
)

#Text box para solo pertenecientes al conjunto C
plt.annotate(f'n(C): {nC}',
    xy= diagram.get_label_by_id('001').get_position(),
    xytext= (-120,20),
    size= 'medium',
    ha= 'center',
    textcoords= 'offset points',
    bbox= dict(boxstyle='round, pad = 0.5', fc='lime', alpha=0.3),
    arrowprops= dict(arrowstyle='->',connectionstyle='arc3, rad = -0.2',color='gray')
)

#Text box Intersección de todos
plt.annotate(f'n(A∩B∩C): {AiBiC}',
    xy= diagram.get_label_by_id('111').get_position(),
    xytext= (-150,0),
    size= 'medium',
    ha= 'center',
    textcoords= 'offset points',
    bbox= dict(boxstyle='round, pad = 0.5', fc='lime', alpha=0.3),
    arrowprops= dict(arrowstyle='->',connectionstyle='arc3, rad = -0.2',color='gray')
)

#Text box complemento de A
plt.annotate(f"n(A'): {nA_}", 
    xy= diagram.get_label_by_id('100').get_position(),
    xytext= (-100,-10),
    size= 'medium',
    ha= 'center',
    textcoords= 'offset points',
    bbox= dict(boxstyle='round, pad = 0.5', fc='lime', alpha=0.3),
    arrowprops= dict(arrowstyle='->',connectionstyle='arc3, rad = -0.2',color='gray')
)

#Text box AiB
plt.annotate(f"n(A∩B): {AiB}", 
    xy= diagram.get_label_by_id('110').get_position(),
    xytext= (0,80),
    size= 'medium',
    ha= 'center',
    textcoords= 'offset points',
    bbox= dict(boxstyle='round, pad = 0.5', fc='lime', alpha=0.3),
    arrowprops= dict(arrowstyle='->',connectionstyle='arc3, rad = -0.2',color='gray')
)

# Etiqueta del complemento
plt.text(0.4,-0.5,
    s=f"Fuera de conjuntos: {N}",
    size=12, ha="left", va="top", bbox=dict(boxstyle="square",
        ec=(1.0,0.7,0.5),
        fc=(1.0,0.9,0.8),))

plt.text(0.4,-0.62,
    s=f"n(A∪B∪C): {AuBuC}",
    size=12, ha="left", va="top", bbox=dict(boxstyle="square",
        ec=(1.0,0.7,0.5),
        fc=(1.0,0.9,0.8),))

plt.text(0.4,-0.74,
    s=f"n(A∩C'): {AiC_}",
    size=12, ha="left", va="top", bbox=dict(boxstyle="square",
        ec=(1.0,0.7,0.5),
        fc=(1.0,0.9,0.8),))

plt.text(0.4,-0.86,
    s=f"n(A'∩B'∩C'): {N}",
    size=12, ha="left", va="top", bbox=dict(boxstyle="square",
        ec=(1.0,0.7,0.5),
        fc=(1.0,0.9,0.8),))       

plt.show()