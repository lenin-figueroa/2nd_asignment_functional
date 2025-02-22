def posiciones(elemento, lista):
    indices = []  # Creamos una lista vacía para guardar los índices
    for i in range(len(lista)):  # Recorremos la lista con un bucle for
        if lista[i] == elemento:  # Si el elemento actual es igual al buscado
            indices.append(i)  # Agregamos su índice a la lista
    return indices  # Devolvemos la lista de índices

# Ejemplos de uso
resultado1 = posiciones(4, [1, 4, 3, 7, 4, 2])
resultado2 = posiciones([3, 5], [[3, 6], [2, 5]])
resultado3 = posiciones(10, [1, 2, 3])  # Elemento no presente

print(f"Posiciones del 4: {resultado1}")  # Debería mostrar [1, 4]
print(f"Posiciones de [3, 5]: {resultado2}")  # Debería mostrar []
print(f"Posiciones del 10: {resultado3}")  # Debería mostrar []