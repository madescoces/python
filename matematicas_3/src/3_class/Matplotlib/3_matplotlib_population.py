import matplotlib.pyplot as plt
import numpy as np

popPerKM = {'Estados Unidos':[331002651,9831510],'Brasil':[212559417,8514877],'México':[128932753,1964375],\
'Colombia':[50882891,1141748],'Argentina':[45195774,2792600],'Canadá':[37742154,9984670],\
'Perú':[33050325,1285216],'Venezuela':[37742154,9984670],'Chile':[19116201,755934],\
'Guatemala':[17915568,108990],'Ecuador':[17643054,283561],'Bolivia':[11673021,1098585],\
'Cuba':[11326616,110860],'Haití':[11402528,27850],'República Dominicana':[10847910,48762],\
'Honduras':[9904607,112492],'Paraguay':[7132538,406750],'Nicaragua':[6624554,121430],\
'El Salvador':[6486205,21481],'Costa Rica':[5094118,51160],'Panamá':[4314767,78260],'Uruguay':[3473730,176215],\
'Jamaica':[2961167,11524],'Puerto Rico':[2860853,9104],'Trinidad y Tovago':[1399488,5128],\
'Guyana':[786552,214969],'Surinam':[586632,163820],'Belice':[397628,22966],'Bahamas':[393244,13940],\
'Barbados':[287375,439],'Santa Lucia':[183627,623],'Granada':[112523,344],\
'San Vicente y las Granadinas':[110940,389],'Antigua y Barbuda':[97929,443],\
'Dominicana':[71986,754],'San Cristobal y Nieves':[53199,261]}

fig = plt.figure(figsize=(16,8), dpi=72)
ax = fig.add_subplot(111)
peoplePerKm = []

for x,y in popPerKM.values():
    peoplePerKm.append(round(x/y))

for x, y in zip(list(popPerKM), peoplePerKm):
    rgb = np.random.rand(3,)
    ax.bar(x,y,color=[rgb])
    
for i in range(len(peoplePerKm)):
    ax.bar_label(ax.containers[i])

ax.set_title('Habitantes por Kilómetro Cuadrado en America')
ax.set_xlabel('Paises de la región')
ax.set_ylabel('Habitantes por Km')

plt.xticks(rotation='vertical')
plt.subplots_adjust(left=0.1, bottom=0.3)


current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

plt.show()