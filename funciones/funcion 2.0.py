def calcular():
    print("¿Qué operación deseas hacer?")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    opcion = input("Elige una opción (1/2/3/4): ")

    if opcion in ['1', '2', '3', '4']:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        
        if opcion == '1':
            resultado = num1 + num2
            operacion = "suma"
        elif opcion == '2':
            resultado = num1 - num2
            operacion = "resta"
        elif opcion == '3':
            resultado = num1 * num2
            operacion = "multiplicación"
        elif opcion == '4':
            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
                return
            resultado = num1 / num2
            operacion = "división"

        print(f"El resultado de la {operacion} es: {resultado}")
    else:
        print("Opción no válida.")

# Ejecutar la función
calcular()