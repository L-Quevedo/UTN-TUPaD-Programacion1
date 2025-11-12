# TPI - Gestión de datos de países

# Profesores: Virginia Cimino,
# Alumnos: Quevedo Lucas, Aramburu Juan
# Grupo: 58

import os
from pathlib import Path

# creamos la funcion para cargar los datos en el archivo CSV
# Función para cargar los datos en la lista de países
def cargar_datos_csv(ruta_archivo):
    lista_paises = []
    try:
        with open(ruta_archivo, "r", encoding="iso-8859-1") as archivo:
            
            # usamos esta linea para saltear los encabezados y que el codigo no indique error
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
        print(f"Error, el archivo en '{ruta_archivo}' no fue encontrado, verifique la ruta.")
        return []

# Ahora creamos la función que ejecuta la aplicación y el menu de opciones
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


# funcion que ayuda
def imprimir_lista_paises(lista_paises):
    if not lista_paises:
        print("La lista de paises esta vacía o no hay resultados.")
        return
    
    # Formateo para que se vea como una tabla
    print("-" * 80)
    for i, pais in enumerate(lista_paises):
        print(f"{i+1:3}. {pais['nombre']:<30} | Pob.: {pais['poblacion']:<15,} | Sup.: {pais['superficie']:<15,} km² | Cont.: {pais['continente']}")
    print("-" * 80)
    print(f"Total de países mostrados: {len(lista_paises)}")


def mostrar_todos_los_paises(lista_paises):
    if not lista_paises:
        print("La lista de paises esta vacía")
        return

    print("\n--- 7. Lista Completa de Paises ---")
    imprimir_lista_paises(lista_paises) # Ahora usa la función ayudante


# Aca definimos la función principal del programa
def main():
    global PAISES

    # Corrección para que siempre encuentre el CSV
    carpeta_del_script = Path(__file__).parent
    nombre_archivo_completo = carpeta_del_script / "dataset.csv"

    PAISES = cargar_datos_csv(nombre_archivo_completo)

    if not PAISES:
        print("Programa terminado: no se pudieron cargar los datos iniciales")
        return
    
    while True:
        opcion = mostrar_menu()

        if opcion == 1:
            agregar_pais(PAISES)
        elif opcion == 2:
            actualizar_pais(PAISES) 
        elif opcion == 3:
            buscar_pais(PAISES)     
        elif opcion == 4:
            filtrar_paises(PAISES) 
        elif opcion == 5:
            ordenar_paises(PAISES)
        elif opcion == 6:
            mostrar_estadisticas(PAISES)
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



# funcion para agregar países
def agregar_pais(lista_paises):
    print("\n--- 1. Agregar nuevo país ---")

    while True:
        nombre = input("Ingrese el nombre del país: ").strip().capitalize()
        if nombre:
            # Validación para no duplicar países
            existe = False
            for pais in lista_paises:
                if pais['nombre'].lower() == nombre.lower():
                    print(f"Error: El país '{nombre}' ya existe en la lista.")
                    existe = True
                    break
            if not existe:
                break
        else:
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


# funcion que ayuda a buscar y seleccionar un solo pais en la lista

def seleccionar_pais(lista_paises):

    print("\n--- Selección de País ---")
    termino_busqueda = input("Ingrese el nombre del país a seleccionar: ").strip()

    if not termino_busqueda:
        print("Error: El término de búsqueda no puede estar vacío.")
        return None

    # Buscamos coincidencias
    resultados = []
    termino_lower = termino_busqueda.lower()
    for pais in lista_paises:
        if termino_lower in pais['nombre'].lower():
            resultados.append(pais)

    # Evaluamos resultados
    if not resultados:
        print(f"\nNo se encontraron países que coincidan con '{termino_busqueda}'.")
        return None

    if len(resultados) == 1:
        pais_encontrado = resultados[0]
        print(f"\nPaís encontrado: {pais_encontrado['nombre']}")
        return pais_encontrado

    # Si hay múltiples, le pedimos al usuario que elija
    print(f"\nSe encontraron {len(resultados)} coincidencias. Por favor, elija uno:")
    for i, pais in enumerate(resultados):
        print(f"  {i+1}. {pais['nombre']}")

    while True:
        opcion_str = input(f"Ingrese el número (1-{len(resultados)}) o 0 para cancelar: ")
        if not opcion_str.isdigit():
            print("Error: Debe ingresar un número.")
            continue

        opcion_num = int(opcion_str)

        if opcion_num == 0:
            return None # Cancelar

        if 1 <= opcion_num <= len(resultados):
            pais_seleccionado = resultados[opcion_num - 1]
            print(f"País seleccionado: {pais_seleccionado['nombre']}")
            return pais_seleccionado
        else:
            print(f"Error: Opción inválida. Ingrese un número entre 1 y {len(resultados)}.")

