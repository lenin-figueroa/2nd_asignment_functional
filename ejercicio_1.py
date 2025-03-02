def contar_negativos(lista):
    # Inicializamos el contador en 0
    contador = 0
    
    # Recorremos la lista
    for numero in lista:
        if numero < 0:  # Verificamos si el número es negativo
            contador += 1  # Incrementamos el contador
            
    return contador

if __name__ == "__main__":
    numeros = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))
    resultado = contar_negativos(numeros)
    print(f"Número de elementos negativos: {resultado}")
    input("Presione Enter para salir...")