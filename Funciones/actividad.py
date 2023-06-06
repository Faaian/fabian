menu = """"

"""

def menu():
    opcion_valida = False
    while not opcion_valida:
        print(""""
        1- Primera opcion
        2- Segunda opcion
        3- Tercera opcion
        4- Cuarta opcion
        """)
        opcion = input("Elija una opcion por favor: ")
        if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4":
            print("Opcion no valida")
        else:
            opcion_valida = True
    return opcion 

opcion_selecciona = menu()
print(f"Opcion seleccionada: {opcion_selecciona}")