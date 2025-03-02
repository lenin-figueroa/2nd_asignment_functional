def nded(lista):
    # Usamos un conjunto para encontrar los elementos únicos
    elementos_distintos = set(lista)
    # Devuelve la cantidad de elementos distintos
    return len(elementos_distintos)

if __name__ == "__main__":
    numeros = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))
    resultado = nded(numeros)
    print(f"Número de elementos distintos: {resultado}")
    input("Presione Enter para salir...")