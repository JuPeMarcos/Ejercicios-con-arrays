"""
3. Escribe un programa que genere 20 números enteros aleatorios entre 0 y 100 y que los almacene en un array de numpy. 
El programa debe ser capaz de pasar todos los números pares a las primeras posiciones del array (del 0 en adelante) y 
todos los números impares a las celdas restantes. Utiliza arrays auxiliares si es necesario.
"""

import numpy as np

# Generar 20 números enteros aleatorios entre 0 y 100 usando NumPy
randoms = np.random.randint(0, 101, 20)

# Separar números pares e impares
par_numbers = randoms[randoms % 2 == 0]
impar_numbers = randoms[randoms % 2 != 0]

# Crear un array con los números pares seguidos de los impares
numbers = np.concatenate((par_numbers,impar_numbers))

print("Array original:")
print(randoms)
print("\nArray con números pares al inicio:")
print(numbers)