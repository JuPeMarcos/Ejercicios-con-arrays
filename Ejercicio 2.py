"""
2. Haz el ejercicio anterior usando numpy y aprovechando sus ventajas.
"""

import numpy as np

number = np.random.randint(0, 100, 20)
square = np.square(number)
cube = np.power(number, 3)

print("Número\t\tCuadrado\tCubo")
for i in range(20):
    print(number[i], "\t\t", square[i], "\t\t", cube[i])

