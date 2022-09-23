import matplotlib.pyplot as plt
from matplotlib_venn import venn3_unweighted 


moto={5,20,3,10}
auto={46,20,10,14}
bici={0,3,10,14}
ninguno={1}


moto_auto_bici = sum(moto&auto&bici)
solo_moto = sum(moto-(auto|bici))
solo_auto = sum(auto-(moto|bici))
solo_bici = sum(bici-(auto|moto))
moto_bici = sum(moto&bici)-moto_auto_bici
moto_auto = sum(moto&auto)-moto_auto_bici
auto_bici = sum(auto&bici)-moto_auto_bici

conjunto = venn3_unweighted(subsets=(solo_moto,solo_auto,moto_auto,solo_bici,moto_bici,auto_bici,moto_auto_bici),
    set_labels=('Moto','Auto','Bici'),alpha=0.5,normalize_to=1.2)

# Agrego el conjunto universal con un circulo como delimitador
from matplotlib.patches import Circle
plt.gca().add_patch(Circle([0,0],1,fill=False))
plt.xlim(-1.05,1.05)
plt.ylim(-1.05,1.05)

# Etiqueta del universo
plt.text(-0.9,1.1,
    s="U = " + str(sum(moto|auto|bici|ninguno)),
    size=12, ha="left", va="top", bbox=dict(boxstyle="square",
        ec=(1.0,0.7,0.5),
        fc=(1.0,0.9,0.8),))

# Etiqueta del complemento
plt.text(0.28,-0.75,
    s="Fuera de conjuntos: " + str(sum(ninguno)),
    size=12, ha="left", va="top", bbox=dict(boxstyle="square",
        ec=(1.0,0.7,0.5),
        fc=(1.0,0.9,0.8),))

plt.text(-1.1,1.25,'Diagrama de preferencia vehicular',fontsize=16)

plt.show()