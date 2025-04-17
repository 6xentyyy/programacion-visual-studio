import math

numeros = [2,4,6,9,10,14]
decimal = 69.4269

print(f"El número mayor de la lista {numeros} es {max(numeros)}")
print(f"El número menor de la lista {numeros} es {min(numeros)}")

print(f"Redondear el decimal {decimal} = {round(decimal)}")
print(f"Redondear el decimal {decimal} a 2 decimales = {round(decimal)}")
print(f"Truncar el decimal {decimal} = {math.trunc(decimal)}")
print(f"Valor absuluto de -45= {math.fabs(-45)}")