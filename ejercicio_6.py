def posiciones(elemento, lista):
    indices = []  # Creamos una lista vacía para guardar los índices
    for i in range(len(lista)):  # Recorremos la lista con un bucle for
        if lista[i] == elemento:  # Si el elemento actual es igual al buscado
            indices.append(i)  # Agregamos su índice a la lista
    return indices  # Devolvemos la lista de índices

if __name__ == "__main__":
    elemento = int(input("Ingrese el elemento a buscar: "))
    lista = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))
    resultado = posiciones(elemento, lista)
    print(f"Posiciones del {elemento}: {resultado}")
    input("Presione Enter para salir...")