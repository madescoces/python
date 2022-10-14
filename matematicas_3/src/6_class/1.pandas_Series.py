import datetime
import numpy as np
import pandas as pd 

#Esta linea es para setear el formato de float a 2 decimales
pd.options.display.float_format = '${:,.2f}'.format

rangoAnios = range(int(input("Ingrese desde que año: ")),int(input("Hasta que año: "))+1)
data =  np.random.uniform(low=0, high=999999.99, size=(len(rangoAnios)))

id = pd.date_range(start=datetime.date(rangoAnios[0],1,1), periods=len(rangoAnios), freq='AS')

serie = pd.Series(data, index=id.year)
print(f"\nPandas serie sin descuento:\n{serie}")

serie -= serie*0.1
print(f"\nPandas serie con descuento de 10%:\n{serie}")