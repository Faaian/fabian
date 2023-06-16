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


asientos_disponibles = {
    'A': [1] * 10,
    'B': [1] * 10,
    'C': [1] * 10,
    'D': [1] * 10,
    'E': [1] * 10,
    'F': [1] * 10,
    'G': [1] * 10,
    'H': [1] * 10,
    'I': [1] * 10,
    'J': [1] * 10,
    'K': [1] * 10,
    'L': [1] * 10,
    'M': [1] * 10,
    'N': [1] * 10,
    'Ñ': [1] * 10,
    'O': [1] * 10,
    'P': [1] * 10,
    'Q': [1] * 10,
    'R': [1] * 10,
    'S': [1] * 10,
    'T': [1] * 10,
    'U': [1] * 10,
    'V': [1] * 10,
    'W': [1] * 10,
    'X': [1] * 10,
    'Y': [1] * 10,
    'Z': [1] * 10
    }

for columna in asientos_disponibles.items():
    columnas = columna + 1 
