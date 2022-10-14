import pandas as pd
import numpy as np
import os

# 4. El archivo autos.xlsx contiene datos de precios de autos y stock. 
# Construye el código necesario que emita el precio mínimo, el máximo y promedio.

# Cambio de directorio
os.chdir('D:/Usuario/Pablo/Escritorio/workspace/python/matematicas_3/src/6_class/')

xls = pd.ExcelFile('autos.xlsx')
autos = xls.parse('autos')
marca = xls.parse('marca')

autosMerged = pd.merge(marca,autos,left_on='id', right_on='IDMARCA')

print(f"\nEl valor del auto más economico es: $ {autosMerged['PRECIO'].min()}")
print(f"\nEl valor del auto más caro es: $ {autosMerged['PRECIO'].max()}")
print(f"\nEl valor medio es: $ {np.round(autosMerged['PRECIO'].mean(), decimals= 2)}")
#print(marca)
