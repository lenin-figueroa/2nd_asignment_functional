def diag(caracteres):
    for i, char in enumerate(caracteres):
        # Imprimimos el carácter con un número de espacios igual a su índice
        print(' ' * i + char)

# Ejemplo de uso
lista_de_caracteres = ['a', 'b', 'c', 'd', 'e']
diag(lista_de_caracteres)
