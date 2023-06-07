menu = """"
1- Calcular IVA
2- Descuento
3- Calcular IMC
4- Salir
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

def Calcular_iva(costo):
    iva = costo * 0.19
    return iva

def descuento_aplicado(precio, descuento):
    precio_con_descuento = precio - (precio * descuento / 100)
    return precio_con_descuento
    
def Calcular_imc():
    peso = float(input("Ingrese su peso en KG por favor: "))
    estatura = float(input("Ingrese su estatura en METROS por favor: "))
    imc = peso/(estatura**2)
    return imc
                     
def que_tipo_obesidad(imc):
        if imc <= 18.5:   
            return "Bajo peso"
        elif imc < 24.9:
            return "Adecuado"
        elif imc < 29.9:
            return "Sobrepeso"
        elif imc < 34.9:
            return "Obesidad grado 1"
        elif imc < 39.9:
            return "Obesidad grado 2"
        else:   
            return "Obesidad grado 3"    


while True:
    opcion_selecciona = seleccionar_opcion()
    if opcion_selecciona == "1":
        print ("Calcular IVA")
        costo = int(input("Ingrese el costo del producto: "))
        total_iva = Calcular_iva(costo)
        print (f"El costo del IVA es: {total_iva}")
    elif opcion_selecciona == "2":
        print ("Descuento") 
        precio_original = float(input("Ingrese el precio del producto: "))
        porcentaje_descuento = float(input("Ingrese el porcentaje a aplicar: "))
        precio_con_descuento = descuento_aplicado(precio_original, porcentaje_descuento)
        print (f"El precio del producto con descuento es: {precio_con_descuento}")
    elif opcion_selecciona == "3":
        print ("Calcular IMC")
        imc_resultado = Calcular_imc()
        tipo_obesidad = que_tipo_obesidad(imc_resultado)
        print (f"Tu Indice de Masa Corporal (IMC) es {imc_resultado}")
        print (f"Tipo de obesidad: {tipo_obesidad} ")
    elif opcion_selecciona == "4":
            break

    print ("Fin ejercicio")         
    