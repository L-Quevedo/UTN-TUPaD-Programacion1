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

