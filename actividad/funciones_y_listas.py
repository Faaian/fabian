
import os
menu = """
1- Ver ubicaciones disponibles.
2- Comprar ticket.
3- Ver compras realizadas.
4- Salir.
"""
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def seleccionar_opcion():
    opcion_valida = False
    while not opcion_valida:
        print("\nBienvenido al Teatro Estrella.")
        print (menu)
        opcion = input("Elija una opción: ")
        if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
            print ("Opción invalida, vuelva a seleccionar")
        else:
            opcion_valida = True
    return opcion

asientos_disponibles = {
    'A': [True] * 10,
    'B': [True] * 10,
    'C': [True] * 10,
    'D': [True] * 10,
    'E': [True] * 10,
    'F': [True] * 10,
    'G': [True] * 10,
    'H': [True] * 10,
    'I': [True] * 10,
    'J': [True] * 10,
    'K': [True] * 10,
    'L': [True] * 10,
    'M': [True] * 10,
    'N': [True] * 10,
    'Ñ': [True] * 10,
    'O': [True] * 10,
    'P': [True] * 10,
    'Q': [True] * 10,
    'R': [True] * 10,
    'S': [True] * 10,
    'T': [True] * 10,
    'U': [True] * 10,
    'V': [True] * 10,
    'W': [True] * 10,
    'X': [True] * 10,
    'Y': [True] * 10,
    'Z': [True] * 10
    }

compras_realizadas = []

def mostrar_ubicaciones():
    print("Ubicaciones disponibles: ")
    for fila, asientos in asientos_disponibles.items():
        fila_caracter = fila + " "
        for asiento in asientos:
            if asiento:
                fila_caracter += 'O '
            else:
                fila_caracter += 'X '
        print(fila_caracter)
    print("")

def comprar_ticket():
    fila_raw = input("Ingrese la fila del asiento (A-Z): ")
    fila = fila_raw.upper()
    columna = int(input("Ingrese la columa del asiento por favor (1-10): "))

    if fila not in asientos_disponibles.keys():
        print("La fila ingresada no esta disponible, vuelva a intentarlo.")

    if columna  < 1 or columna > 10:
        print ("La columna ingresada no es valida, vuelva a intentarlo por favor.")
        return 
    
    if not asientos_disponibles[fila][columna - 1]:
        print("El asiento seleccionado no esta disponible.")
        return
    
    if fila in ["A", "B", "C"]:
        precio = 50
    elif fila in ["D", "E", "F"]:
        precio = 40
    elif fila in ["G", "H", "I"]:
        precio = 30
    else:
        precio = 20

    nombre_cliente = input("Ingrese el nombre del cliente por favor: ")
    asientos_disponibles[fila][columna] = False               
    compra = {
        'Nombre': nombre_cliente,
        'Ubicacion': fila + str(columna),
        'Precio': precio
    } 
    compras_realizadas.append(compra)

    print("¡Compra Realizada exitosamente!")

def ver_compras():
    for compra in compras_realizadas:
        print ("Nombre", compra['Nombre'])
        print ("ubicacion", compra['Ubicacion'])
        print ("Total pagado", compra['Precio']) 
        print ("----------------------------------")
    total_ventas = sum(compra['Precio'] for compra in compras_realizadas) 
    print (f"Total de ventas: {total_ventas}")
    print("")    
        
             

while True:
    limpiar_pantalla()
    opcion_selecciona = seleccionar_opcion()
    if opcion_selecciona == "1":
        limpiar_pantalla()
        print ("Ver ubicaciones disponibles:")
        mostrar_ubicaciones()
        input("Presione Enter para volver al menú principal...")
        
    elif opcion_selecciona == "2":
        limpiar_pantalla()
        print ("Comprar tickets.")
        comprar_ticket()
        input("Presione Enter para volver al menú principal...")
        
    elif opcion_selecciona == "3":
       limpiar_pantalla()
       print ("Ver compras realizadas.")
       ver_compras()
       input("Presione Enter para volver al menú principal...")
    elif opcion_selecciona == "4":
            break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
        input("Presione Enter para continuar...")
     