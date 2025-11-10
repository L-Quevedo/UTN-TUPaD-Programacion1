#TPI - Gestión de datos de países

#Profesores: Virginia Cimino,
#Alumnos: Quevedo Lucas, Aramburu Juan
#Grupo: 58


import os
from pathlib import Path

#creamos la funcion para cargar los datos en el archivo CSV
# Función para cargar los datos en la lista de países
def cargar_datos_csv(ruta_archivo):
    lista_paises = []
    try:
        with open(ruta_archivo, "r", encoding="iso-8859-1") as archivo:
            
            #usamos esta linea para saltear los encabezados y que el codigo no indique error
            archivo.readline() 

            for linea in archivo:
                linea = linea.strip()
                campos = linea.split(",")

                if len(campos) == 4:
                    try:
                        pais = {"nombre": campos[0].strip(),
                                "poblacion": int(campos[1].strip()),
                                "superficie": int(campos[2].strip()),
                                "continente": campos[3].strip()}
                        lista_paises.append(pais)
                    except ValueError:
                        print(f"Error de formato (tipos de datos) en línea: {linea}. No se cargó.")
        
        print(f"Se han cargado {len(lista_paises)} países exitosamente.")
        return lista_paises
    
    except FileNotFoundError:
        print(f"Error, el archivo '{ruta_archivo}' no fue encontrado, verifique la ruta.")
        return []

#Ahora creamos la función que ejecuta la aplicación y el menu de opciones
def mostrar_menu():

    print("\n" + "="*40)
    print("      Gestor de Datos de Países")
    print("="*40)
    print("1. Agregar un país")
    print("2. Actualizar Población/Superficie")
    print("3. Buscar país por nombre")
    print("4. Filtrar países (Continente, Rango, etc.)")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Mostrar todos los países") 
    print("0. Salir")
    print("="*40)

    while True:
        opcion = input("Ingrese el numero de la opcion correspondiente: ")
        if opcion.isdigit():
            return int(opcion)
        print("Opcion invalida, ingrese solo el número")



def mostrar_todos_los_paises(lista_paises):
    if not lista_paises:
        print("La lista de paises esta vacía")
        return
    
    print("\n--- Lista Completa de Paises ---")
    for pais in lista_paises:
        print(f"{pais['nombre']} | Pob.: {pais['poblacion']:,} | Sup.: {pais['superficie']:,} km² | Cont.: {pais['continente']}")
    print("-"*40)


#Aca definimos la función principal del programa
def main():
    global PAISES

    nombre_archivo = "dataset.csv"
    PAISES = cargar_datos_csv(nombre_archivo)

    if not PAISES:
        print("Programa terminado: no se pudieron cargar los datos iniciales")
        return
    
    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            agregar_pais(PAISES)
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            mostrar_todos_los_paises(PAISES)
        elif opcion == 0:
            print("Gracias por usar el GESTOR DE PAÍSES!")
            break
        else:
            print("Opción inválida, vuelva a interntarlo")


def pedir_entero(mensaje):
    while True:
        valor_str = input(mensaje).strip()

        if not valor_str:
            print("El campo no puede estar vacío")
            continue

        try:
            valor = int(valor_str)
            if valor >=0:
                return valor
            else:
                print("El valor debe ser un número entero positivo o 0")
        except ValueError:
            print("Entrada inválida, por favor ingrese un número valido")



#funcion para agregar países
def agregar_pais(lista_paises):
    print("\n--- Agregar nuevo país ---")

    while True:
        nombre = input("Ingrese el nombre del país: ").strip().capitalize()
        if nombre:
            break
        print("El nombre no puede estar vacío")

    while True:
        continente = input("Ingrese el continente del país: ").strip().capitalize()
        if continente:
            break
        print("El continente no puede estar vacío")

    poblacion = pedir_entero("Ingrese la población (solo números): ")
    superficie = pedir_entero("Ingrese la superficie en Km² (solo números): ")

    nuevo_pais = {'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
        }

    lista_paises.append(nuevo_pais)
    print(f"\n País '{nombre}' Agregado exitosamente")
    print(f"Total de países: {len(lista_paises)}")




#definimos punto de entrada par el programa con una lista inicial vacía
PAISES = []
if __name__ == "__main__":
    main()

