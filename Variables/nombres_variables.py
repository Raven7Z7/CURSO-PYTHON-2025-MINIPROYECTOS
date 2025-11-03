#Programa: Registro de explorador espacial
#Asignar valores a las variables
nombre_explorador = "Luna Vega"
planeta_origen = "Marte"
edad_explorador = 25
misiones_completadas = 6
nivel_energia = 90

# for = 15 esto provoca un error (no se deben usar keywords o palabras reservadas)

Nivel_Energia = 100 # no es una buena práctica
NIVEL_ENERGIA = 200 # se considera que es una constante
nivel_energía = 300 # no se deben usar caracteres especiales (acentos, ñ)

#Imprimir los valores
print("=== REGISTRO ESPACIAL===")
print("Nombre del explorador:", nombre_explorador)
print("Planeta de origen:", planeta_origen)
print("Edad del explorador:", edad_explorador)
print("Cantidad de misiones completadas:", misiones_completadas)
print("Nivel de energía:", nivel_energia)