"""
6. Haz el ejercicio anterior usando numpy y aprovechando sus ventajas.
"""

import numpy as np

# Generar 20 números enteros aleatorios entre 100 y 999
numbers = np.random.randint(100, 1000, 20)

# Organizar los números en una matriz de 4 filas por 5 columnas
matrix = numbers.reshape(4, 5)

# Mostrar la matriz y calcular sumas parciales
print("Matriz de 4x5:")
for row in matrix:
    print(' | '.join(map(str, row)))

print("\nSumas parciales de filas:")
print(np.sum(matrix, axis=1))

print("\nSumas parciales de columnas:")
print(np.sum(matrix, axis=0))

print("\nSuma total:", np.sum(numbers))

