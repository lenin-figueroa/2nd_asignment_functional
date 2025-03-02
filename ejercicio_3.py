def cuadrado(cadena):
    # Recorremos la longitud de la cadena para imprimirla en líneas
    for _ in range(len(cadena)):
        print(cadena)

if __name__ == "__main__":
    cadena = input("Ingrese una cadena de caracteres: ")
    cuadrado(cadena)
    input("Presione Enter para salir...")