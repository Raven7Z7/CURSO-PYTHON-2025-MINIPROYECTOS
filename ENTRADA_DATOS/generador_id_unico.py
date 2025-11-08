from random import randint
# Programa: Generador de ID único
print("*** Sistema Generador de ID único ***")
nombre_usuario = input("¿Cuál es tu nombre? ")
apellido_usuario = input("¿Cuál es tu apellido? ")
anio_nacimiento = input("¿Cuál es tu año de nacimiento (YYYY)? ") # Y - year
valor_aleatorio = randint(1000, 9999)

print(f"Hola {nombre_usuario},\n"
      "\tTu nuevo número de identificación (ID) generado por el sistema es:\n"
      f"\t{nombre_usuario[0:2].upper()}{apellido_usuario[0:2].upper()}{anio_nacimiento[2:].upper()}{valor_aleatorio}\n"
      "\t¡Felicidades!")