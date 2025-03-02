def ndedc(lista):
    if not lista:  # Si la lista está vacía
        return 0
    
    count = 1  # Contamos el primer elemento como único
    for i in range(1, len(lista)):
        if lista[i] != lista[i - 1]:  # Si el elemento actual es diferente al anterior
            count += 1  # Aumentamos el contador
            
    return count

if __name__ == "__main__":
    numeros = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))
    resultado = ndedc(numeros)
    print(f"Número de elementos distintos: {resultado}")
    input("Presione Enter para salir...")
