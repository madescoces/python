import numpy as np
import pandas as pd

# 3. Escribe una función que reciba los datos siguientes en un DataFrame, una lista de meses, 
# y devuelva el balance (ventas - gastos) total en los meses indicados.

datos = {'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'], 'Ventas':[30500, 35600, 28300, 33900], 'Gastos':[22000, 23400, 18100, 20700]}

dataFrame = pd.DataFrame(datos)
dataFrame['Balance']=dataFrame['Ventas'] - dataFrame['Gastos']

print(dataFrame)