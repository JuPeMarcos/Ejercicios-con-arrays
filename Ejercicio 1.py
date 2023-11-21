"""
1. Define tres listas de 20 números enteros cada uno, con nombres number, square y cube. Carga las lista number 
con valores aleatorios entre 0 y 100. En la lista square se deben almacenar los cuadrados de los valores que hay 
en number. En la lista cube se deben almacenar los cubos de los valores que hay en number. A continuación, muestra 
el contenido de las tres listas dispuesto en tres columnas.
"""

import random
number = [random.randint(0, 100) for _ in range(20)]
square = [num ** 2 for num in number]
cube = [num ** 3 for num in number]


print("Número\t\tCuadrado\tCubo")

for i in range(20):
    print(number[i], "\t\t", square[i], "\t\t", cube[i])

