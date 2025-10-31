#TP8 - Manejo de archivos - Quevedo Lucas

#1. Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos. 
# Cada línea debe tener: nombre,precio,cantidad

with open("productos.txt", "w") as archivo:
    archivo.write("Lapicera,40,120\n")
    archivo.write("Cuaderno,60,80\n")
    archivo.write("Regla,34,58\n")


#2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea, la procese con .strip() y .split(","), 
# y muestre los productos en el siguiente formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

with open("productos.txt","r") as archivo:
    for archivo_limpio in archivo:
        mostrar_producto = archivo_limpio.strip()
        partes = mostrar_producto.split(",")
        nombre = partes[0]
        precio = partes[1]
        cantidad = partes[2]

        print(f"El producto {nombre} tiene un valor de {precio} y hay {cantidad} en stock")


#3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos, 
# le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad) y lo agregue al archivo sin borrar el contenido existente.

nuevo_nombre = input("Ingrese un nuevo producto: ")
nuevo_precio = input("Ingrese el precio del nuevo prodcuto: ")
nuevo_cantidad = input("Ingrese la cantidad en stock de ese producto: ")

with open("productos.txt","a") as archivo:
    nuevo_producto = f"{nuevo_nombre},{nuevo_precio},{nuevo_cantidad}\n"
    archivo.write(nuevo_producto)

    print(f"Se ah agregado {nuevo_nombre} como nuevo producto al archivo")


#4. Cargar productos en una lista de diccionarios: 
# Al leer el archivo, cargar los datos en una lista llamada productos, 
# donde cada elemento sea un diccionario con claves: nombre, precio, cantidad.

datos_del_archivo = ["manzana,500.50,150","banana,350.75,220","leche,980.00,80","pan,200.00,100"]

productos = []

for linea in datos_del_archivo:
    partes = linea.strip().split(',')
    if len(partes) == 3:
        nombre_prod = partes[0].strip()
        precio_prod = float(partes[1].strip())
        cantidad_prod = int(partes[2].strip())
        producto_diccionario = {"nombre": nombre_prod,"precio": precio_prod,"cantidad": cantidad_prod}
        productos.append(producto_diccionario)
    else:
        print(f"Advertencia: La línea '{linea.strip()}' no tiene el formato esperado y fue omitida.")

print(productos)

print(f"El precio de la {productos[0]['nombre']} es ${productos[0]['precio']}.")


#5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. 
# Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si no existe, mostrar un mensaje de error.

productos = [
    {'nombre': 'manzana', 'precio': 500.5, 'cantidad': 150},
    {'nombre': 'banana', 'precio': 350.75, 'cantidad': 220},
    {'nombre': 'leche', 'precio': 980.0, 'cantidad': 80},
    {'nombre': 'pan', 'precio': 200.0, 'cantidad': 100}
]

nombre_buscado = input("Ingrese el nombre del producto a buscar: ").lower()

encontrado = False

for producto_actual in productos:
    if producto_actual["nombre"] == nombre_buscado:
        encontrado = True
        print("\n--- ¡Producto Encontrado! ---")
        print(f"Nombre: {producto_actual['nombre'].capitalize()}")
        print(f"Precio: ${producto_actual['precio']:.2f}")
        print(f"Cantidad en Stock: {producto_actual['cantidad']} unidades")
        print("----------------------------")
        break 

if not encontrado:
    print(f"Error: El producto '{nombre_buscado}' no se encuentra en el inventario.")


#6. Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, 
# sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista.

productos = [
    {'nombre': 'manzana', 'precio': 500.5, 'cantidad': 150},
    {'nombre': 'banana', 'precio': 350.75, 'cantidad': 220},
    {'nombre': 'leche', 'precio': 980.0, 'cantidad': 80},
    {'nombre': 'pan', 'precio': 200.0, 'cantidad': 100},
    {'nombre': 'tomate', 'precio': 450.0, 'cantidad': 50}
]

nombre_archivo = "productos.txt"

print("Iniciando el proceso de guardado y sobrescritura...")

with open(nombre_archivo, 'w') as archivo:
    for producto_actual in productos:
        nombre = producto_actual["nombre"]
        precio = str(producto_actual["precio"]) 
        cantidad = str(producto_actual["cantidad"])
        linea_a_escribir = f"{nombre},{precio},{cantidad}\n"
        archivo.write(linea_a_escribir)

print(f"Guardado completado, el archivo '{nombre_archivo}' ha sido sobrescrito con los datos actualizados.")



#Fin.