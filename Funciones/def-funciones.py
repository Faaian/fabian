def sumar (a, b):
    return a + b

suma1 = sumar(15, 78)
print (suma1)
suma2 = sumar (1, 5)
print (suma2)

#funcion sin argumento y sin retorno
def saludo():
    print ("Hola mucho, gusto")

#funcion sin argumento y con retorno
def sumar():
    num1 = 5
    num2 = 4
    return num1 + num2
print ("La suma es: ", sumar())

#funcion con argumento y sin retorno
def sumar(a, b):
    suma = a + b
    print (f"La suma de los dos numeros es: {suma}")
num1 = int(input("Ingrese el primer numeror: "))
num2 = int(input("Ingrese el segundo numero: "))   
sumar (num1, num2)

#funcion con argumento y con retorno
def sumar (a, b):
    suma = a + b
    return suma
num1 = int(input("Por favor ingrese el primer numero: "))
num2 = int(input("Por favor ingrese el segundo numero: "))
print (f"el resultado de la suma es", sumar(num1, num2))