def actualizar_pais(lista_paises):
    print("\n--- 2. Actualizar Población/Superficie ---")

    # Primero, encontramos el país
    pais_a_modificar = seleccionar_pais(lista_paises)

    if pais_a_modificar is None:
        print("Proceso de actualización cancelado.")
        return 

    # Mostramos los datos actuales
    print("\nDatos actuales del país:")
    print(f"  Nombre: {pais_a_modificar['nombre']}")
    print(f"  Población: {pais_a_modificar['poblacion']:,}")
    print(f"  Superficie: {pais_a_modificar['superficie']:,} km²")
    print("-" * 30)

    # Preguntamos que actualizar
    print("¿Qué dato desea actualizar?")
    print("  1. Población")
    print("  2. Superficie")

    while True:
        opcion = input("Ingrese 1 o 2 (o 0 para cancelar): ").strip()

        if opcion == '1':
            nueva_poblacion = pedir_entero(f"Ingrese la nueva población para {pais_a_modificar['nombre']}: ")
            pais_a_modificar['poblacion'] = nueva_poblacion
            print("¡Población actualizada exitosamente!")
            break
        elif opcion == '2':
            nueva_superficie = pedir_entero(f"Ingrese la nueva superficie (km²) para {pais_a_modificar['nombre']}: ")
            pais_a_modificar['superficie'] = nueva_superficie
            print("¡Superficie actualizada exitosamente!")
            break
        elif opcion == '0':
            print("Actualización cancelada.")
            break
        else:
            print("Opción inválida. Por favor, ingrese solo 1, 2 o 0.")

    print("\nDatos actualizados:")
    print(f"{pais_a_modificar['nombre']} | Pob.: {pais_a_modificar['poblacion']:,} | Sup.: {pais_a_modificar['superficie']:,} km²")


def buscar_pais(lista_paises):
    print("\n--- 3. Buscar País por Nombre ---")

    termino_busqueda = input("Ingrese el nombre (o parte del nombre) del país a buscar: ").strip()

    if not termino_busqueda:
        print("Error: El término de búsqueda no puede estar vacío.")
        return

    resultados = []

    for pais in lista_paises:
        nombre_pais = pais['nombre'].lower()
        termino_lower = termino_busqueda.lower()

        if termino_lower in nombre_pais:
            resultados.append(pais)

    if not resultados:
        print(f"\nNo se encontraron países que coincidan con '{termino_busqueda}'.")
    else:
        print(f"\nSe encontraron {len(resultados)} coincidencias para '{termino_busqueda}':")
        imprimir_lista_paises(resultados)
    

# opcion4, filtro

def _filtrar_por_continente(lista_paises):
    print("\n--- Filtro por Continente ---")
    continente_buscado = input("Ingrese el nombre del continente: ").strip().capitalize()
    
    if not continente_buscado:
        print("Error: El continente no puede estar vacío.")
        return

    resultados = []
    for pais in lista_paises:
        # Comparamos ambos capitalizados para ser flexibles
        if pais['continente'].capitalize() == continente_buscado:
            resultados.append(pais)
            
    if not resultados:
        print(f"No se encontraron países en el continente '{continente_buscado}'.")
    else:
        print(f"\n--- Países encontrados en '{continente_buscado}' ---")
        imprimir_lista_paises(resultados)

def _filtrar_por_rango_poblacion(lista_paises):
    print("\n--- Filtro por Rango de Población ---")
    pob_min = pedir_entero("Ingrese la población MÍNIMA: ")
    pob_max = pedir_entero("Ingrese la población MÁXIMA: ")
    
    if pob_min > pob_max:
        print("Error: El valor mínimo no puede ser mayor al máximo.")
        return

    resultados = []
    for pais in lista_paises:
        if pob_min <= pais['poblacion'] <= pob_max:
            resultados.append(pais)
            
    if not resultados:
        print(f"No se encontraron países con población entre {pob_min:,} y {pob_max:,}.")
    else:
        print(f"\n--- Países con población entre {pob_min:,} y {pob_max:,} ---")
        imprimir_lista_paises(resultados)

def _filtrar_por_rango_superficie(lista_paises):
    print("\n--- Filtro por Rango de Superficie ---")
    sup_min = pedir_entero("Ingrese la superficie MÍNIMA (km²): ")
    sup_max = pedir_entero("Ingrese la superficie MÁXIMA (km²): ")
    
    if sup_min > sup_max:
        print("Error: El valor mínimo no puede ser mayor al máximo.")
        return

    resultados = []
    for pais in lista_paises:
        if sup_min <= pais['superficie'] <= sup_max:
            resultados.append(pais)
            
    if not resultados:
        print(f"No se encontraron países con superficie entre {sup_min:,} y {sup_max:,} km².")
    else:
        print(f"\n--- Países con superficie entre {sup_min:,} y {sup_max:,} km² ---")
        imprimir_lista_paises(resultados)

