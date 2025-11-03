# Programa: Ejemplo de concatenación de cadenas

# 1. Usando el operador +
nombre = "Jonathan"
apellido = "Bailon"
nombre_completo = nombre + " " + apellido
print("Usando +: " + nombre_completo)

# 2. Usando el método print
edad = 25
print("Usando comas:", "Nombre:", nombre_completo, ", Edad:", edad)

# 3. Usando f-strings
ciudad = "Guayaquil"
pais = "Ecuador"
profesion = "Ingeniero"
presentacion = f"Hola, soy {nombre_completo}, tengo {edad + 1} años y soy {profesion} en {ciudad}, {pais}"
print(presentacion)