#TP7 - Datos complejos - Quevedo Lucas


#1. Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)


#2. Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)


#3. Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, 
# crear una lista que contenga únicamente las frutas sin los precios.

print(precios_frutas.keys())


#4. Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

contacto = {}

for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefónico: ")
    contacto [nombre] = numero

consulta = input("Ingrese un contacto para buscar: ")

if consulta in contacto:
    print(f"El número de {consulta} es: {contacto[consulta]}")
else:
    print("El contacto no exíste")


#5. Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)

recuento = {}

for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1

print(f"Las palabras utilizadas son: {palabras}")
print(f"La cantidad de palabras utilizadas es: {recuento}")


#6. Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

alumnos = {}





#7. Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1 = {1,2,3,4,5,6}
parcial_2 = {2,3,6,8,9,10}

ambos_parciales = parcial_1 & parcial_2
solo_uno_de_los_parciales = parcial_1 ^ parcial_2
al_menos_uno = parcial_1 | parcial_2

print(f"Los alumnos que aprobaron ambos parciales son: {ambos_parciales}")
print(f"Los alumnos que aprobaron solo uno de los parciales son: {solo_uno_de_los_parciales}")
print(f"Los alumnos que aprobaron al menos un parcial son: {ambos_parciales}")


#8. Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

stock_productos = {"harina":10,"manteca":8,"yerba":24,"gaseosa":20,"azucar":3,"aceite":2,"leche":5,"jabon":1}

print(f"Stock de productos {stock_productos}")

producto = input("Ingrese el nombre del producto: ")

for producto in stock_productos:
    print(f"Stock actual de {producto}: {stock_productos[producto]}")
    agregar = int(input("Cuantas unidades desea agregar al stock?"))
    stock_productos[producto] += agregar
    print(f"El nuevo stock de {producto}: {stock_productos}")
else:
    print(f"{producto} no existe en el inventario")
    nuevo_stock = int(input("Ingrse el stock inicial para este produto: "))
    stock_productos[producto] = nuevo_stock
    print(f"{producto} agregado con {nuevo_stock} unidades")

print("Stock actualizado")
print(stock_productos)


#9. Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Permití consultar qué actividad hay en cierto día y hora.



#10. Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.