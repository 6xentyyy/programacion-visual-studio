# Usamos el ciclo FOR para recorrer elementos de un grupo de datos
juegos = ["Dota 2","MK","Street Fighter","Counter Strike","7DaystoDie"]
numeros = [10,20,30,40]
diccionario = {
    "nombre":"6xetny",
    "apellido":"Que sea la ultima vez",
    "edad":"18",
    "estudiante":False
}

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


print()
for elemento in diccionario:
   print(f"La clave del dato es: {elemento}")


for elemento in diccionario.items():
     clave = elemento[0]
     valor = elemento[1]
     print(f"La clave del dato es: '{clave}' y el valor es: '{valor}'")


conjunto = {"El BigPiroca",55,True,"YaTuSabe",23}

print()
for elemento in conjunto:
    if type(elemento) == str:
     print(elemento) 