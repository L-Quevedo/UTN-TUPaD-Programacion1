#TP9 - Recursividad - Quevedo Lucas

#1. Crea una función recursiva que calcule el factorial de un número. 
# Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

numero_limite = int(input("Ingrese un número positivo para convertir a binario: "))

if numero_limite < 0:
    print("El factorial no se puede ejecutar en numeros negativos")
else:
    print(f"\n--- Calculando factoruales desde 1 hasta {numero_limite} ---")

    for i in range(1, numero_limite + 1):
        resultado = factorial(i)
        print(f"El factorial de {i} es: {resultado}")


#2. Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci (num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci (num - 2)

posicion_limite = int(input("Ingrese hasta que posición de la serie de Fibonacci desea calcular: "))

if posicion_limite < 0:
    print("Errir, la posición debe ser un número entero positivo")
else:
    print(f"\n --- Serie de Fibonacci hasta la posición {posicion_limite} ---")

    for i in range(posicion_limite + 1):
        resultado = fibonacci(i)
        print(f"Fibonacci({i}) = {resultado}")


#3. Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
# utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)

base = int(input("Ingrese el número base: "))
exponente = int(input("Ingrese el número exponente (entero positivo): "))

if exponente < 0:
    print("Error, el exponente debe ser un numero positivo")
else:
    resultado = potencia_recursiva(base, exponente)
    print(f"\nEl resultado de {base} elevado a la {exponente} es: {resultado}")


#4. Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.
# Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y unos (1), en base 2. 
# Para convertir un número decimal a binario, se puede seguir este procedimiento:
#a. Dividir el número por 2.
#b. Guardar el resto (0 o 1).
#c. Repetir el proceso con el cociente hasta que llegue a 0.
#d. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.

def decimal_a_binario(num):
    if num < 2:
        return str(num)
    else:
        return decimal_a_binario(num // 2) + str(num % 2)

num_decimal = int(input("Ingrese un número entero positivo: "))

if num_decimal < 0:
    print("El numero debe ser positivo")
else:
    resultado_binario = decimal_a_binario(num_decimal)
    print(f"\nEl número decimal {num_decimal} en binario e {resultado_binario}")



#Fin