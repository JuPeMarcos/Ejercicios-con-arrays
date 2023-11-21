"""
5. Escribe un programa que genere 20 números enteros entre 100 y 999. Estos números se deben introducir en una lista 
de 4 filas por 5 columnas. El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de 
cálculo se tratara. La suma total debe aparecer en la esquina inferior derecha.
"""

import random

# Generar 20 números enteros aleatorios entre 100 y 999
numbers = [random.randint(100, 1000) for _ in range(20)]

# Organizar los números en una lista de 4 filas por 5 columnas
matrix = []
for i in range(4):
    matrix.append(numbers[i * 5: (i + 1) * 5])


# Mostrar la matriz y calcular sumas parciales
print("Matriz de 4x5:")
for row in matrix:
    print(row)

print("\nSumas parciales de filas:")
for row in matrix:
    print(sum(row), end=" | ")

print("\nSumas parciales de columnas:")
for i in range(5):
    print(sum(row[i] for row in matrix), end=" ")

print("\nSuma total:", sum(numbers))

