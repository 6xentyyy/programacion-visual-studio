# Usamos el ciclo FOR para recorrer elementos de un grupo de datos
juegos = ["Dota 2","MK","Street Fighter","Counter Strike","7DaystoDie"]
numeros = [10,20,30,40]

for juego in juegos: 
    print(juego) 

print()
for numero in numeros:
    resultado = numero * numero
    print(f"El resultado de multiplicar {numero} * {numero} = {resultado}")

print()
for num in range(5):
    print(num)

print()
for num in range(5,16):
    print(num)

print()
for num in range(5,16,5):
    print(num)

for elemento in enumerate(numeros):
    indice = elemento[0]
    valor = elemento[1]
    print(f"El índice es: {indice} y el valor es: {valor}")