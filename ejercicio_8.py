def nded(lista):
    # Usamos un conjunto para encontrar los elementos únicos
    elementos_distintos = set(lista)
    # Devuelve la cantidad de elementos distintos
    return len(elementos_distintos)

numeros = [1, 2, 2, 3, 4, 4, 5]
resultado = nded(numeros)
print(f"Número de elementos distintos: {resultado}")