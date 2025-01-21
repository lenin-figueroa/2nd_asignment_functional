def contar_negativos(lista):
    return len(list(filter(lambda x: x < 0, lista)))

# Ejemplo de uso
print(contar_negativos([-1, 2, -3, 4, -5]))  # Resultado: 3
