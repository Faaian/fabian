# Precios de los productos
precio_hamburguesa = 5500
precio_papas = 2500
precio_bebida = 1350

# Variables para manejar los precios y cantidades
subtotal = 0
descuento = 0
total = 0

# Menú de opciones
menu = """
Bienvenido a Wendy McKing. Por favor, seleccione una opción:
1. Hamburguesa - $5500
2. Papas Fritas - $2500
3. Bebidas - $1350
4. Calcular Total
"""

# Función para solicitar una cantidad válida al usuario
def solicitar_cantidad():
    while True:
        cantidad = input("Ingrese la cantidad deseada: ")
        if cantidad.isdigit() and int(cantidad) > 0:
            return int(cantidad)
        else:
            print("Error: Ingrese un número entero mayor a cero.")

# Función para aplicar los descuentos al subtotal
def aplicar_descuento(subtotal):
    if subtotal > 35000:
        return subtotal * 0.75
    elif subtotal > 20000:
        return subtotal * 0.85
    elif subtotal > 10000:
        return subtotal * 0.95
    else:
        return subtotal

# Inicializar el pedido
pedido = {}

# Ciclo principal del programa
while True:
    print(menu)
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cantidad_hamburguesa = solicitar_cantidad()
        pedido["Hamburguesa"] = cantidad_hamburguesa
        subtotal += cantidad_hamburguesa * precio_hamburguesa
    elif opcion == "2":
        cantidad_papas = solicitar_cantidad()
        pedido["Papas Fritas"] = cantidad_papas
        subtotal += cantidad_papas * precio_papas
    elif opcion == "3":
        cantidad_bebida = solicitar_cantidad()
        pedido["Bebidas"] = cantidad_bebida
        subtotal += cantidad_bebida * precio_bebida
    elif opcion == "4":
        # Calcular el total y aplicar descuentos
        total = aplicar_descuento(subtotal)
        break
    else:
        print("Error: Opción inválida. Por favor, seleccione una opción válida.")

# Mostrar resumen del pedido
print("\nResumen del Pedido:")
for producto, cantidad in pedido.items():
    subtotal_producto = cantidad * precio_hamburguesa if producto == "Hamburguesa" else cantidad * precio_papas if producto == "Papas Fritas" else cantidad * precio_bebida
    print(f"{producto}: {cantidad} x ${subtotal_producto}")
print(f"\nSubtotal: ${subtotal}")
print(f"Descuento: ${subtotal - total}")
print(f"Total a pagar: ${total}")
print("\n¡Gracias por su compra!")