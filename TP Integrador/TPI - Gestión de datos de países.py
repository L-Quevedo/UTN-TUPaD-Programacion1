#TPI - Gestión de datos de países - Quevedo Lucas, Aranburu Juan


with open("Dataset_lista_paises.csv","r") as archivo:
    for linea in archivo:
        linea = linea.strip()
        partes = linea.split(",")
        print(partes)

