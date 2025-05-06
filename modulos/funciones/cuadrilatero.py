# Definir 3 funciones... Cálculo de perimetro, área y volumen...

def perimetro(Lado_1,lado_2):
    resultado = Lado_1 + lado_2 * 2
    return resultado

def area(ancho,largo):
    return ancho * largo

def volumen(ancho,largo,alto):
    return ancho * largo * alto

print(perimetro(2,3))
print(area(2,3))
print(volumen(2,3,4))