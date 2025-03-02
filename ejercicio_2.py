def diag(caracteres):
    for i, char in enumerate(caracteres):
        # Imprimimos el carácter con un número de espacios igual a su índice
        print(' ' * i + char)

if __name__ == "__main__":
    lista_de_caracteres = input("Ingrese una lista de caracteres separados por espacios: ").split()
    diag(lista_de_caracteres)
    input("Presione Enter para salir...")
