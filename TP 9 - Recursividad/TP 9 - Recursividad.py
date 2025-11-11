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
# Convertir el número 10 a binario:
# 10 ÷ 2 = 5 resto: 0
# 5 ÷ 2 = 2 resto: 1
# 2 ÷ 2 = 1 resto: 0
# 1 ÷ 2 = 0 resto: 1
# Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010"

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


#5. Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, 
# y devuelva True si es un palíndromo o False si no lo es.
#Requisitos:
#La solución debe ser recursiva.
#No se debe usar [::-1] ni la función reversed()

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra_ingresada = input("Ingrse una palabra sin espacios ni tildes: ")

if es_palindromo(palabra_ingresada):
    print(f"\nResultado: True (la palabra '{palabra_ingresada}' Es un palíndromo)")
else:
    print(f"\nResultado: False (la palabra '{palabra_ingresada}' No es un palíndromo)")


#6. Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

def suma_digitos(n):
    if n < 10:
        return n
    else:
        ultimo_digito = n % 10
        resto_del_numero = n // 10
        return ultimo_digito + suma_digitos(resto_del_numero)

numero_ingresado = int(input("Ingrse un número entero positivo: "))

if numero_ingresado < 0:
    print("Erro, el número debe ser psositivo: ")
else:
    resultado = suma_digitos(numero_ingresado)
    print(f"\nLa suma de los dígitos de {numero_ingresado} es: {resultado}")


# 7) Un niño está construyendo una pirámide con bloques. 
# En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo 
# y devuelva el total de bloques que necesita para construir toda la pirámide.
# Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

numero_base = int(input("Ingrese el número de bloques en el nivel mas bajo: "))

if numero_base < 1:
    print("Error, el número mas bajo debe tener al menos 1 bloque")
else:
    resultado = contar_bloques(numero_base)
    print(f"\nSe necesitan un total de '{resultado}' bloques para construir la piramide")


#8. Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), 
# y devuelva cuántas veces aparece ese dígito dentro del número.
# Ejemplos:
# contar_digito(12233421, 2) → 3
# contar_digito(5555, 5) → 4
# contar_digito(123456, 7) → 0

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    conteo_actual = 0
    if (numero % 10) == digito:
        conteo_actual = 1
    return conteo_actual + contar_digito(numero // 10, digito)

numero_ingresado = int(input("Ingrese un número entero positivo: "))
digito_buscado = int(input("Ingrese el digito que desea contar (0-9): "))

if numero_ingresado < 0 or not (0 <= digito_buscado <= 9):
    print("Error, el numero debe ser positivo y el dígito debe estar entre 0 y 9")
else:
    resultado = contar_digito(numero_ingresado, digito_buscado)
    print(f"\nEl digito {digito_buscado} aparece '{resultado}' veces en el número {numero_ingresado}")



#Fin