# Programa: Crear una receta de cocina con entradas del usuario
print("*** Receta de Cocina ***")
nombre_receta = input("Ingresa el nombre: ")
ingredientes_receta = input("Ingresa los ingredientes: ")
tiempo_receta = int(input("Ingresa el tiempo de preparación (min): "))
dificultad_receta = input("Ingresa la dificultad: ")

# Imprimimos los valores
print("-"*20)
print(f"Nombre receta: {nombre_receta}")
print(f"Ingredientes: {ingredientes_receta}")
print(f"Tiempo de preparación: {tiempo_receta}")
print(f"Dificultad: {dificultad_receta}")