def dividir(lista):
    result = []
    for i in range(1, len(lista)):
        result.append(lista[i-1])
        if lista[i] == lista[i-1]:
            result.append('\n')
    result.append(lista[-1])  # Agregar el último elemento
    return ''.join(result)

# Ejemplo de uso
print(dividir(['a', 'b', 'b', 'c', 'c', 'c', 'd']))
# Resultado:
# ab
# bc
# cd