def filtrar_paises(lista_paises):
    print("\n--- 4. Filtrar Países ---")
    
    while True:
        print("\nOpciones de Filtro:")
        print("  1. Por Continente")
        print("  2. Por Rango de Población")
        print("  3. Por Rango de Superficie")
        print("  0. Volver al Menú Principal")
        
        opcion = input("Seleccione una opción de filtro: ").strip()
        
        if opcion == '1':
            _filtrar_por_continente(lista_paises)
        elif opcion == '2':
            _filtrar_por_rango_poblacion(lista_paises)
        elif opcion == '3':
            _filtrar_por_rango_superficie(lista_paises)
        elif opcion == '0':
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")


# opcion 5 ordenar

def _pedir_orden():
    while True:
        orden = input("Seleccione el orden: 1. Ascendente | 2. Descendente: ").strip()
        if orden == '1':
            return False  # reverse=False es Ascendente
        elif orden == '2':
            return True   # reverse=True es Descendente
        else:
            print("Opción inválida. Ingrese 1 o 2.")

def ordenar_paises(lista_paises):
    print("\n--- 5. Ordenar Países ---")
    
    while True:
        print("\nOpciones de Ordenamiento:")
        print("  1. Por Nombre")
        print("  2. Por Población")
        print("  3. Por Superficie")
        print("  0. Volver al Menú Principal")
        
        opcion = input("Seleccione una opción de ordenamiento: ").strip()
        
        # Hacemos una copia para no modificar la lista original al ordenar
        lista_a_ordenar = lista_paises.copy()
        
        if opcion == '1':
            es_descendente = _pedir_orden()
            lista_a_ordenar.sort(key=lambda pais: pais['nombre'].lower(), reverse=es_descendente)
            orden_str = "Descendente (Z-A)" if es_descendente else "Ascendente (A-Z)"
            print(f"\n--- Lista ordenada por Nombre ({orden_str}) ---")
            imprimir_lista_paises(lista_a_ordenar)
            
        elif opcion == '2':
            es_descendente = _pedir_orden()
            lista_a_ordenar.sort(key=lambda pais: pais['poblacion'], reverse=es_descendente)
            orden_str = "Descendente (Mayor a Menor)" if es_descendente else "Ascendente (Menor a Mayor)"
            print(f"\n--- Lista ordenada por Población ({orden_str}) ---")
            imprimir_lista_paises(lista_a_ordenar)

        elif opcion == '3':
            es_descendente = _pedir_orden()
            lista_a_ordenar.sort(key=lambda pais: pais['superficie'], reverse=es_descendente)
            orden_str = "Descendente (Mayor a Menor)" if es_descendente else "Ascendente (Menor a Mayor)"
            print(f"\n--- Lista ordenada por Superficie ({orden_str}) ---")
            imprimir_lista_paises(lista_a_ordenar)

        elif opcion == '0':
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")


# estadisticas opcion 6

def mostrar_estadisticas(lista_paises):
    print("\n--- 6. Estadísticas Globales ---")

    if not lista_paises:
        print("No hay países cargados para mostrar estadísticas.")
        return

    # Inicializamos variables
    total_poblacion = 0
    total_superficie = 0
    pais_max_pob = lista_paises[0]
    pais_min_pob = lista_paises[0]
    conteo_continentes = {}

    # Recorremos la lista una sola vez para calcular todo
    for pais in lista_paises:
        total_poblacion += pais['poblacion']
        total_superficie += pais['superficie']
        
        # Min/Max Población
        if pais['poblacion'] > pais_max_pob['poblacion']:
            pais_max_pob = pais
        if pais['poblacion'] < pais_min_pob['poblacion']:
            pais_min_pob = pais
            
        # Conteo por Continente
        continente = pais['continente'].capitalize()
        conteo_continentes[continente] = conteo_continentes.get(continente, 0) + 1

    # Calculamos promedios
    cantidad_paises = len(lista_paises)
    promedio_poblacion = total_poblacion / cantidad_paises
    promedio_superficie = total_superficie / cantidad_paises

    # Imprimimos resultados
    print("\n--- Población ---")
    print(f"País con Mayor Población: {pais_max_pob['nombre']} ({pais_max_pob['poblacion']:,})")
    print(f"País con Menor Población: {pais_min_pob['nombre']} ({pais_min_pob['poblacion']:,})")
    print(f"Promedio de Población Global: {promedio_poblacion:,.2f}")

    print("\n--- Superficie ---")
    print(f"Promedio de Superficie Global: {promedio_superficie:,.2f} km²")
    
    print("\n--- Continentes ---")
    print("Cantidad de países por continente:")
    for continente, cantidad in conteo_continentes.items():
        print(f"  - {continente}: {cantidad} país(es)")
    
    print("-" * 40)


# definimos punto de entrada par el programa con una lista inicial vacía
PAISES = []
if __name__ == "__main__":
    main()