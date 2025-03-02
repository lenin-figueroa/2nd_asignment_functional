def dividir(lista):
    resultado = []
    for i in range(1, len(lista)):
        resultado.append(lista[i-1])
        if lista[i] == lista[i-1]:
            resultado.append('\n')
    resultado.append(lista[-1])  # Agregar el último elemento
    return ''.join(resultado)

if __name__ == "__main__":
    cadena = input("Ingrese una cadena de caracteres: ")
    print(dividir(cadena))
    input("Presione Enter para salir...")