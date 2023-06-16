import numpy as np

#Caso tradicional 
matriz = np.array([[0,1,2], [3,4,5]])
for f in range (2):
    for c in range(3):
        print(matriz[f][c])


#Usando listas
lista = [[1,2,3],
         [4,5,6]]

matriz = np.array(lista)
matriz   

nombre = "fabian"

mayus = nombre.upper()

print(mayus)