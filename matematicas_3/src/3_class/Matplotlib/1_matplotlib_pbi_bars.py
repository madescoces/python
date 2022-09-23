import matplotlib.pyplot as plt
import numpy as np

pbiLatino = {'Argentina' : 440769.2, 'Bolivia' : 29702.8, 'Brasil' : 2364409.9, 'Chile' : 286013.8, \
'Colombia' : 394571.1, 'Ecuador' : 88554.7,'Guyana' : 4780.6,'México' : 1309880.9,'Paraguay' : 37260.6, \
'Perú' : 210881.6,'Surinam' : 4678.2,'Uruguay' : 50532.1,'Venezuela' : 116067.8 }

# Figure creation

fig = plt.figure(figsize=(16,6), dpi=72)
ax = fig.add_subplot(111)

ax.bar(list(pbiLatino),list(pbiLatino.values()))
ax.set_title('Pbi Latinoamericano')
ax.set_xlabel('Paises de la región')
ax.set_ylabel('Pbi en USD americanos')

current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

plt.show()
