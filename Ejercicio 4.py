"""
4. Escribe un programa que lea 5 números por teclado y que los almacene en una lista. Rota los elementos de esa lista,
 es decir, el elemento de la posición 0 debe pasar a la posición 1, el de la 1 a la 2, etc. El número que se encuentra 
 en la última posición debe pasar a la posición 0. Finalmente, muestra el contenido de la lista.
"""

num = []
for i in range(5):
    num.append(int(input("Introduce un número: ")))

# Sacar el último número y lo ubicamos en la primera posición
num.insert(0, num.pop())

print(num)
