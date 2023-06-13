import numpy as np
menu = """
1- Ver ubicaciones disponibles.
2- Comprar ticket.
3- Ver compras realizadas.
4- Salir.
"""

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
}


while True:
    opcion_selecciona = seleccionar_opcion()
    if opcion_selecciona == "1":
        print ("Ver ubicaciones disponibles.")
        
    elif opcion_selecciona == "2":
        print ("Comprar tickets.") 
        
    elif opcion_selecciona == "3":
       print ("Ver compras realizadas.")
    elif opcion_selecciona == "4":
            break

    print ("Fin ejercicio")      