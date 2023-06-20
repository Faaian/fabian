ubicaciones = [ 
    ['O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O']
]
   

#for asientos in ubicaciones:
#    print(asientos)
def print_ubicacion_simple():
    for asiento in ubicaciones:
        print(asiento)


def print_ubicaciones():
    for asiento in ubicaciones:
        print_asiento = "|"
        for elemento in asiento:
            print_asiento = f"{print_asiento} {elemento} |"
        print(print_asiento)

print_ubicaciones()

asientos = int(input("Indique la fila: "))
columna = int(input("Indique la columna: "))
asientos = asientos - 1
columna = columna - 1

# asientos >= 0 and asientos <= 1
if 0 <= asientos <= 1:
    if 0 <= columna <=2:
        ubicaciones[asientos][columna] = 'X'     
    else:
        print("Columna no valida...")
else:
    print ("Fila no valida...")

print_ubicaciones()           


   