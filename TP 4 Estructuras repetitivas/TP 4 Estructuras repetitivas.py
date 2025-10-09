#TP 4 - Estructuras repetitivas - Quevedo Lucas


#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

(print("Números enteros: "))
for i in range(0, 101):
    print(i)


#2)  Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero = (input("Ingrese un número entero: "))
print("El número tiene", len(numero.lstrip('-')), "dígitos.")


#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

numero_1 = int(input("Ingrese el primer valor: "))
numero_2 = int(input("Ingrese el segundo valor: "))
suma = 0

for i in range(min(numero_1, numero_2) + 1, max(numero_1, numero_2)):
    suma += i
print("Suma entre los valores (excluidos): ", suma)


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

total = 0

while True:
    num = int(input("Ingresa un número entero (0 para terminar): "))
    if num == 0:
        break
    total += num

print("El total acumulado es:", total)


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random 

secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adiviná el número (0-9): "))
    intentos += 1

    if intento < secreto:
        print("Más alto.")
    elif intento > secreto:
        print("Más bajo.")
    else:
        print(f"Exacto!, fueron necesarios {intentos} intentos")
        break


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2):
    print(i)


#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.


numero = int(input("Indique un número entero positivo: "))
suma = 0

for i in range(0, numero + 1):
    suma += i

print(f"La suma de los números entre 0 y {numero} es: {suma}")


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

cantidad_numeros = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Ingresa {cantidad_numeros} números enteros:")

for i in range(cantidad_numeros):
    numero = int(input(f"Ingresa el número {i + 1}: "))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"\nResultados:")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")


#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

total = 0
cantidad = int(input("Cuantos numeros queres ingresar para la media? "))

for i in range(cantidad):
    num = int(input("Numero: "))
    total += num
print("Media:", total / cantidad)


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingrese un numero: ")

if numero.startswith("-"):
    invertido = "-" + numero[:0:-1]
else:
    invertido = numero[::-1]

print("Numero invertido:", invertido)



#Fin