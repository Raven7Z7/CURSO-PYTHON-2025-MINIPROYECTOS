print("*** Sistema Autenticación ***")
# Definimos las constantes almacenadas de usuario y contraseña
USUARIO_ALMACENADO, PASSWORD = "Jonathan", "admin"

# Preguntamos al usuario los datos
usuario_pregunta = input("Ingrese el nombre del usuario: ").strip()
password_pregunta = input("Ingrese el password del usuario: ").strip()

# Comprobamos si los datos son iguales
comprobacion = usuario_pregunta == USUARIO_ALMACENADO and PASSWORD == password_pregunta

# Imprimimos el resultado
print(f"¿Los datos son correctos? {comprobacion}")