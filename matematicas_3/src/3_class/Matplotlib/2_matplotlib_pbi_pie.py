import matplotlib.pyplot as plt
import numpy as np

pbiLatino = {'Argentina' : 440769.2, 'Bolivia' : 29702.8, 'Brasil' : 2364409.9, 'Chile' : 286013.8, \
'Colombia' : 394571.1, 'Ecuador' : 88554.7,'Guyana' : 4780.6,'México' : 1309880.9,'Paraguay' : 37260.6, \
'Perú' : 210881.6,'Surinam' : 4678.2,'Uruguay' : 50532.1,'Venezuela' : 116067.8 }

# Figure creation

fig = plt.figure(figsize=(12,12), dpi=72)
ax = fig.add_subplot(111)
defase = [0.1,0,0,0,0,0,0,0,0,0,0,0,0]

ax.pie(list(pbiLatino.values()),labels=list(pbiLatino),autopct="%0.1f %%", explode=defase)
ax.set_title('Pbi Latinoamericano')

plt.show()
