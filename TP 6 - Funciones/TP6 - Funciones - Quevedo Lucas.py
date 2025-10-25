#TP6 - Funciones - Quevedo Lucas



#1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola_mundo():
    print("Hola mundo!")

imprimir_hola_mundo()


#2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre = input("Ingrese su nombre: ")
print(saludar_usuario(nombre))


#3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal (nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su pais de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)


#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
# como parámetro y devuelva el área del círculo. calcular_perimetro_
# circulo(radio) que reciba el radio como parámetro y devuelva
# el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
# funciones para mostrar los resultados.

import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingresá el radio del círculo: "))

print(f"Área: {calcular_area_circulo(radio):.2f}")
print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")


#5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar
# el resultado usando esta función.

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingresá una cantidad de segundos: "))
print(f"Horas: {segundos_a_horas(segundos):.1f}")


#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

num_tabla = int(input("Ingresá un número para su tabla de multiplicar: "))

tabla_multiplicar(num_tabla)


#7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado
# de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
# de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return suma, resta, multiplicacion, division

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

suma, resta, multiplicacion, division = operaciones_basicas(a, b)

print(f"La suma de los números es: {suma}, la resta de los numeros es: {resta}, la miltuplicación es: {multiplicacion} y la división es: {division}")


#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
# para mostrar el resultado con dos decimales.

#IMC = Peso(kg) / altura(m) x altura(m) = kg/m2
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en Kilogramos: "))
altura = float(input("Ahora ingrese su altura en metros: "))

IMC = calcular_imc(peso, altura)

print(f"Tu indice de masa corporal es de {IMC:.2f}kg/m2")


#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

#formula de C a F = (°C x 1,8) + 32.

def celsius_a_fahrenheit(celsius):
    return (celsius * 1.8) + 32

celsius = float(input("Ingresá la temperatura en °C: "))

print(f"°{celsius} a Fahrenheit son: °{celsius_a_fahrenheit(celsius):.2f}")


#10. Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingrese el primero número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(a, b, c)

print(f"El promedio es {promedio:.1f}")



#Fin