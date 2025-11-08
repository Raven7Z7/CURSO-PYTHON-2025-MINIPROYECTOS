# Programa: Generador de emails V2
print("*** Sistema Generador de Emails ***")
nombre_usuario = input("Ingrese su nombre: ")
apellidos_usuario = input("Ingrese sus apellidos: ")
nombre_empresa = input("Ingrese el nombre de la empresa: ")
extension_dominio = input("Ingrese la extensión del dominio: ")

# Normalizar variables
nombre_usuario = nombre_usuario.lower().strip().replace(" ",".")
apellidos_usuario = apellidos_usuario.lower().strip().replace(" ",".")
nombre_empresa = nombre_empresa.lower().strip().replace(" ","")
extension_dominio = extension_dominio.strip().lower().replace(" ","")

# Imprimimos email generado
email_generado = f"{nombre_usuario}.{apellidos_usuario}@{nombre_empresa}{extension_dominio}"
print(f"""
Tu nuevo email generado por el sistema es: 
    {email_generado}
    ¡Felicidades!""")