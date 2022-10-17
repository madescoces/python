# 5. El archivo comercio_interno.csv contiene información sobre el comercio interno desde la década del 
# 90. Escribe un programa que:
#   a. Muestre por pantalla las dimensiones del Data Frame, el número de datos que contiene, los nombres 
#   de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas 
#   filas.
#   b. Muestre por pantalla un gráfico de los datos de empleo por provincia y su relación con la columna 
#   valor.
#   c. Muestre por pantalla la columna alcance_nombre ordenada alfabéticamente.
#   d. Muestre un gráfico de la actividad_producto_nombre agrupados en relación al valor
#   e. Sume por alcance_nombre los valores de los años 2009 al 2019
#   f. Muestre un gráfico de la actividad_producto_nombre en la provincia de Mendoza del año 2015 al 2019

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
import os
import datetime
from printPlotH import *

#Cambio de directorio
os.chdir("D:/Usuario/Pablo/Escritorio/workspace/python/matematicas_3/src/6_class/")

#Importación y creación del DataFrame
csv = pd.read_csv("comercio_interno.csv", encoding='latin-1')
df_original = pd.DataFrame(csv)

#Con estas lineas se remueven las columnas no usadas
df_filtered = df_original.drop(['sector_id','sector_nombre','variable_id','unidad_de_medida','fuente','frecuencia_nombre','cobertura_nombre','alcance_id'] , axis=1)

#Con estas lineas se remueven las filas no usadas
df_filtered = df_filtered.drop(df_filtered[df_filtered['alcance_nombre'] == 'Argentina'].index)
df_filtered = df_filtered.drop(df_filtered[df_filtered['alcance_nombre'] == 'GRAN BUENOS AIRES'].index)
df_filtered = df_filtered.drop(df_filtered[df_filtered['alcance_nombre'] == 'INDETERMINADA'].index)
df_filtered = df_filtered.drop(df_filtered[df_filtered['alcance_nombre'] == 'PARTIDOS DE GBA'].index)
df_filtered = df_filtered.drop(df_filtered[df_filtered['alcance_nombre'] == 'RESTO DE BUENOS AIRES'].index)

df_alcance_nombre = df_filtered.drop_duplicates(subset=['alcance_nombre'])
df_alcance_nombre = df_alcance_nombre.get(['alcance_nombre'])
df_alcance_nombre = pd.DataFrame.sort_values(df_alcance_nombre, by=['alcance_nombre'])

print(f"\nLa base de datos tiene: {df_filtered.shape[0]} Filas x {df_filtered.shape[1]} Columnas")
print(f"\nCantidad de registros: {df_filtered.shape[0]*df_filtered.shape[1]}")

temp = df_filtered.dtypes
nameType = pd.DataFrame({'Nombre de la Columna':temp.index, 'Tipo Dato':temp.values})

print(f'\n{tabulate(nameType, showindex=False, headers=nameType.columns)}')
print(f'\n{tabulate(df_filtered.head(10), showindex=False, headers=df_filtered.columns)}')
print(f'\n{tabulate(df_filtered.tail(10), showindex=False, headers=df_filtered.columns)}')
print(f'\n{tabulate(pd.DataFrame(df_alcance_nombre), showindex=False, headers=df_alcance_nombre.columns)}')

#########################################################################################################
# b. Muestre por pantalla un gráfico de los datos de empleo por provincia y su relación con la columna 
#########################################################################################################

# me quedo solo con los indicadores de Empleo, configuro variables a usar
empleo = df_filtered.drop(df_filtered[df_filtered['indicador'] != 'Empleo'].index)
etiquetas = list(empleo.groupby('alcance_nombre')['valor'].sum().index) # Etiquetas de provincia
valores = np.round(empleo.groupby('alcance_nombre')['valor'].sum(), decimals=0) # cantidad de empleos

printPlot(etiquetas, valores, titulo='Indicadores de empleos por provincia 1996/2018', alto=8, ancho=17)

#########################################################################################################
# d. Muestre un gráfico de la actividad_producto_nombre agrupados en relación al valor
#########################################################################################################

# Filtrado
df_filtered = df_filtered.drop(df_filtered[df_filtered['actividad_producto_nombre'] == 'Vtas en centros_de_compras_total'].index)
df_filtered = df_filtered.drop(df_filtered[df_filtered['actividad_producto_nombre'] == 'Vtas en mayoristas_total'].index)
df_filtered = df_filtered.drop(df_filtered[df_filtered['actividad_producto_nombre'] == 'Vtas en super_total'].index)

# Variables de Generacion del grafico
tipoAct = df_filtered.groupby('actividad_producto_nombre')['valor'].sum()
etiquetas2 = list(tipoAct.index) # Etiquetas de actividad_producto_nombre
valores2 = np.round(tipoAct.values, decimals=0) # valores acumulados

printPlot(etiquetas2,valores2, titulo='Millones de pesos por actividad 1996/2018', alto=8, ancho=18)

#########################################################################################################
# e. Sume por alcance_nombre los valores de los años 2009 al 2019
#########################################################################################################

# Variables de Generacion del grafico y filtrado
df_filtered['indice_tiempo']=pd.to_datetime(df_filtered['indice_tiempo'], format="%d/%m/%Y")
df_filtered['año'],df_filtered['mes']=df_filtered['indice_tiempo'].dt.year,df_filtered['indice_tiempo'].dt.month
valores2009_2019 = df_filtered.drop(df_filtered[df_filtered['año']>=2009].index)
valores2009_2019 = df_filtered.groupby('alcance_nombre')['valor'].sum()

etiquetas3 = list(valores2009_2019.index) # Etiquetas de actividad_producto_nombre
valores3 = np.round(valores2009_2019.values, decimals=0) # valores acumulados

printPlot(etiquetas3,valores3, titulo='Indicadores de empleos por provincia 2009/2018', alto=8, ancho=17)

#########################################################################################################
# f. Muestre un gráfico de la actividad_producto_nombre en la provincia de Mendoza del año 2015 al 2019
#########################################################################################################

# Variables de Generacion del grafico y filtrado

df_filtered['indice_tiempo'] = pd.to_datetime(df_filtered['indice_tiempo'], format="%d/%m/%Y")
df_filtered['año'],df_filtered['mes'] = df_filtered['indice_tiempo'].dt.year,df_filtered['indice_tiempo'].dt.month
mendoza2015Plus = df_filtered.drop(df_filtered[df_filtered['año']>=2015].index)
mendoza2015Plus = mendoza2015Plus.drop(mendoza2015Plus[mendoza2015Plus['alcance_nombre'] != 'MENDOZA'].index)

mendoza2015Plus = df_filtered.groupby('actividad_producto_nombre')['valor'].sum()
etiquetas4 = list(mendoza2015Plus.index) # Etiquetas de actividad_producto_nombre
valores4 = np.round(mendoza2015Plus.values, decimals=0) # valores acumulados

printPlot(etiquetas4,valores4, titulo='Indicadores de actividad en MENDOZA desde el 2015', alto=8, ancho=17)