ubicaciones = [ 
    ['O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O']
]

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