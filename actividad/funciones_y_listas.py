import numpy as np
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
        print (menu)
        opcion = input("Elija una opción: ")
        if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
            print ("Opción invalida, vuelva a seleccionar")
        else:
            opcion_valida = True
    return opcion

def lista_comprar(ubicaciones):
    print("Ubicaciones disponibles:")
    print("   1 2 3 4 5 6 7 8 9 10")
    for fila, asientos in ubicaciones.items():
        print(fila, end=" ")
        for asiento in asientos:
            print(asiento, end=" ")
        print()

def mostrar_ubicaciones_disponibles(ubicaciones):
    filas = len(ubicaciones)
    columnas = len(ubicaciones["A"])

    matriz = np.empty((filas, columnas), dtype=str)

    for i, (fila, columnas) in enumerate(ubicaciones.items()):
        for j, valor in columnas.items():
            if valor == "O":
                matriz[i, int(j) - 1] = "O"
            else:
                matriz[i, int(j) - 1] = "X"

    print(matriz)

ubicaciones = {
    "A":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "B":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "C":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "D":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "F":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "G":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "H":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "I":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "J":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "K":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "L":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "M":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "N":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "Ñ":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "O":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "P":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "Q":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "R":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "S":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "T":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "U":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "U":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "W":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "X":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "Y":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"},
    "Z":{"1":"O", "2": "O", "3": "O", "4": "O", "5": "O", "6": "O", "7": "O", "8": "O", "9": "O", "10": "O"}
}


while True:
    limpiar_pantalla()
    opcion_selecciona = seleccionar_opcion()
    if opcion_selecciona == "1":
        limpiar_pantalla()
        print ("Ver ubicaciones disponibles:")
        mostrar_ubicaciones_disponibles(ubicaciones)
        input("Presione Enter para volver al menú principal...")
        
    elif opcion_selecciona == "2":
        limpiar_pantalla()
        print ("Comprar tickets.") 
        input("Presione Enter para volver al menú principal...")
        
    elif opcion_selecciona == "3":
       limpiar_pantalla()
       print ("Ver compras realizadas.")
       input("Presione Enter para volver al menú principal...")
    elif opcion_selecciona == "4":
            break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
        input("Presione Enter para continuar...")
     