print("*** Generación Ticket de Venta ***")

precio_leche = float(input("Precio leche: "))
precio_pan = float(input("Precio pan: "))
precio_lechuga = float(input("Precio lechuga: "))
precio_platanos = float(input("Precio plátanos: "))
descuento_porcentaje = int(input("¿Aplicar algún descuento (%)?: "))

# Cálculo del subtotal (sin impuestos)
subtotal = precio_lechuga + precio_pan + precio_leche + precio_platanos

# Cálculo del descuento aplicado al subtotal
descuento = subtotal * (descuento_porcentaje/100)

# Subtotal con descuento
subtotal_con_descuento = subtotal - descuento

# Cálculo con impuestos (12%)
impuesto = subtotal_con_descuento * 0.12

# Cálculo total de la compra (con impuestos)
costo_total_compra = subtotal_con_descuento + impuesto
print(f"""
Subtotal: ${subtotal:.2f}
Descuento: ${descuento} ({descuento_porcentaje}%)
Subtotal con descuento: ${subtotal_con_descuento}
Impuesto: (12%): ${impuesto:.2f}
Costo total de la compra: ${costo_total_compra:.2f}""")