print("*** Valor dentro de rango ***")
# Definimos constantes
VALOR_MINIMO, VALOR_MAXIMO = 0, 5

# Solicitamos al usuario los datos
valor_usuario = int(input(F"Ingrese el valor entre {VALOR_MINIMO} y {VALOR_MAXIMO}: "))

# Realizamos la comprobación del rango
rango_valido = VALOR_MINIMO <= valor_usuario <= VALOR_MAXIMO

# Imprimimos el resultado
print(f"Valor dentro del rango: {rango_valido}")