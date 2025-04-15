# Definir función saludar
def saludar(nombre):
    print(f"Buen dia maquina fiera {nombre}")

nombre = input("Ingrese su nombre: ")

# Ejecuar función saludar
saludar(nombre)   

# Definir función sumar
def suma(a,b):
    resultado = a + b
    print(f"El resultado de suma {a} + {b} = {resultado}")

numero_1 = int(input("Ingrese su primer número"))
numero_2 = int(input("Ingrese su segundo número"))

# Ejecutar función suma
suma(numero_1,numero_2) 
