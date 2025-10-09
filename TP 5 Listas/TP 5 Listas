#TP 5 - Listas - Quevedo Lucas



#1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

lista_notas = [7, 5, 9, 10, 4, 6, 8, 3, 7, 9]

print("Notas:", lista_notas)

promedio = sum(lista_notas) / len(lista_notas)
print("Promedio:", promedio)

print("Nota más alta:", max(lista_notas))
print("Nota más baja:", min(lista_notas))


#2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []

for i in range(5):
    Lista_productos = input(f"Ingrese el producto {i+1}: ")
    productos.append(Lista_productos)

print("Lista de productos:", sorted(productos))

eliminar_producto = input("Que producto desea eliminar: ")

if eliminar_producto in productos:
    productos.remove(eliminar_producto)
    print(f"Lista actualizada: {productos}")
else:
    print ("Este producto no esta en la lista")


#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

import random

numeros = [random.randint(1, 100) for i in range(15)]

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]


print("Lista completa:", numeros)
print("Pares:", pares, f"({len(pares)} números)")
print("Impares:", impares, f"({len(impares)} números)")


#4) Dada una lista con valores repetidos:
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

datos = [1,3,5,3,7,1,9,5,3]

nueva_lista = set(datos)

print(f"Sin repetidos: {nueva_lista}") 


#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

estudiantes = ["Ana", "Luis", "María", "Jorge", "Carla", "Pedro", "Daiana", "Lucas"]

print(f"Lista actual: {estudiantes}")

accion = input("¿Querés agregar o eliminar un estudiante? (agregar/eliminar): ").lower()

if accion == "agregar":
    nuevo = input("Nombre del nuevo estudiante: ").capitalize()
    estudiantes.append(nuevo)
    print(f"{nuevo} fue agregado correctamente.")
elif accion == "eliminar":
    borrar = input("Nombre del estudiante a eliminar: ").lower()
    encontrados = [e for e in estudiantes if e.lower() == borrar]
    if encontrados:
        estudiantes.remove(encontrados[0])
        print(f"{encontrados[0]} fue eliminado correctamente.")
    else:
        print("Ese estudiante no está en la lista.")
else:
    print("Opción no válida.")

print(f"Lista final actualizada: {estudiantes}")


#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

numeros = [1, 2, 3, 4, 5, 6, 7]

print(f"Lista original: {numeros}")

ultimo = numeros[-1]             
rotacion = [ultimo] + numeros[:-1] 

print(f"Lista rotada: {rotacion}")


#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

temperaturas = [
    [12, 22],
    [14, 25],
    [10, 20],
    [9, 24],
    [11, 21],
    [13, 26],
    [15, 27]
]

prom_min = sum(t[0] for t in temperaturas) / len(temperaturas)
prom_max = sum(t[1] for t in temperaturas) / len(temperaturas)

print(f"Promedio mínimas: {prom_min:.2f}")
print(f"Promedio máximas: {prom_max:.2f}")

amplitudes = [t[1] - t[0] for t in temperaturas]

mayor = max(amplitudes)
dia_mayor = amplitudes.index(mayor) + 1

print(f"La mayor amplitud térmica fue de {mayor}° el día {dia_mayor}.")


#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

notas = [
    [7, 8, 6],
    [5, 6, 7],
    [9, 8, 10],
    [6, 5, 6],
    [8, 9, 7]
]

for i, fila in enumerate(notas, start=1):
    prom = sum(fila) / len(fila)
    print(f"Promedio del estudiante {i}: {prom:.2f}")

print()

for j in range(3):
    prom = sum(notas[i][j] for i in range(5)) / 5
    print(f"Promedio de la materia {j+1}: {prom:.2f}")


#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero():
    for fila in tablero:
        print(" ".join(fila))
    print()

mostrar_tablero()

while True:
    jugador = input("Jugador (X/O): ").upper()
    fila = int(input("Ingrese la fila (0-2): "))
    columna = int(input("Ingrese la columna (0-2): "))

    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
    else:
        print("Esa casilla ya está ocupada.")

    mostrar_tablero()


#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.

ventas = [
    [10, 12, 8, 15, 7, 9, 11],
    [5, 6, 7, 5, 8, 9, 10],
    [20, 18, 22, 19, 25, 17, 21],
    [9, 8, 10, 12, 11, 13, 14]
]

for i, fila in enumerate(ventas, start=1):
    total = sum(fila)
    print(f"Total vendido del producto {i}: {total}")

print()

totales_dia = [sum(ventas[i][j] for i in range(4)) for j in range(7)]

for d, total in enumerate(totales_dia, start=1):
    print(f"Total del día {d}: {total}")

dia_max = totales_dia.index(max(totales_dia)) + 1
print(f"\nEl día con más ventas fue el día {dia_max} con {max(totales_dia)} ventas.")

totales_prod = [sum(fila) for fila in ventas]
prod_max = totales_prod.index(max(totales_prod)) + 1
print(f"El producto más vendido fue el producto {prod_max} con {max(totales_prod)} ventas.")



#Fin