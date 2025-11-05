# Programa: Generador de email a partir de datos
# Reemplazar el espacio entre los nombres por puntos
nombre_usuario = "Jonathan Bailon Torres"
nombre_usuario_normalizado = nombre_usuario.replace(" ", ".").lower()

nombre_empresa = "Global Mentoring"
dominio = ".com.mx"
dominio_email_normalizado = f"@{nombre_empresa.replace(" ","").lower()}{dominio}"
email_final = f"{nombre_usuario_normalizado.lower()}{dominio_email_normalizado.lower()}"

# Imprimimos los valores a mostrar
print("*** Generador de email ***")
print(f"Nombre de usuario: {nombre_usuario}")
print(f"Nombre de usuario normalizado: {nombre_usuario_normalizado}")
print(f"\nNombre de la empresa: {nombre_empresa}")
print(f"Extensión del dominio: {dominio}")
print(f"Dominio de email normalizado: {dominio_email_normalizado}")
print(f"\nEmail final generado: {email_final}")