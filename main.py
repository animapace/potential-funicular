# 1. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número leído.

lista = []
for _ in range(10):
    valor = int(input("Ingrese valor: "))
    lista.append(valor)

mayor = lista[0]
posicion = 0
for i in range(1, 10):
    if lista[i] > mayor:
        mayor = lista[i]
        posicion = i

print("Lista completa:", lista)
print("Mayor de la lista:", mayor)
print("Posición del mayor número:", posicion)

# 2. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número par leído.

def mayorPar(numeros):
    mayor = -1
    posicion = -1
    for i, v in enumerate(numeros):
        if v % 2 == 0 and v > mayor:
            mayor = v
            posicion = i
    return (mayor, posicion)

numeros = []
for _ in range(10):
    valor = int(input("Ingrese valor: "))
    numeros.append(valor)

mayor, posicion = mayorPar(numeros)
print("Mayor número par:", mayor)
print("Posición del mayor número par:", posicion)

# 3. Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número primo leído.

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, math.ceil(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True

numeros = []
for _ in range(10):
    valor = int(input("Ingrese valor: "))
    numeros.append(valor)

mayor_primo = -1
posicion = -1
for i, numero in enumerate(numeros):
    if es_primo(numero) and numero > mayor_primo:
        mayor_primo = numero
        posicion = i

print("Mayor número primo:", mayor_primo)
print("Posición del mayor número primo:", posicion)


# 4. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los almacenados en dicho arreglo comienzan en dígito primo
def es_digito_primo(digito):
    primos = [2, 3, 5, 7]
    return digito in primos

numeros = []
for _ in range(10):
    numero = int(input("Introduce un número entero: "))
    numeros.append(numero)

contador = 0
for numero in numeros:
    primer_digito = int(str(numero)[0])
    if es_digito_primo(primer_digito):
        contador += 1

print(f"Cantidad de números que comienzan con un dígito primo: {contador}")



# 5. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición se encuentra el número primo con mayor cantidad de dígitos pares
def es_primo(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
def contar_digitos_pares(numero):
    conteo = 0
    for digito in str(numero):
        if int(digito) % 2 == 0:
            conteo += 1
    return conteo


numeros = []
for _ in range(10):
    numero = int(input("Introduce un número entero: "))
    numeros.append(numero)

max_digitos_pares = -1
posicion_max_digitos_pares = -1

for i, numero in enumerate(numeros):
    if es_primo(numero):
        digitos_pares = contar_digitos_pares(numero)
        if digitos_pares > max_digitos_pares:
            max_digitos_pares = digitos_pares
            posicion_max_digitos_pares = i

if posicion_max_digitos_pares != -1:
    print(f"La posición del número primo con la mayor cantidad de dígitos pares es: {posicion_max_digitos_pares}")
else:
    print("No hay números primos en la lista.")

# 6. Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se encuentran los números con más de 3 dígitos.

numeros = [468, 6524, 2698, 458, 39459, 22] 
resultado = list(filter(lambda n: len(str(n[1])) > 3, enumerate(numeros)))
for i in resultado:
    print(f"El {i[1]} se encuentra en la posición {i[0]}")

# 7. Leer 10 números enteros, almacenarlos en una lista y determinar a cuánto es igual el promedio entero de los datos de la lista.

numeros = [4, 6, 32, 6, 3, 5, 37, 2, 1, 7]  
promedio = sum(numeros) // len(numeros)
print("Promedio entero de los datos de la lista:", promedio)

# 8. Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números negativos hay.

numeros = [8, -6, 32, -6, 3, 5, -4, -2, 1, 7]  
numeros_negativos = len(list(filter(lambda n: n < 0, numeros)))
print("Números negativos:", numeros_negativos)

# 9. Leer 10 números enteros, almacenarlos en una lista y calcular la factorial a cada uno de los números leídos almacenados en otra lista.

numeros = [4, -6, 32, -6, 3, 5, 37, -2, 1, 7]  
factoriales = [factorial(n) for n in numeros if n >= 0]
print("Factoriales de los números:", factoriales)

# 10. Leer 10 números enteros, almacenarlos en una lista. Luego leer un entero y determinar cuántos divisores exactos tiene este último número entre los valores almacenados en la lista.
numeros = [4, -6, 32, -6, 3, 5, 37, -2, 1, 7]  
divisor = int(input("Ingrese un número para verificar divisores: "))
divisores = len(list(filter(lambda n: n != 0 and divisor % n == 0, numeros)))
print("Número de divisores exactos:", divisores)



