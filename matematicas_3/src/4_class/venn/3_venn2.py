import matplotlib.pyplot as plt
from matplotlib_venn import venn2_unweighted 

figDPI = 150

fig = plt.figure(figsize=(8,5), dpi=figDPI)
U=500

conjunto = venn2_unweighted(subsets={'10':1,'01':1,'11':1},
    set_labels=('Algebra II','Deportes'),alpha=0.5,normalize_to=2.35)

#Settings de algebra II
conjunto.get_label_by_id('10').set_text('125-52 = 73')
conjunto.get_patch_by_id('10').set_color('tomato')
#Settings de deportes
conjunto.get_label_by_id('01').set_text('257-52 = 205')
conjunto.get_patch_by_id('01').set_color('tomato')
#Settings de los comunes a ambos
conjunto.get_label_by_id('11').set_text('52')
conjunto.get_patch_by_id('11').set_color('orange')

# Agrego el conjunto universal con un circulo como delimitador
from matplotlib.patches import Circle
plt.gca().add_patch(Circle([0,0],1.15,fill=False))
plt.xlim(-1.16,1.16)
plt.ylim(-1.16,1.16)

# Etiqueta del universo
plt.text(-0.9,1.1,
    s="U = " + str(U),
    size=12, ha="left", va="top", bbox=dict(boxstyle="square",
        ec=(1.0,0.7,0.5),
        fc=(1.0,0.9,0.8),))

# Etiqueta del complemento
plt.text(0.28,-1.10,
    s="Fuera de conjuntos:\n" + str('500-(73+52+205)= 170'),
    size=12, ha="left", va="top", bbox=dict(boxstyle="square",
        ec=(1.0,0.7,0.5),
        fc=(1.0,0.9,0.8),))

plt.text(-1.45,1.30,'Diagrama de inscriptos Algebra / Deportes',fontsize=16)

#Text box para algebra
plt.annotate('Inscriptos en\nÁlgebra II: 125', 
    xy= conjunto.get_label_by_id('10').get_position(),
    xytext= (-100,-80),
    size= 'medium',
    ha= 'center',
    textcoords= 'offset points',
    bbox= dict(boxstyle='round, pad = 0.5', fc='lime', alpha=0.3),
    arrowprops= dict(arrowstyle='->',connectionstyle='arc3, rad = 0.2',color='gray')
)

#Text box para deportes
plt.annotate('Practican\ndeportes: 257', 
    xy= conjunto.get_label_by_id('01').get_position(),
    xytext= (100,-80),
    size= 'medium',
    ha= 'center',
    textcoords= 'offset points',
    bbox= dict(boxstyle='round, pad = 0.5', fc='lime', alpha=0.3),
    arrowprops= dict(arrowstyle='->',connectionstyle='arc3, rad = -0.2',color='gray')
)

#Text box para los comunes
plt.annotate('Inscritos en Álgebra II\ny practican deportes.', 
    xy= conjunto.get_label_by_id('11').get_position(),
    xytext= (0,-70),
    size= 'medium',
    ha= 'center',
    textcoords= 'offset points',
    bbox= dict(boxstyle='round, pad = 0.5', fc='lime', alpha=0.3),
    arrowprops= dict(arrowstyle='->',connectionstyle='arc3, rad = 0',color='gray')
)

plt.show()