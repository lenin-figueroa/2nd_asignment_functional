def contar_negativos(lista):
    # Inicializamos el contador en 0
    contador = 0
    
    # Recorremos la lista
    for numero in lista:
        if numero < 0:  # Verificamos si el número es negativo
            contador += 1  # Incrementamos el contador
            
    return contador

numeros = [3, -1, 4, -2, 0, -5, 6]
resultado = contar_negativos(numeros)
print(f"Número de elementos negativos: {resultado}")