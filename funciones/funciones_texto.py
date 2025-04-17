nombre = "Oe loquito"
apellido = "Teni un cigarro"
nombre_completo = nombre + apellido

nombre_mayusculas = nombre.upper()
apellido_mayusculas = apellido.upper()

nombre_minusculas = nombre_mayusculas.lower()
apellido_minusculas = apellido_mayusculas.lower()

nombre_titulo = nombre.title()
apellido_titulo = apellido.title()

print(nombre_completo.endswith("o"))

print(f"Hola admirable y maravilloso {nombre} {apellido} {3+4}")
print(f"Nombre y apellido en mayúsculas: {nombre_mayusculas} {apellido_mayusculas}")
print(f"Nombew y apellido en miúsculas: {nombre_minusculas} {apellido_minusculas}")
print(f"Nombre y apellido como título: {nombre_titulo} {apellido_titulo}")