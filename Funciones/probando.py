def aplicar_descuento(precio, descuento):
    precio_con_descuento = precio - (precio * descuento / 100)
    return precio_con_descuento

precio_original = float(input("Ingrese el precio original del producto: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento a aplicar: "))

precio_con_descuento = aplicar_descuento(precio_original, porcentaje_descuento)
print("El precio con descuento es:", precio_con_descuento)