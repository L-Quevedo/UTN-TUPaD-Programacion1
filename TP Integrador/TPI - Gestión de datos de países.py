#TPI - Gestión de datos de países - Quevedo Lucas, Aranburu Juan


import csv
from pathlib import Path

#Ruta del archivo
ruta_csv = Path("Dataset_lista_paises.csv")

print("Verificando archivo…")
print("Ruta actual:", Path().absolute())
print("Existe el archivo CSV:", ruta_csv.exists())

